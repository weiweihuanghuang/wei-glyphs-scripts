#MenuTitle: Show Kerning Groups
# -*- coding: utf-8 -*-
__doc__="""
"""

import GlyphsApp
import collections
thisFont = Glyphs.font 

rightGlyph_LeftKerningGroup = {}	
rightGlyph_LeftKerningGroup = collections.OrderedDict()
leftGlyph_RightKerningGroup = {}
leftGlyph_RightKerningGroup = collections.OrderedDict()

for g in thisFont.glyphs:
	# g.leftKerningGroup = g.leftKerningGroup
	# g.rightKerningGroup = g.rightKerningGroup
	# right glyph
	if g.leftKerningGroup in rightGlyph_LeftKerningGroup:
		pass
	elif g.leftKerningGroup:
		if thisFont.glyphs[g.leftKerningGroup]:
			rightGlyph_LeftKerningGroup[g.leftKerningGroup] = [g.leftKerningGroup]
		else:
			# print "exception:", g.name
			rightGlyph_LeftKerningGroup[g.leftKerningGroup] = [g.name]

	# left glyph
	if g.rightKerningGroup in leftGlyph_RightKerningGroup:
		pass
	elif g.rightKerningGroup:
		if thisFont.glyphs[g.rightKerningGroup]:
			leftGlyph_RightKerningGroup[g.rightKerningGroup] = [g.rightKerningGroup]
		else:
			# print "exception:", g.name
			leftGlyph_RightKerningGroup[g.rightKerningGroup] = [g.name]

Glyphs.clearLog()

editString = u""""""

editString += "Left:\n"

for groups, glyphs in leftGlyph_RightKerningGroup.items():
	# print groups, glyphs
	editString += "/%s" % glyphs[0]

editString += "\n\nRight:\n"

for groups, glyphs in rightGlyph_LeftKerningGroup.items():
	# print groups, glyphs
	editString += "/%s" % glyphs[0]

# print editString
Glyphs.font.newTab(editString)