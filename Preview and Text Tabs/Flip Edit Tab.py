#MenuTitle: Flip Edit Tab
# -*- coding: utf-8 -*-
__doc__="""
Flips the edit tab text up-side down
"""

import GlyphsApp
Font = Glyphs.font
Doc = Glyphs.currentDocument

currentGraphicView = Font.currentTab.graphicView()

if currentGraphicView.isFlipped() == 0:
	currentGraphicView.setFlipped_(1)
elif currentGraphicView.isFlipped() == 1:
	currentGraphicView.setFlipped_(0)