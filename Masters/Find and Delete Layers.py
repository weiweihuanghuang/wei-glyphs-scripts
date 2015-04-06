#MenuTitle: Find and Delete Layers
# -*- coding: utf-8 -*-
__doc__="""Deletes layers containing the search string in the selected glyphs"""

import GlyphsApp
import vanilla

Doc = Glyphs.currentDocument

class findInLayerNames(object):
	def __init__(self):
		self.w = vanilla.FloatingWindow((280, 40), "Search for")

		self.w.textSearch = vanilla.TextBox((15, 12+2, 67, 14), "Search for:", sizeStyle='small')
		self.w.searchFor = vanilla.EditText((15+67, 12, 110, 19), "[", sizeStyle='small')

		self.w.findButton = vanilla.Button((-80, 12+1, -15, 17), "Delete", sizeStyle='small', callback=self.buttonCallback)
		self.w.setDefaultButton( self.w.findButton )
		
		self.w.center()
		self.w.open()

	def process(thisGlyph, searchFor):
		numberOfLayers = len( thisGlyph.layers )
		for i in range( numberOfLayers )[::-1]:
			thisLayer = thisGlyph.layers[i]
			if thisLayer.layerId != thisLayer.associatedMasterId:
				thisLayerName = thisLayer.name
				if searchFor in thisLayer.name:
					print "%s in %s deleted" % (thisLayerName, thisGlyph.name)
					del thisGlyph.layers[i]

	def buttonCallback(self, sender):
		Font = Glyphs.font
		selectedLayers = Font.selectedLayers
		searchFor = self.w.searchFor.get()		

		Font.disableUpdateInterface()

		for thisLayer in selectedLayers:
			thisGlyph = thisLayer.parent

			thisGlyph.beginUndo()
			process(thisGlyph, searchFor)
			thisGlyph.endUndo()

		Font.enableUpdateInterface()
		Glyphs.showMacroWindow()

findInLayerNames()