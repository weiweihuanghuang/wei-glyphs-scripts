#MenuTitle: Set Kerning Groups to the Component 
# -*- coding: utf-8 -*-
__doc__="""
"""

# Need to detect for suffixes

import GlyphsApp

Glyphs.clearLog() # clears macro window log
thisFont = Glyphs.font # frontmost font
thisFontMaster = thisFont.selectedFontMaster # active master
listOfSelectedLayers = [ l for l in thisFont.selectedLayers if hasattr(l.parent, 'name')]
 # active layers of selected glyphs

listOfFailures = ""

def process( thisLayer ):
	thisGlyph = thisLayer.parent
	global listOfFailures
	name = thisGlyph.name
	baseName = name
	suffix = ""
	periodPos = baseName.find(".")

	if periodPos > 0:
		baseName = name[:periodPos]
		suffix = name[periodPos:]

	if ".sc" in suffix:
		suffix = ""

	try:
		baseComponentGlyph = thisLayer.components[0].name

		leftKerningGroupBaseGlyph = baseComponentGlyph
		thisGlyph.leftKerningGroup = Glyphs.font.glyphs[leftKerningGroupBaseGlyph].leftKerningGroup
		print "Left kerning group of %s to: %s" % (thisGlyph.name, leftKerningGroupBaseGlyph)

		rightKerningGroupBaseGlyph = baseComponentGlyph
		thisGlyph.rightKerningGroup = Glyphs.font.glyphs[rightKerningGroupBaseGlyph].rightKerningGroup
		print "Right kerning group of %s to: %s" % (thisGlyph.name, rightKerningGroupBaseGlyph)
	except:
		listOfFailures += "/%s" % thisGlyph.name


thisFont.disableUpdateInterface() # suppresses UI updates in Font View

for thisLayer in listOfSelectedLayers:
	# thisLayer.beginUndo() # begin undo grouping
	process( thisLayer )
	# thisLayer.endUndo()   # end undo grouping

thisFont.enableUpdateInterface() # re-enables UI updates in Font View

thisFont.newTab(listOfFailures)
print "These were unchanged:\n%s" % " ".join(listOfFailures.split("/"))