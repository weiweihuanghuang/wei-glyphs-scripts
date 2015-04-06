#MenuTitle: Show All Kerning Pairs
# -*- coding: utf-8 -*-
__doc__="""
Show All Kerning Pairs for this Master in a new tab
"""
import GlyphsApp
from PyObjCTools.AppHelper import callAfter

Font = Glyphs.font
Doc = Glyphs.currentDocument
selectedLayers = Font.selectedLayers
selectedMaster = Font.selectedFontMaster
masterID = selectedMaster.id

editString = u""""""

def nameMaker(kernGlyph):
	if kernGlyph[0] == "@":
		return kernGlyph[7:]
	else:
		return Font.glyphForId_(kernGlyph).name	

for L in Font.kerning[ masterID ]:
	try:
		for R in Font.kerning[masterID][L]:
			kernPair = "/%s/%s  " % (nameMaker(L), nameMaker(R))
			editString += kernPair
	except:
		pass

callAfter( Doc.windowController().addTabWithString_, editString )
