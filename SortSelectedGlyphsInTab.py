#MenuTitle: Sort Selected Glyphs in Tab
# -*- coding: utf-8 -*-
""""""
import GlyphsApp
Font = Glyphs.font
Doc = Glyphs.currentDocument

editString = ""
ListOfSelectedGlyphs = [ l.parent.name for l in Font.selectedLayers if hasattr(l.parent, 'name')]
editString = "/" + "/".join( [g.name for g in Glyphs.font.glyphs if g.name in ListOfSelectedGlyphs] )

# Replace selected text
TextStoreage = Font.currentTab.graphicView().textStorage()
Range = Doc.windowController().activeEditViewController().graphicView().selectedRange()

# Convert text string into character string
charString = Font.charStringFromDisplayString_(editString)
TextStoreage.replaceCharactersInRange_withString_(Range, charString)

# Set cursor at start of TextStorage
Font.currentTab.graphicView().setSelectedRange_(NSRange(0,0))

# Font.newTab(editString)