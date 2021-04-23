#MenuTitle: Show Glyphs in Kerning Groups
# -*- coding: utf-8 -*-
"""
Show all glyphs in the kerning groups of the selected glyph in a new tab.
"""

import GlyphsApp

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers
ListOfSelectedGlyphs = [ l.parent for l in Font.selectedLayers if hasattr(l.parent, 'name')]

editString = """"""

for thisGlyph in ListOfSelectedGlyphs:
	allLeftGlyphs = ""
	allRightGlyphs = ""

	leftGroup = thisGlyph.leftKerningGroup
	rightGroup = thisGlyph.rightKerningGroup

	# print '\t', leftGroup, rightGroup
	if leftGroup != None:
		for g in Font.glyphs:
			if g.leftKerningGroup == leftGroup:
				allLeftGlyphs += "/" + g.name
	if rightGroup != None:
		for g in Font.glyphs:
			if g.rightKerningGroup == rightGroup:
				allRightGlyphs += "/" + g.name
	editString += "/%s\nL %s\nR %s\n\n" % (thisGlyph.name, allRightGlyphs, allLeftGlyphs)

	# "/" + g.name + '\n' + allLeftGlyphs + '\n' + allRightGlyphs + '\n\n'

# print allLeftGlyphs
# print allRightGlyphs

Font.newTab( editString )