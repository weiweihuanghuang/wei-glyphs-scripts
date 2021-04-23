#MenuTitle: Open Preview Panel Medium
# -*- coding: utf-8 -*-
__doc__="""
Open preview panel for all tabs
"""
import GlyphsApp
Font = Glyphs.font

frameHeight = 80
# frameHeight = 69

# for eachTab in Font.tabs:
# 	splitView = eachTab.previewSplitView()
# 	Frame = splitView.frame()
# 	splitView.setPosition_ofDividerAtIndex_(Frame.size.height - frameHeight , 0)

Glyphs.defaults["GSPreviewHeight"] = frameHeight
for eachTab in Font.tabs:
	eachTab.previewHeight = frameHeight