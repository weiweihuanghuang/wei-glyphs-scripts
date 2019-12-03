#MenuTitle: Sync All Metrics in All Masters
# -*- coding: utf-8 -*-
__doc__="""
Sync All Metrics in All Masters.
"""

import GlyphsApp

thisFont = Glyphs.font # frontmost font
listOfSelectedLayers = thisFont.selectedLayers # active layers of selected glyphs

def process( thisGlyph ):
	numberOfLayers = len( thisGlyph.layers )
	for i in range( numberOfLayers )[::-1]:
		thisLayer = thisGlyph.layers[i]
		thisFontMasterID = thisLayer.associatedFontMaster().id
		if thisLayer.layerId == thisFontMasterID:
			thisLayer.syncMetrics()

thisFont.disableUpdateInterface() # suppresses UI updates in Font View

for thisLayer in listOfSelectedLayers:
	thisGlyph = thisLayer.parent
	print "Aligning components in:", thisGlyph.name
	thisGlyph.beginUndo() # begin undo grouping
	process( thisGlyph )
	thisGlyph.endUndo()   # end undo grouping

thisFont.enableUpdateInterface() # re-enables UI updates in Font View