#MenuTitle: Show Each Glyph in Context (New Tab)
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
namesOfSelectedGlyphs = [i for i in namesOfSelectedGlyphs if i != "/space"]

editString = ""

for index, eachItem in enumerate(namesOfSelectedGlyphs):
	if eachItem == "\n" and index != (len(selectedLayers)-1):
		editString += "\n"
	elif eachItem != "\n" and eachItem != "/space":
		editString += kernMaker(eachItem)
		editString += "\n"

editString = "{0}\n{1}".format("".join(namesOfSelectedGlyphs), editString)

# print editString
Font.newTab(editString)