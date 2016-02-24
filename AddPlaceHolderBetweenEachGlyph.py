#MenuTitle: Add Placeholder Between Each Selected Glyph
# -*- coding: utf-8 -*-
""""""
import GlyphsApp
Font = Glyphs.font
Doc = Glyphs.currentDocument

namesOfSelectedGlyphs = [ "/%s" % l.parent.name if hasattr(l.parent, 'name') else "\n" for l in Font.selectedLayers ]
editString = ""

# Replace selected text
TextStoreage = Font.currentTab.graphicView().textStorage()
Range = TextStoreage.selectedRange()

for g in namesOfSelectedGlyphs:
	if g != "\n":
		editString += g + "/Placeholder "
	else:
		editString += g

# Convert text string into character string
charString = Font.charStringFromDisplayString_(editString)
TextStoreage.replaceCharactersInRange_withString_(Range, charString)

# Set cursor at start of TextStorage
TextStoreage.setSelectedRange_(NSRange(0,0))

# Font.newTab(editString)