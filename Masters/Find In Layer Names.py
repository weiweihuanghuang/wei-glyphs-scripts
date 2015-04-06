#MenuTitle: Find in Layer Names
# -*- coding: utf-8 -*-
__doc__="""
Reports Glyphs with Layers containing the search string in a new tab"""

import GlyphsApp
import vanilla
from PyObjCTools.AppHelper import callAfter

Doc = Glyphs.currentDocument

class findInLayerNames(object):
	def __init__(self):
		self.w = vanilla.FloatingWindow((280, 40), "Search for")

		self.w.textSearch = vanilla.TextBox((15, 12+2, 67, 14), "Search for:", sizeStyle='small')
		self.w.searchFor = vanilla.EditText((15+67, 12, 110, 19), "[", sizeStyle='small')

		self.w.findButton = vanilla.Button((-80, 12+1, -15, 17), "Find", sizeStyle='small', callback=self.buttonCallback)
		self.w.setDefaultButton( self.w.findButton )
		
		self.w.center()
		self.w.open()
	
	def buttonCallback(self, sender):
		Font = Glyphs.font
		selectedLayers = Font.selectedLayers
		numberOfMasters = len( Font.masters )
		editString = u""
		
		searchFor = self.w.searchFor.get()
		
		for g in Font.glyphs:
			if len( g.layers ) > numberOfMasters:
				for l in [ x for x in g.layers ][numberOfMasters:]:
					if searchFor in l.name:
						print "%s in %s" % (l.name, g.name)
						UpperGlyph = Font.glyphForName_(g.name)
						Char = unichr(Font.characterForGlyph_(UpperGlyph))
						editString += Char
# 		Glyphs.showMacroWindow()
		callAfter( Doc.windowController().addTabWithString_, editString )
findInLayerNames()