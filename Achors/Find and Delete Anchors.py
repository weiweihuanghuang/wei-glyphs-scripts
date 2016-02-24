#MenuTitle: Find and Delete Anchors
# -*- coding: utf-8 -*-
__doc__="""
Find and deletes all anchors in active layers of selected glyphs that contains the search string.
"""

import GlyphsApp
import vanilla

class findInLayerNames(object):
	def __init__(self):
		self.w = vanilla.FloatingWindow(
			( 280, 40 ), # default window size
			"Find and Delete Anchor Containing", # window title
			autosaveName = "com.wwhh.FindAnchors.mainwindow" # stores last window position and size
			)

		self.w.textSearch = vanilla.TextBox((15, 12+2, 67, 14), "Search for:", sizeStyle='small')
		self.w.searchFor = vanilla.EditText((15+67, 12, 110, 19), "bottom", sizeStyle='small', callback=self.SavePreferences)

		self.w.findButton = vanilla.Button((-80, 12+1, -15, 17), "Delete", sizeStyle='small', callback=self.buttonCallback)
		self.w.setDefaultButton( self.w.findButton )

		# Load Settings:
		if not self.LoadPreferences():
			print "Note: 'Adjust Kerning in Master' could not load preferences. Will resort to defaults"

		self.w.open()
		self.w.makeKey()

		# Set defaults for class variables
		self.searchFor = self.w.searchFor.get()

	def SavePreferences( self, sender ):
		try:
			Glyphs.defaults["com.wwhh.FindAnchors.searchFor"] = self.w.searchFor.get()
		except:
			return False
		return True

	def LoadPreferences( self ):
		try:
			NSUserDefaults.standardUserDefaults().registerDefaults_(
				{
					"com.wwhh.FindAnchors.searchFor": "bottom"
				}
			)
			self.w.searchFor.set( Glyphs.defaults["com.wwhh.FindAnchors.searchFor"] )
		except:
			return False
		return True

	def buttonCallback(self, sender):
		Font = Glyphs.font
		selectedLayers = Font.selectedLayers
		searchFor = self.w.searchFor.get()

		for thisLayer in selectedLayers:
			try:
				thisGlyph = thisLayer.parent
				delList = []
				for anchor in thisLayer.anchors:
					anchorName = str(anchor.name)
					if searchFor in anchorName:
						delList += [anchorName]
				# print "Deleting anchors in %s:" % thisGlyph.name
				for anchor in delList:
					print "Deleting %s in %s" % (anchor, thisGlyph.name)
					thisGlyph.beginUndo()
					del(thisLayer.anchors[anchor])
					thisGlyph.endUndo()
			except Exception, e:
				raise e
		Glyphs.showMacroWindow()

findInLayerNames()