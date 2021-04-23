#MenuTitle: Show Each Glyph in Context
# -*- coding: utf-8 -*-
__doc__="""
Show each selected glyph in spacing context in a new tab.
"""
import GlyphsApp
import kernMakerFunc
import importlib
importlib.reload(kernMakerFunc)
from kernMakerFunc import kernMaker

# Glyphs.clearLog()
Font = Glyphs.font
Doc = Glyphs.currentDocument
selectedLayers = Font.selectedLayers
namesOfSelectedGlyphs = [ "/%s" % l.parent.name if l.parent.name != None else "\n" for l in selectedLayers ]

# Replace all text instead of new tab:
TextStoreage = Doc.windowController().activeEditViewController().graphicView().textStorage()
String = TextStoreage.text().string()
Range = Doc.windowController().activeEditViewController().graphicView().selectedRange()
Range.location = 0 # Replace all text
Range.length = len(String) # Replace all text

editString = ""

for index, eachItem in enumerate(namesOfSelectedGlyphs):
	if eachItem == "\n" and index != (len(selectedLayers)-1):
		editString += "\n"
	elif eachItem != "\n" and eachItem != "/space":
		editString += kernMaker(eachItem)
		editString += "\n"

editString = "{0}\n{1}".format("".join(namesOfSelectedGlyphs), editString)

# print editString

# Replace text in tab
charString = Font.charStringFromDisplayString_(editString)
TextStoreage.replaceCharactersInRange_withString_(Range, charString)