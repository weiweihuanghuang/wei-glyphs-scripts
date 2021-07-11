#MenuTitle: Case: Lowercase
# -*- coding: utf-8 -*-
"""Converts the selected text to lowercase."""
 
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

def LowercaseString(String):
	LowString = ""
	for Char in String:
		g = Font.glyphForCharacter_(ord(Char))
		try:
			if ord(Char) > ord(' '):
				name = g.name
				baseName = name
				suffix = None
				periodPos = baseName.find(".")
				if periodPos > 0:
					baseName = name[:periodPos]
					suffix = name[periodPos:]
				LowerGlyph = Font.glyphForName_(baseName)
				LowerString = u"%c" % int(LowerGlyph.unicode, 16)
				LowerUnicode = "%0.4X" % ord(LowerString.lower()[0])
				LowerGlyph = Font.glyphForUnicode_(LowerUnicode)
				# if suffix is not None:
				# 	UpperName = LowerGlyph.name + suffix
				# 	LowerGlyph = Font.glyphForName_(UpperName)
				Char = chr(Font.characterForGlyph_(LowerGlyph))
		except:
			pass
		LowString += Char
	return LowString

LowString = LowercaseString(String)
TextStoreage.replaceCharactersInRange_withString_(Range, LowString)