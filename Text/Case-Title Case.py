#MenuTitle: Case: Title Case
# -*- coding: utf-8 -*-
"""Converts the selected text to title case."""
 
Font = Glyphs.font
Doc = Glyphs.currentDocument
TextStoreage = Doc.windowController().activeEditViewController().graphicView().textStorage()
String = TextStoreage.text().string()
Range = Doc.windowController().activeEditViewController().graphicView().selectedRange()
if Range.length == 0:
	Range.location = 0
	Range.length = len(String)
	
# only selected
# if Range.length == 0:
# 	Range.length = 1

String = String.substringWithRange_(Range)

UpperString = String.title()
TextStoreage.replaceCharactersInRange_withString_(Range, UpperString)