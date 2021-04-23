#MenuTitle: Show Kerning Pairs for Space
# -*- coding: utf-8 -*-
__doc__="""
Show Kerning Pairs for this glyph in a new tab.
"""
import GlyphsApp
import traceback

thisFont = Glyphs.font
Doc = Glyphs.currentDocument
selectedLayers = thisFont.selectedLayers
selectedMaster = thisFont.selectedFontMaster
masterID = selectedMaster.id

kernDict = thisFont.kerningDict()
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
				return rightGroups[kernGlyphOrGroup][0]
			except:
				pass
		elif side == "left":
			# left glyph, right kerning group
			try:
				return leftGroups[kernGlyphOrGroup][0]
			except:
				pass
	else:
		return thisFont.glyphForId_(kernGlyphOrGroup).name

editString = u""""""
editStringL = u""""""
editStringR = u""""""

thisGlyph = thisFont.glyphs["space"]
thisGlyphName = thisGlyph.name
rGroupName = str(thisGlyph.rightKerningGroup)
lGroupName = str(thisGlyph.leftKerningGroup)

# print "\t", rGroupName, lGroupName

kernPairListL = []
kernPairListSortedL = []
kernPairListR = []
kernPairListSortedR = []

for L in thisFont.kerning[ masterID ]:
	try:
		# if the this kerning-pair's left glyph matches rGroupName (right side kerning group of thisGlyph)
		if rGroupName == L[7:] or rGroupName == thisFont.glyphForId_(L).name or thisFont.glyphForId_(L).name == thisGlyph.name:
			# for every R counterpart to L in the kerning pairs of rGroupName
			for R in thisFont.kerning[masterID][L]:
				if thisFont.kerning[masterID][L][R] != 0:
					kernPairListL += [nameMaker(R, "right")]
	except:
		# print traceback.format_exc()
		pass

	for R in thisFont.kerning[masterID][L]:
		try:
			# if the R counterpart (class glyph) of L glyph is the selectedGlyph
			if lGroupName == R[7:] or lGroupName == thisFont.glyphForId_(R).name or thisFont.glyphForId_(R).name == thisGlyph.name:
				if thisFont.kerning[masterID][L][R] != 0:
					kernPairListR += [nameMaker(L, "left")]
		except:
			pass

kernPairListSortedL = [g.name for g in Font.glyphs if g.name in kernPairListL]
for everyGlyph in kernPairListSortedL:
	editStringL += "/%s/%s/bar" % (thisGlyphName, everyGlyph)

kernPairListSortedR = [g.name for g in Font.glyphs if g.name in kernPairListR]
for everyGlyph in kernPairListSortedR:
	editStringR += "/%s/%s/bar" % (everyGlyph, thisGlyphName)

# editString = "/bar" + editStringL + "\n\n" + editStringR + "/bar"
editString = "/bar%s\n\n/bar%s" % (editStringL, editStringR)

thisFont.newTab(editString)