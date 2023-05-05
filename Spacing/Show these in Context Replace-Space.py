#MenuTitle: Show these in Context (Space separated items)
# -*- coding: utf-8 -*-
__doc__="""
Show selected items, each separated by /space, in spacing context replacing everything in this tab.
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

# Replace all text instead of new tab:
TextStoreage = Doc.windowController().activeEditViewController().graphicView().textStorage()
String = TextStoreage.text().string()
Range = Doc.windowController().activeEditViewController().graphicView().selectedRange()

# Replace all text
Range.location = 0
Range.length = len(String)

editString = """"""

# Get the name of each selected glyph and insert a '/space\n/space' for new line character instead (/space added to slit this into it's own item)
namesOfSelectedGlyphs = ''.join([ "/%s" % l.parent.name if l.parent.name != "newGlyph" else '/space\n/space' for l in selectedLayers ])
# namesOfSelectedGlyphs = ''.join([ "/%s" % l.parent.name for l in selectedLayers if hasattr(l.parent, 'name')])

originalCharString = ''.join([ "/%s" % l.parent.name if l.parent.name != "newGlyph" else '\n' for l in selectedLayers ])

editList = namesOfSelectedGlyphs.split('/space')
# Removed blank items which were added as a result of filtering out new line characters
editList = list(filter(None, editList))

for i, eachItem in enumerate(editList):
	if eachItem == u"\n":
		if i != len(editList)-1:
			editString += "\n"
	else:
		# Normal kernMaker
		editString += kernMaker(eachItem)
		if i != len(editList)-1:
			editString += """\n"""

# Include original string
editString = "{0}\n{1}".format(originalCharString, editString)


# Replace text in tab
charString = Font.charStringFromDisplayString_(editString)
TextStoreage.replaceCharactersInRange_withString_(Range, charString)

# try:
# 	mod=reload(mod)
# except:
# 	mod=__import__('Replace with GSUB Glyphs')