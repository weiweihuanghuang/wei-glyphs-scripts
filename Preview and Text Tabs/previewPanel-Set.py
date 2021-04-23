#MenuTitle: Set Preview Panel
# -*- coding: utf-8 -*-
__doc__="""
Set preview panel height and master across every tab to the same as this tab
"""
import GlyphsApp
Font = Glyphs.font
Doc = Glyphs.currentDocument

thisTab = Font.currentTab
currentFrameHeight = thisTab.previewHeight+1
# currentMasterIndex =  thisTab.masterIndex()
# PreviewField = Doc.windowController().activeEditViewController()
currentInstanceNumber = Font.currentTab.previewInstances

for eachTab in Font.tabs:
	eachTab.previewHeight = currentFrameHeight
	# eachTab.setMasterIndex_(currentMasterIndex) # Set current master
	eachTab.previewInstances = currentInstanceNumber # Set same preview instance