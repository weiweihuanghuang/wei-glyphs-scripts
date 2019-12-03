#MenuTitle: Delete All Anchors in All Masters of Selected Glyphs
# -*- coding: utf-8 -*-
__doc__="""
Deletes all anchors in all masters of selected glyphs.
"""

import GlyphsApp

Font = Glyphs.font
selectedLayers = Font.selectedLayers

def process( thisGlyph ):
	
	numberOfLayers = len( thisGlyph.layers )
	for i in range( numberOfLayers )[::-1]:
		thisLayer = thisGlyph.layers[i]
		if thisLayer.layerId == thisLayer.associatedMasterId:
			thisLayer.setAnchors_( None )			

Font.disableUpdateInterface()

for thisLayer in selectedLayers:
	thisGlyph = thisLayer.parent

	thisGlyph.beginUndo()
	process( thisGlyph )
	thisGlyph.endUndo()

Font.enableUpdateInterface()