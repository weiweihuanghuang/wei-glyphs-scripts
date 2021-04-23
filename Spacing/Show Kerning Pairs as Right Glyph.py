#MenuTitle: Show Kerning Pairs as Right Glyph
# -*- coding: utf-8 -*-
__doc__="""
Show Kerning Pairs for this glyph in a new tab.
"""
import GlyphsApp

thisFont = Glyphs.font
Doc = Glyphs.currentDocument
selectedLayers = thisFont.selectedLayers
selectedMaster = thisFont.selectedFontMaster
masterID = selectedMaster.id

editString = u""""""

def nameMaker(kernGlyphOrGroup, side):
	# if this is a kerning group
	if kernGlyphOrGroup[0] == "@":
		for g in thisFont.glyphs:
			# right glyph
			if side == "right":
				# left side of right glyph
				if g.leftKerningGroup == kernGlyphOrGroup[7:]:
					return g.name
			if side == "left":
				# right side of left glyph
				if g.rightKerningGroup == kernGlyphOrGroup[7:]:
					return g.name
	else:
		return thisFont.glyphForId_(kernGlyphOrGroup).name

for thisLayer in selectedLayers:
	thisGlyph = thisLayer.parent
	thisGlyphName = thisGlyph.name
	rGroupName = str(thisGlyph.rightKerningGroup)
	lGroupName = str(thisGlyph.leftKerningGroup)

	# for L in thisFont.kerning[ masterID ]:
	# 	try:
	# 		# if the this kerning-pair's left glyph matches rGroupName (right side kerning group of thisGlyph)
	# 		if L[0] == "@" and rGroupName == L[7:] or rGroupName == thisFont.glyphForId_(L).name or thisFont.glyphForId_(L).name == thisGlyph.name:
	# 			# for every R counterpart to L in the kerning pairs of rGroupName
	# 			for R in thisFont.kerning[masterID][L]:
	# 				if thisFont.kerning[masterID][L][R] != 0:
	# 					kernPair = "/%s/%s  " % (thisGlyphName, nameMaker(R, "right"))
	# 					editString += kernPair
	# 	except:
	# 		pass

		for R in thisFont.kerning[masterID][L]:
			try:
				# if the R counterpart (class glyph) of L glyph is the selectedGlyph
				if R[0] == "@" and lGroupName == R[7:] or lGroupName == thisFont.glyphForId_(R).name or thisFont.glyphForId_(R).name == thisGlyph.name:
					if thisFont.kerning[masterID][L][R] != 0:
						kernPair = "/%s/%s  " % (nameMaker(L, "left"), thisGlyphName)
						editString += kernPair
			except:
				pass

thisFont.newTab(editString)