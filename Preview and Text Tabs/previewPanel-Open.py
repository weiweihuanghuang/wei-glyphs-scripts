#MenuTitle: Open Preview Panel
# -*- coding: utf-8 -*-
__doc__="""
Open preview panel for all tabs
"""
import GlyphsApp
Font = Glyphs.font

# from Foundation import NSPoint, NSValue

frameHeight = 160
# frameHeight = 69

# for eachTab in Font.tabs:
# 	splitView = eachTab.previewSplitView()
# 	Frame = splitView.frame()
# 	splitView.setPosition_ofDividerAtIndex_(Frame.size.height - frameHeight , 0)

Glyphs.defaults["GSPreviewHeight"] = frameHeight
for eachTab in Font.tabs:
	eachTab.previewHeight = frameHeight
	# eachTab.previewView().setValue_forKey_(NSValue.valueWithPoint_(NSPoint(0,0)), "userOffset")
	# eachTab.previewView().setNeedsDisplay_(True)