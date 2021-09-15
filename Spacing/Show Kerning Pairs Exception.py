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

leftGroups = {}
rightGroups = {}
for g in thisFont.glyphs:
	if g.rightKerningGroup:
		group_name = g.rightKerningGroupId()
		try:
			leftGroups[group_name].append(g.name)
		except:
			leftGroups[group_name] = [g.name]

	if g.leftKerningGroup:
		group_name = g.leftKerningGroupId()
		try:
			rightGroups[group_name].append(g.name)
		except:
			rightGroups[group_name] = [g.name]

def nameMaker(kernGlyphOrGroup, side):
	# if this is a kerning group
	if kernGlyphOrGroup[0] == "@":
		# right glyph, left kerning group
		if side == "right":
			try:
				# return rightGroups[kernGlyphOrGroup][0]
				return sorted(rightGroups[kernGlyphOrGroup], key=len)[0]
			except:
				pass
		elif side == "left":
			# left glyph, right kerning group
			try:
				# return leftGroups[kernGlyphOrGroup][0]
				return sorted(leftGroups[kernGlyphOrGroup], key=len)[0]
			except:
				pass
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

	for L in thisFont.kerning[ masterID ].keys():
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
				for R in thisFont.kerning[masterID][L].keys():
					if thisFont.kerning[masterID][L][R] < 8e+10:
						# print "L: L @R, L R\t", L, R
						# print "\t", "%s, %s" % (thisGlyphName, nameMaker(R, "right"))
						kernPair = "/%s/%s  " % (thisGlyphName, nameMaker(R, "right"))
						editString += kernPair
		except:
			pass

		for R in thisFont.kerning[masterID][L].keys():
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