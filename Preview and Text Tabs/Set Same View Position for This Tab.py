#MenuTitle: Set Same View Position
# -*- coding: utf-8 -*-
__doc__="""
Set tab in current font and other font to to the same view position as this one (also sets the preview panel height) and same master
"""
import GlyphsApp
Font = Glyphs.font

thisTab = Font.currentTab

currentVisibleRect = thisTab.viewPort
currentScale = thisTab.scale
currentSelectedCursor = thisTab.textCursor
currentSelectedRange = thisTab.textRange
currentFrameHeight = thisTab.previewHeight+1
currentMasterIndex =  Font.masterIndex
currentOffset = thisTab.previewView().valueForKey_("userOffset")

# currentOffset = thisTab.previewView.valueForKey_("selectionOffset")
# otherTab.previewView().setValue_forKey_(currentOffset, "selectionOffset")

# print currentVisibleRect
# print currentScale
# print currentFrameHeight

otherTab = Glyphs.fonts[1].currentTab
otherTab.textCursor = currentSelectedCursor
otherTab.textRange = currentSelectedRange
otherTab.scale = currentScale
#otherTab.frameView().zoomViewToVisibleRect_(currentVisibleRect)
#otherTab.frameView().zoomViewToSaveRect_(currentVisibleRect)
#otherTab.frameView().zoomViewToRect_(currentVisibleRect)
otherTab.viewPort = currentVisibleRect

otherTab.previewHeight = currentFrameHeight
otherTab.setMasterIndex_(currentMasterIndex)

otherTab.previewView().setValue_forKey_(NSValue.valueWithPoint_(NSPoint(currentOffset.x, currentOffset.y)), "userOffset")
otherTab.previewView().setNeedsDisplay_(True)
#otherTab.viewPort = currentVisibleRect
