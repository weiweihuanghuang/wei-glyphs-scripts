#MenuTitle: Delete Kerning Pairs In Text
# -*- coding: utf-8 -*-
__doc__="""
Deletes all selected kerning pairs present in selected text
"""

import GlyphsApp

Font = Glyphs.font
Master = Font.selectedFontMaster
selectedLayers = Font.selectedLayers
masterID = Master.id

listOfG = []
for l in selectedLayers:
    if hasattr(l.parent, 'name'):
        listOfG.append(l.parent)
    else:
		listOfG.append("None")

pairsToBeDeleted = []

def nameMaker(kernGlyph):
	if kernGlyph[0] == "@":
		return "@%s" % kernGlyph[7:]
	else:
		return kernGlyph

def uniquify(seq):
    seen = set()
    return [x for x in seq if x not in seen and not seen.add(x)]

for glyphIndex, eachGlyph in enumerate(listOfG):
	if eachGlyph != "None":
		glyphName = eachGlyph.name
		# set whether there is kerning class or not for left glyph
		if eachGlyph.rightKerningGroup is not None:
			glyphClass = "@MMK_L_{0}".format(eachGlyph.rightKerningGroup)
		else:
			glyphClass = glyphName
		nextGlyphIndex = glyphIndex + 1
		if nextGlyphIndex < len(listOfG) and listOfG[nextGlyphIndex] != "None":
			nextGlyph = listOfG[nextGlyphIndex]
			nextGlyphName = nextGlyph.name
			# set whether there is kerning class or not for right glyph
			if nextGlyph.rightKerningGroup is not None:
				nextGlyphClass = "@MMK_R_{0}".format(nextGlyph.leftKerningGroup)
			else:
				nextGlyphClass = nextGlyphName 
			pairsToBeDeleted.append( (glyphClass, nextGlyphClass) )
			pairsToBeDeleted.append( (glyphName, nextGlyphName) )
			pairsToBeDeleted.append( (glyphName, nextGlyphClass) )
			pairsToBeDeleted.append( (glyphClass, nextGlyphName) )

Font.disableUpdateInterface()
for kernPair in uniquify(pairsToBeDeleted):
	leftGlyphName = kernPair[0]
	rightGlyphName = kernPair[1]
	if Font.kerningForPair( masterID, leftGlyphName, rightGlyphName ) < 9e+17:
		try:
			print "Deleting %s %s: %s" % ( nameMaker(leftGlyphName), nameMaker(rightGlyphName), Font.kerningForPair( masterID, leftGlyphName, rightGlyphName ) ) 
			Font.removeKerningForPair( masterID, leftGlyphName, rightGlyphName )
		except Exception, e:
			print "-- Error: could not delete pair %s %s (%s)" % ( leftGlyphName, rightGlyphName, e )
Font.enableUpdateInterface()