#MenuTitle: Show All Kerning Pairs
# -*- coding: utf-8 -*-
__doc__="""
Show All Kerning Pairs for this Master in a new tab
"""
import GlyphsApp
# this script is flawed because its not comparing when it makes a GLYPH GLYPH whether the kerning pair has an exception, so it should get the kerning pair first, then check whether the @MMK GLYPH, or GLYPH @MMK, or @MMK @MMK is the same as GLYPH GLYPH, if not then go to next glyph in the group, otherwise in the end just go with the glyph (cus then there's no other instance where the @MMK kerning would apply)

thisFont = Glyphs.font
Doc = Glyphs.currentDocument
selectedLayers = thisFont.selectedLayers
selectedMaster = thisFont.selectedFontMaster
masterID = selectedMaster.id

editString = u""""""

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

for L in thisFont.kerning[ masterID ].keys():
	try:
		for R in thisFont.kerning[masterID][L].keys():
			kernPair = "/%s/%s/space" % (nameMaker(L, "left"), nameMaker(R, "right")) 
			editString += kernPair
	except:
		pass

# print editString

thisFont.newTab(editString)