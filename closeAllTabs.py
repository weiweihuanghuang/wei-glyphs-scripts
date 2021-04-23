#MenuTitle: Close All Tabs
# -*- coding: utf-8 -*-
__doc__="""
Close All Tabs in this font"""

import GlyphsApp
thisFont = Glyphs.font
for i in range(len(thisFont.tabs)):
    del thisFont.tabs[0]
