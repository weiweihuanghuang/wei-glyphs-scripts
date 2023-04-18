#MenuTitle: Show All Glyphs that Use this Glyph as a Component
# -*- coding: utf-8 -*-

from AppKit import NSRange

Font = Glyphs.font
Doc = Glyphs.currentDocument

# # Replace selected text
# TextStoreage = Font.currentTab.graphicView().textStorage()
# Range = Doc.windowController().activeEditViewController().graphicView().selectedRange()
editString = """"""

for l in [ l for l in Font.selectedLayers if l.parent.name]:
	glyphsContainingComponentWithName = Font.glyphsContainingComponentWithName_masterId_(l.parent.name, l.associatedMasterId)
	if glyphsContainingComponentWithName != ():
		editString += "/" + l.parent.name + "  "
		for eachGlyph in glyphsContainingComponentWithName:
			editString += "/" + eachGlyph.name
		editString += "\n"

Font.newTab( editString )