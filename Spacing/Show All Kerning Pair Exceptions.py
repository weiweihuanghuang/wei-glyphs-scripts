#MenuTitle: Show All Kerning Pair Exceptions
# -*- coding: utf-8 -*-
__doc__="""
Show All Kerning Pair Exceptions for this Master in a new tab
"""
import GlyphsApp

thisFont = Glyphs.font
Doc = Glyphs.currentDocument
selectedLayers = thisFont.selectedLayers
selectedMaster = thisFont.selectedFontMaster
masterID = selectedMaster.id

editString = u""""""
errorString = u""""""


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


for L in thisFont.kerning[ masterID ].keys():
	# L @R, L R
	# if this is L glyph kerning and L does have a rightKerningGroup (i.e. it is an exception)
	if L[0] != "@":
		if thisFont.glyphs[thisFont.glyphForId_(L).name].rightKerningGroup != None:
			for R in thisFont.kerning[masterID][L].keys():

				# L R
				if R[0] != "@":
					kernPair = "/%s/%s/space" % (thisFont.glyphForId_(L).name, thisFont.glyphForId_(R).name) 
					editString += kernPair

				# L @R
				else:
					if nameMaker(R, "right") != None:
						kernPair = "/%s/%s/space" % (thisFont.glyphForId_(L).name, nameMaker(R, "right")) 
						editString += kernPair
					else:
						errorString += "%s, %s\n" % (thisFont.glyphForId_(L).name, R)

	# @L R
	else:
		for R in thisFont.kerning[masterID][L].keys():
			# if this is R glyph kerning but R does have a leftKerningGroup (i.e. it is an exception)
			if R[0] != "@":
				if thisFont.glyphs[thisFont.glyphForId_(R).name].leftKerningGroup != None:
					if nameMaker(L, "left") != None:
						kernPair = "/%s/%s/space" % (nameMaker(L, "left"), thisFont.glyphForId_(R).name) 
						editString += kernPair
					else:
						errorString += "%s, %s\n" % (L, thisFont.glyphForId_(R).name)

# L R
	# Check if these glyphs have kerning groups:
		# Right side of @L
		# Left side of @R
# L @R
	# Check if these glyphs have kerning groups:
		# Right side of @L
# @L R
	# Check if these glyphs have kerning groups:
		# Left side of @R

thisFont.newTab(editString)
print "The following kerning pairs had a group without glyphs in the kerning group:"
print errorString