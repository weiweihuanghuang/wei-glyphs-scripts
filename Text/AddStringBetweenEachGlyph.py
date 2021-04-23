from __future__ import print_function
#MenuTitle: Add String Between Each Selected Glyph
# -*- coding: utf-8 -*-
__doc__="""
Adds this string between each selected glyph, must be in /slash format"""

import GlyphsApp
import vanilla

class insertString(object):
	def __init__(self):
		self.w = vanilla.FloatingWindow(
			( 360, 40 ), # default window size
			"Add this /s/t/r/i/n/g between selected glyphs", # window title
			autosaveName = "com.wwhh.insertString.mainwindow" # stores last window position and size
			)

		self.w.textAdd = vanilla.TextBox((10, 12+2, 32, 14), "Add:", sizeStyle='small')
		self.w.addThisString = vanilla.EditText((10+32, 12, 220, 19), "", sizeStyle='small', callback=self.SavePrefs)

		self.w.findButton = vanilla.Button((-80, 12+1, -15, 17), "Add", sizeStyle='small', callback=self.buttonCallback)
		self.w.setDefaultButton( self.w.findButton )

		if not self.LoadPrefs( ):
			print("Note: Could not load preferences. Will resort to defaults.")

		self.w.open()

	def buttonCallback(self, sender):
		Font = Glyphs.font
		Doc = Glyphs.currentDocument
		selectedLayers = Font.selectedLayers
		addThisString = self.w.addThisString.get()

		namesOfSelectedGlyphs = [ "/%s" % l.parent.name if l.parent.name else "\n" for l in Font.selectedLayers ]
		editString = ""

		# Replace selected text
		TextStoreage = Font.currentTab.graphicView().textStorage()
		Range = Doc.windowController().activeEditViewController().graphicView().selectedRange()

		editString = addThisString

		for g in namesOfSelectedGlyphs:
			if g != "\n":
				editString += g + addThisString
			else:
				editString += g

		try:
			# Convert text string into character string
			charString = Font.charStringFromDisplayString_(editString)
			TextStoreage.replaceCharactersInRange_withString_(Range, charString)

			# Set cursor at start of TextStorage
			Font.currentTab.graphicView().setSelectedRange_(NSRange(0,0))
		except:
			pass


	def SavePrefs( self, sender ):
		Glyphs.defaults["com.wwhh.insertString.savedAddThisString"] = self.w.addThisString.get()
		return True

	def LoadPrefs( self ):
		try:
			self.w.addThisString.set( Glyphs.defaults["com.wwhh.insertString.savedAddThisString"] )
			return True
		except:
			return False


insertString()