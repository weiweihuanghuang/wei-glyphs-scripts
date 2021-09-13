#MenuTitle: Show All Kerning Pairs in Current Master
# -*- coding: utf-8 -*-
__doc__="""
Show All Kerning Pairs for this Master in a new tab
"""
import GlyphsApp

Font = Glyphs.font
Doc = Glyphs.currentDocument
selectedLayers = Font.selectedLayers
selectedMaster = Font.selectedFontMaster
masterID = selectedMaster.id

editString = u""""""

leftGroupDefaults = {}
rightGroupDefaults = {}
for thisGlyph in Font.glyphs[::-1]:
	if thisGlyph.leftKerningGroup:
		leftGroupDefaults[thisGlyph.leftKerningGroup] = thisGlyph.name
	if thisGlyph.rightKerningGroup:
		rightGroupDefaults[thisGlyph.rightKerningGroup] = thisGlyph.name

def nameMakerL(kernGlyph):
	if kernGlyph[0] == "@":
		Glyphname1 = rightGroupDefaults[kernGlyph[7:]]
		return Glyphname1
	else:
		return Font.glyphForId_(kernGlyph).name	
        
def nameMakerR(kernGlyph):
	if kernGlyph[0] == "@":
		Glyphname2 = leftGroupDefaults[kernGlyph[7:]]
		return Glyphname2
	else:
		return Font.glyphForId_(kernGlyph).name	

for L in Font.kerning[ masterID ]:
	try:
		for R in Font.kerning[masterID][L]:
			kernPair = "/%s/%s  " % (nameMakerL(L), nameMakerR(R))
			editString += kernPair
	except:
		pass

Glyphs.font.newTab(editString)
