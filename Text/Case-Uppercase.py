#MenuTitle: Case: Uppercase
# -*- coding: utf-8 -*-
"""Converts the selected text to upppercase."""
 
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

def UppercaseString(String):
	UpperString = ""
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
				UpperUnicode = "%0.4X" % ord(LowerString.upper()[0])
				UpperGlyph = Font.glyphForUnicode_(UpperUnicode)
				# if suffix is not None:
				# 	UpperName = UpperGlyph.name + suffix
				# 	UpperGlyph = Font.glyphForName_(UpperName)
				Char = chr(Font.characterForGlyph_(UpperGlyph))
		except Exception as e:
			Glyphs.showMacroWindow()
			print("\n⚠️ Script Error:\n")
			import traceback
			print(traceback.format_exc())
			print()
			raise e
		UpperString += Char
	return UpperString

UpperString = UppercaseString(String)
TextStoreage.replaceCharactersInRange_withString_(Range, UpperString)