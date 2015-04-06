#MenuTitle: Clear Every Master Layer
# -*- coding: utf-8 -*-
__doc__="""
Clears every master layer and places content in background.
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
			thisLayer.setBackground_( thisLayer )
			thisLayer.setPaths_( None )
			thisLayer.setComponents_( None )
			thisLayer.setAnchors_( None )

thisFont.disableUpdateInterface() # suppresses UI updates in Font View

for thisLayer in listOfSelectedLayers:
	thisGlyph = thisLayer.parent
	print "Clearing ", thisGlyph.name
	thisGlyph.beginUndo() # begin undo grouping
	process( thisGlyph )
	thisGlyph.endUndo()   # end undo grouping

thisFont.enableUpdateInterface() # re-enables UI updates in Font View
