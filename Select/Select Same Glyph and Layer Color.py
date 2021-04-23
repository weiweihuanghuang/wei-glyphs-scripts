#MenuTitle: Select Same Glyph and Layer Color
# -*- coding: utf-8 -*-
__doc__="""
In Font view, select glyphs with the same color(s) and layer color as the currently selected one(s).
"""

import GlyphsApp

def indexSetWithIndex( index ):
	indexSet = NSIndexSet.alloc().initWithIndex_( index )
	return indexSet

thisFont = Glyphs.font
thisDoc = Glyphs.currentDocument # frontmost document
try:
    fontView = thisDoc.windowController().tabBarControl().tabItemAtIndex_(0).glyphsArrayController()
except:
    fontView = thisDoc.windowController().tabBarControl().viewControllers()[0].glyphsArrayController()
displayedGlyphsInFontView = fontView.arrangedObjects() # all glyphs currently displayed
glyphColorIndexes = []
LayerColorIndexes = []

if displayedGlyphsInFontView:
	displayedIndexRange = range(len(displayedGlyphsInFontView)) # indexes of glyphs in Font view
	for i in displayedIndexRange:
		if fontView.selectionIndexes().containsIndex_(i):
			thisGlyphColorIndex = displayedGlyphsInFontView[i].colorIndex()
			thisLayerColorIndex = displayedGlyphsInFontView[i].layers[thisFont.selectedFontMaster.id].colorIndex()
			if not thisGlyphColorIndex in glyphColorIndexes:
				glyphColorIndexes.append( thisGlyphColorIndex )
			if not thisLayerColorIndex in LayerColorIndexes:
				LayerColorIndexes.append( thisLayerColorIndex )
	if glyphColorIndexes:
		for i in displayedIndexRange:
			if displayedGlyphsInFontView[i].colorIndex() in glyphColorIndexes and displayedGlyphsInFontView[i].layers[thisFont.selectedFontMaster.id].colorIndex() in LayerColorIndexes:
				fontView.addSelectionIndexes_( indexSetWithIndex(i) )