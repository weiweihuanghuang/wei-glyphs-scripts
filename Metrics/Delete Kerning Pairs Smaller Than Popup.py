#MenuTitle: Delete Kerning Pairs Smaller Than #
# -*- coding: utf-8 -*-
__doc__="""
Delete all kerning pairs equal to or smaller than # in selected master
"""

import vanilla
import GlyphsApp

class deleteKerning( object ):
	def __init__( self ):
		self.w = vanilla.FloatingWindow( (200, 110), "Delete Kerning", minSize=(180, 110), maxSize=(600, 110), autosaveName="com.wwhh.DeleteKerning.mainwindow" )

		self.w.text_1 = vanilla.TextBox( (15-1, 12+2, -15, 14), "All kerning pairs in this Master smaller than:", sizeStyle='small' )
		self.w.value_1 = vanilla.EditText((15, 36, 50, 19), "10", sizeStyle='small', callback=self.SavePreferences)

		self.w.runButton = vanilla.Button((-100, 36, -10, 17), "Adjust", sizeStyle='small', callback=self.DeleteKerningMain )
		self.w.setDefaultButton( self.w.runButton )

		self.w.keepWindow = vanilla.CheckBox( (15, 60, -15, 20), "Keep window open", value=False, callback=self.SavePreferences, sizeStyle='small' )

		try:
			self.LoadPreferences( )
		except:
			pass

		self.w.open()

	def SavePreferences( self, sender ):
		try:
			Glyphs.defaults["com.wwhh.DeleteKerning.popup_1"] = self.w.popup_1.get()
			Glyphs.defaults["com.wwhh.DeleteKerning.value_1"] = self.w.value_1.get()
			Glyphs.defaults["com.wwhh.DeleteKerning.keepWindow"] = self.w.keepWindow.get()
		except:
			return False

		return True

	def LoadPreferences( self ):
		try:
			self.w.popup_1.set( Glyphs.defaults["com.wwhh.DeleteKerning.popup_1"] )
			self.w.value_1.set( Glyphs.defaults["com.wwhh.DeleteKerning.value_1"] )
			self.w.keepWindow.set( Glyphs.defaults["com.wwhh.DeleteKerning.keepWindow"] )
		except:
			return False

		return True

	def nameForID( self, Font, ID ):
		try:
			if ID[0] == "@": # is a group
				return ID
			else: # is a glyph
				return Font.glyphForId_( ID ).name
		except Exception as e:
			raise e

	def DeleteKerningMain( self, sender ):
		try:
			Font = Glyphs.font
			Master = Font.selectedFontMaster
			MasterID = Master.id
			MasterKernDict = Font.kerning[ MasterID ]

			maxKerningSize = float(self.w.value_1.get())

			Font.disableUpdateInterface()

			LeftKeys = MasterKernDict.keys()[:]
			for leftGlyphID in LeftKeys:
				leftName = self.nameForID( Font, leftGlyphID )
				RightKeys = MasterKernDict[ leftGlyphID ].keys()[:]
				for rightGlyphID in RightKeys:
					originalKerning = MasterKernDict[ leftGlyphID ][ rightGlyphID ]
					if abs(originalKerning) <= maxKerningSize:
						rightName = self.nameForID( Font, rightGlyphID )
						print "Deleting %s %s %s kerning pair" % (leftName, originalKerning, rightName)
						Font.removeKerningForPair( MasterID, leftName, rightName )

			Font.enableUpdateInterface()
		except Exception, e:
			raise e

deleteKerning()