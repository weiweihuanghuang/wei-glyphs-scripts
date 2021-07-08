#MenuTitle: Show Kerning Pairs
# -*- coding: utf-8 -*-
__doc__="""
Show Kerning Pairs for this glyph in a new tab.
"""
import GlyphsApp

Font = Glyphs.font
Doc = Glyphs.currentDocument
selectedLayers = Font.selectedLayers
selectedMaster = Font.selectedFontMaster
masterID = selectedMaster.id

editString = u""""""
editStringL = u"""L: """
editStringR = u"""R: """

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

	for L in Font.kerning[ masterID ].keys():
		try:
			# if the this kerning-pair's left glyph matches rGroupName (right side kerning group of thisGlyph)
			if L[0] == "@" and rGroupName == L[7:] or rGroupName == Font.glyphForId_(L).name or Font.glyphForId_(L).name == thisGlyph.name:
				# for every R counterpart to L in the kerning pairs of rGroupName
				for R in Font.kerning[masterID][L].keys():
					if Font.kerning[masterID][L][R] != 0:
						kernPair = "/%s/%s  " % (thisGlyphName, nameMaker(R))
						editStringL += kernPair
		except:
			pass

		for R in Font.kerning[masterID][L].keys():
			try:
				# if the R counterpart (class glyph) of L glyph is the selectedGlyph
				if R[0] == "@" and lGroupName == R[7:] or lGroupName == Font.glyphForId_(R).name or Font.glyphForId_(R).name == thisGlyph.name:
					if Font.kerning[masterID][L][R] != 0:
						kernPair = "/%s/%s  " % (nameMaker(L), thisGlyphName)
						editStringR += kernPair
			except:
				pass


editString = editStringL + "\n\n" + editStringR
Glyphs.font.newTab(editString)