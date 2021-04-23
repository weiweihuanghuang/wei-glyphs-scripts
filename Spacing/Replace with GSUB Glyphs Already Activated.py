#MenuTitle: Replace with GSUB Glyphs (Already Activated)
# -*- coding: utf-8 -*-
__doc__="""
Activates features then replaces the whole tab with its substituted glyph, i.e. /a => /a.sc
"""
if __name__ != '__main__':
	from __main__ import *
import GlyphsApp

Font = Glyphs.font
Doc = Glyphs.currentDocument

# Replace all text instead of new tab:
TextStoreage = Doc.windowController().activeEditViewController().graphicView().textStorage()
String = TextStoreage.text().string()
Range = Doc.windowController().activeEditViewController().graphicView().selectedRange()
originalLocation = Range.location
Range.location = 0 # Replace all text
Range.length = len(String) # Replace all text

editTab = Glyphs.currentDocument.windowController().activeEditViewController()

# Replace text with substituted glyphs
TextGlyphs = Doc.windowController().activeEditViewController().graphicView().layoutManager().cachedGlyphs()
editString = ""

namesOfSelectedGlyphs = [ "/%s" % l.parent.name if l.parent.name != None else "\n" for l in TextGlyphs ]

editString = "".join(namesOfSelectedGlyphs)

featureList = [ f for f in editTab.selectedFeatures() ]
for featureItem in featureList:
	editTab.selectedFeatures().remove(featureItem)
editTab.graphicView().reflow()
editTab.graphicView().layoutManager().updateActiveLayer()
editTab._updateFeaturePopup()

charString = Font.charStringFromDisplayString_(editString)
TextStoreage.replaceCharactersInRange_withString_(Range, charString)
Font.currentTab.graphicView().setSelectedRange_((originalLocation, 0))
# TextStoreage.setSelectedRange_((originalLocation, 0))