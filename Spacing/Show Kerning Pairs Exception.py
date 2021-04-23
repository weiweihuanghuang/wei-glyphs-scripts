#MenuTitle: Show Kerning Pairs Exception
# -*- coding: utf-8 -*-
__doc__="""
Show Kerning Exception Pairs for this glyph in a new tab.
"""
import GlyphsApp

thisFont = Glyphs.font
Doc = Glyphs.currentDocument
selectedLayers = thisFont.selectedLayers

namesOfSelectedGlyphs = [ l.parent.name for l in selectedLayers if hasattr(l.parent, 'name')]
namesOfSelectedGlyphs = [i for i in namesOfSelectedGlyphs if i != "/space"]

selectedMaster = thisFont.selectedFontMaster
masterID = selectedMaster.id

# Look for:
	# New Tab for every glyph
# to make it every glyph new tab


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


# One Tab for all
editString = u""""""

for thisGlyphName in namesOfSelectedGlyphs:

	# New Tab for every glyph
	# editString = u""""""
	thisGlyph = thisFont.glyphs[thisGlyphName]
	rGroupName = str(thisGlyph.rightKerningGroup)
	lGroupName = str(thisGlyph.leftKerningGroup)

	for L in thisFont.kerning[ masterID ]:
		try:
			# If L matches thisGlyph or its right side group
			# @L R
			# if L[0] == "@" and rGroupName == L[7:] or rGroupName == thisFont.glyphForId_(L).name:
			# 	# for every R counterpart to L in the kerning pairs of rGroupName
			# 	for R in thisFont.kerning[masterID][L]:
			# 		# R is not group kerning
			# 		if thisFont.kerning[masterID][L][R] != 0 and R[0] != "@":
			# 			print "L: @L R\t\t", L, R
			# 			print "\t", "%s, %s" % (thisGlyphName, nameMaker(R, "right"))
			# 			kernPair = "/%s/%s  " % (thisGlyphName, nameMaker(R, "right"))
			# 			editString += kernPair
			# L @R, L R
			if thisFont.glyphForId_(L).name == thisGlyph.name:
				# for every R counterpart to L in the kerning pairs of rGroupName
				for R in thisFont.kerning[masterID][L]:
					if thisFont.kerning[masterID][L][R] < 8e+10:
						# print "L: L @R, L R\t", L, R
						# print "\t", "%s, %s" % (thisGlyphName, nameMaker(R, "right"))
						kernPair = "/%s/%s  " % (thisGlyphName, nameMaker(R, "right"))
						editString += kernPair
		except:
			pass

		for R in thisFont.kerning[masterID][L]:
			try:
				# If R matches thisGlyph or its left side group
				# L @R
				# if R[0] == "@" and lGroupName == R[7:] or lGroupName == thisFont.glyphForId_(R).name:
				# 	if thisFont.kerning[masterID][L][R] != 0 and L[0] != "@":
				# 		print "R: L @R\t\t", L, R
				# 		print "\t", "%s, %s" % (nameMaker(L, "left"), thisGlyphName)
				# 		kernPair = "/%s/%s  " % (nameMaker(L, "left"), thisGlyphName)
				# 		editString += kernPair

				# @L R, L R
				if thisFont.glyphForId_(R).name == thisGlyph.name:
					if thisFont.kerning[masterID][L][R] < 8e+10:
						# print "R: @L R, L R\t", L, R
						# print "\t", "%s, %s" % (nameMaker(L, "left"), thisGlyphName)
						kernPair = "/%s/%s  " % (nameMaker(L, "left"), thisGlyphName)
						editString += kernPair
			except:
				pass

	# New Tab for every glyph
	# thisFont.newTab(editString)

	# One Tab for all
	# editString += "\n"
thisFont.newTab(editString)