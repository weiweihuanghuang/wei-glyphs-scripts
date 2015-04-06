#MenuTitle: Show these in Context (Space separated items)
# -*- coding: utf-8 -*-
__doc__="""
Show selected items, each separated by /space, in spacing context in a new tab.
"""
import GlyphsApp
from PyObjCTools.AppHelper import callAfter
from kernMakerFunc import kernMaker

Glyphs.clearLog()
Font = Glyphs.font
Doc = Glyphs.currentDocument
selectedLayers = Font.selectedLayers
selectedMaster = Font.selectedFontMaster
masterID = selectedMaster.id

editList = []
editListItem = ""
editString = ""

for index, thisLayer in enumerate(selectedLayers):
	thisGlyph = thisLayer.parent
	if hasattr(thisGlyph, 'name'):
		thisGlyphName = thisGlyph.name
		if thisGlyphName != "space":
			_thisGlyphName = "/" + thisGlyphName
			editListItem += _thisGlyphName
			# print editListItem
			# if the next item is a space and is not the last one, add the editListItem to editList
			if index != len(selectedLayers)-1 and hasattr(selectedLayers[index+1].parent, 'name') and selectedLayers[index+1].parent.name == "space": 
				editList += [editListItem]
				editListItem = ""
		if index == (len(selectedLayers)-1) and thisGlyphName != "space": # when the item is the last one add the editListItem to editList
			editList += [editListItem]
			editListItem = ""
	else: # if the glyph has no name add the editListItem to editList
		if editListItem != "":
			editList += [editListItem]
			editListItem = ""

for eachItem in editList:
	editString += kernMaker(eachItem, "lc")

# print editString
callAfter( Doc.windowController().addTabWithString_, editString )