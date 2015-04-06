#MenuTitle: Show Glyphs in Kerning Groups
# -*- coding: utf-8 -*-
"""
Show all glyphs in the kerning groups of the selected glyph in a new tab.
"""

import GlyphsApp
from PyObjCTools.AppHelper import callAfter

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers

allLeftGlyphs = "L "
allRightGlyphs = "R "

for l in selectedLayers:
	thisGlyph = l.parent
	leftGroup = thisGlyph.leftKerningGroup
	rightGroup = thisGlyph.rightKerningGroup
	print '\t', leftGroup, rightGroup
	for g in Font.glyphs:
		if g.leftKerningGroup and g.leftKerningGroup == leftGroup:
			allLeftGlyphs += "/" + g.name
		if g.rightKerningGroup and g.rightKerningGroup == rightGroup:
			allRightGlyphs += "/" + g.name

print allLeftGlyphs
print allRightGlyphs

callAfter( Doc.windowController().addTabWithString_, allLeftGlyphs + '\n' + allRightGlyphs )