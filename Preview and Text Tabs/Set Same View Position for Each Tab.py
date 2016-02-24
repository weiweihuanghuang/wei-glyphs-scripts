#MenuTitle: Set Same View Position Across Tabs
# -*- coding: utf-8 -*-
__doc__="""
Set every tab to the same view position as this one (also sets the preview panel height)
"""
import GlyphsApp
Font = Glyphs.font

thisTab = Font.currentTab

currentGraphicView = thisTab.graphicView()
currentActivePosition = currentGraphicView.activePosition() # This could be used to just the visibleRect
currentVisibleRect = currentGraphicView.visibleRect()
currentScale = currentGraphicView.scale()
currentSelectedRange = currentGraphicView.textStorage().selectedRange()
currentFrameHeight = thisTab.previewHeight

for eachTab in Font.tabs:
	eachTab.previewHeight = currentFrameHeight
	thisGraphicView = eachTab.graphicView()
	if eachTab == Font.currentTab:
		continue
	thisGraphicView.textStorage().setSelectedRange_(currentSelectedRange)
	thisGraphicView.zoomViewToAbsoluteScale_(currentScale)
	thisGraphicView.scrollRectToVisible_(currentVisibleRect)