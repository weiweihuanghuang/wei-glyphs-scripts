#MenuTitle: Set Preview Panel
# -*- coding: utf-8 -*-
__doc__="""
Set preview panel height and master across every tab to the same as this tab
"""
import GlyphsApp
Font = Glyphs.font

# thisEditViewController = Glyphs.currentDocument.windowController().activeEditViewController()
# currentMasterIndex =  thisEditViewController.masterIndex()

# frameHeight = Font.currentTab.previewView().frame().size.height

# for eachTab in Font.tabs:
# 	splitView = eachTab.previewSplitView()
# 	Frame = splitView.frame()
# 	splitView.setPosition_ofDividerAtIndex_(Frame.size.height - frameHeight - 1, 0)
# 	eachTab.setMasterIndex_(currentMasterIndex)

thisTab = Font.currentTab
currentFrameHeight = thisTab.previewHeight
currentMasterIndex =  thisTab.masterIndex()
# currentPreviewInstance = thisTab.previewInstances

for eachTab in Font.tabs:
	eachTab.previewHeight = currentFrameHeight
	# eachTab.setMasterIndex_(currentMasterIndex) # Set current master
	# eachTab.previewInstances = Glyphs.font.instances[-1] # Set same preview instance