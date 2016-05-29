#MenuTitle: Name This
# -*- coding: utf-8 -*-
__doc__="""
Add a label for this guideline, anchor, point
"""

import GlyphsApp
import vanilla

class nameThisPoint(object):
	def __init__(self):
		self.w = vanilla.FloatingWindow(
			( 280, 40 ), # default window size
			"Name This Point", # window title
			autosaveName = "com.wwhh.namethispoint.mainwindow" # stores last window position and size
			)

		self.w.textSearch = vanilla.TextBox((15, 12+2, 67, 14), "Set Name:", sizeStyle='small')
		self.w.pointName = vanilla.EditText((15+67, 12, 110, 19), "", sizeStyle='small', callback=self.SavePreferences)

		self.w.findButton = vanilla.Button((-80, 12+1, -15, 17), "Set Name", sizeStyle='small', callback=self.buttonCallback)
		self.w.setDefaultButton( self.w.findButton )

		# Load Settings:
		if not self.LoadPreferences():
			print "Note: 'Name This' could not load preferences. Will resort to defaults"

		self.w.open()
		self.w.makeKey()

		# Set defaults for class variables
		self.pointName = self.w.pointName.get()

	def SavePreferences( self, sender ):
		try:
			Glyphs.defaults["com.wwhh.namethispoint.pointName"] = self.w.pointName.get()
		except:
			return False
		return True

	def LoadPreferences( self ):
		try:
			NSUserDefaults.standardUserDefaults().registerDefaults_(
				{
					"com.wwhh.namethispoint.namethispoint": ""
				}
			)
			self.w.pointName.set( Glyphs.defaults["com.wwhh.namethispoint.pointName"] )
		except:
			return False
		return True

	def buttonCallback(self, sender):
		pointName = self.w.pointName.get()

		Font = Glyphs.font
		for p in Layer.selection:
			p.name = pointName

nameThisPoint()
