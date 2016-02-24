#MenuTitle: Set Same Master Across Tabs
# -*- coding: utf-8 -*-
__doc__="""
Set every tab to the same master as this one
"""
import GlyphsApp
Font = Glyphs.font

thisTab = Font.currentTab
currentMasterIndex =  thisTab.masterIndex()

for eachTab in Font.tabs:
	if eachTab.masterIndex() == currentMasterIndex:
		continue
	eachTab.setMasterIndex_(currentMasterIndex) # Set current master
	# eachTab.previewInstances = Glyphs.font.instances[-1] # Set same preview instance