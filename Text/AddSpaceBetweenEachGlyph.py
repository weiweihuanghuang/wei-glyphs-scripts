#MenuTitle: Add Space Between Each Selected Glyph
# -*- coding: utf-8 -*-
""""""
from __future__ import print_function
import GlyphsApp
Font = Glyphs.font
Doc = Glyphs.currentDocument

namesOfSelectedGlyphs = [ "/%s" % l.parent.name if l.parent.name else "\n" for l in Font.selectedLayers ]
editString = ""

# Replace selected text
TextStoreage = Font.currentTab.graphicView().textStorage()
Range = Doc.windowController().activeEditViewController().graphicView().selectedRange()

for g in namesOfSelectedGlyphs:
	if g != "\n":
		editString += g + "/space"
	else:
		editString += g

print(editString)

# Convert text string into character string
charString = Font.charStringFromDisplayString_(editString)
TextStoreage.replaceCharactersInRange_withString_(Range, charString)

# Set cursor at start of TextStorage
Font.currentTab.graphicView().setSelectedRange_(NSRange(0,0))

# Font.newTab(editString)