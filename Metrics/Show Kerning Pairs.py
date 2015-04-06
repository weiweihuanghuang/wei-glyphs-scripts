#MenuTitle: Show Kerning Pairs
# -*- coding: utf-8 -*-
__doc__="""
Show Kerning Pairs for this glyph in a new tab.
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

for thisLayer in selectedLayers:
	thisGlyph = thisLayer.parent
	thisGlyphName = thisGlyph.name
	rGroupName = str(thisGlyph.rightKerningGroup)
	lGroupName = str(thisGlyph.leftKerningGroup)

	for L in Font.kerning[ masterID ]:
		try:
			# if the this kerning-pair's left glyph matches rGroupName (right side kerning group of thisGlyph)
			if L[0] == "@" and rGroupName == L[7:] or rGroupName == Font.glyphForId_(L).name or Font.glyphForId_(L).name == thisGlyph.name:
				# for every R counterpart to L in the kerning pairs of rGroupName
				for R in Font.kerning[masterID][L]:
					kernPair = "/%s/%s  " % (thisGlyphName, nameMaker(R))
					editString += kernPair
		except:
			pass

		for R in Font.kerning[masterID][L]:
			try:
				# if the R counterpart (class glyph) of L glyph is the selectedGlyph
				if R[0] == "@" and lGroupName == R[7:] or lGroupName == Font.glyphForId_(R).name or Font.glyphForId_(R).name == thisGlyph.name:
					kernPair = "/%s/%s  " % (nameMaker(L), thisGlyphName)
					editString += kernPair
			except:
				pass

callAfter( Doc.windowController().addTabWithString_, editString )
