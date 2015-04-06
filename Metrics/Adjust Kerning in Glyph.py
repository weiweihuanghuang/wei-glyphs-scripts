#MenuTitle: Adjust Kerning in Glyph
# -*- coding: utf-8 -*-
__doc__="""
Adjusts all kerning values by a specified amount.
"""

import vanilla
import GlyphsApp

optionList = [ "Multiply by", "Add", "Add Absolute", "Round by" ]

class AdjustKerning( object ):
	def __init__( self ):
		self.w = vanilla.FloatingWindow( (350, 140), "Adjust Kerning", minSize=(350, 140), maxSize=(600, 140), autosaveName="com.wwhh.AdjustKerningTwo.mainwindow" )

		self.w.text_1 = vanilla.TextBox( (15-1, 12+2, -15, 14), "All kerning pairs in the current Master:", sizeStyle='small' )
		self.w.popup_1 = vanilla.PopUpButton( (15, 36, 100, 17), optionList, callback=self.SavePreferences, sizeStyle='small' )

		self.w.text_2 = vanilla.TextBox( (15+100+6, 38, 40, 19), "L:", sizeStyle='small' )
		self.w.value_1 = vanilla.EditText((15+100+24, 36, 40, 19), "10", sizeStyle='small', callback=self.SavePreferences)

		self.w.text_3 = vanilla.TextBox( (15+100+20+40+8, 38, 40, 19), "R:", sizeStyle='small' )
		self.w.value_2 = vanilla.EditText((15+100+20+40+24, 36, 40, 19), "10", sizeStyle='small', callback=self.SavePreferences)
		
		self.w.runButton = vanilla.Button((-80-15, 36, -15, 17), "Adjust", sizeStyle='small', callback=self.AdjustKerningMain )
		self.w.setDefaultButton( self.w.runButton )
		
		self.w.text_4 = vanilla.TextBox( (15-1, 66, -15, 14), "For name/class:", sizeStyle='small' )

		self.w.value_3 = vanilla.EditText((15+100+10, 64, -80-15-16, 19), "A", sizeStyle='small', callback=self.SavePreferences)

		
		self.w.keepWindow = vanilla.CheckBox( (15, 92, -15, 20), "Keep window open", value=False, callback=self.SavePreferences, sizeStyle='small' )
		
		
		try:
			self.LoadPreferences( )
		except:
			pass

		self.w.open()
		
	def SavePreferences( self, sender ):
		try:
			Glyphs.defaults["com.wwhh.AdjustKerning.popup_1"] = self.w.popup_1.get()
			Glyphs.defaults["com.wwhh.AdjustKerning.value_1"] = self.w.value_1.get()
			Glyphs.defaults["com.wwhh.AdjustKerning.value_2"] = self.w.value_2.get()
			Glyphs.defaults["com.wwhh.AdjustKerning.value_3"] = self.w.value_3.get()
			Glyphs.defaults["com.wwhh.AdjustKerning.keepWindow"] = self.w.keepWindow.get()
		except:
			return False
			
		return True

	def LoadPreferences( self ):
		try:
			self.w.popup_1.set( Glyphs.defaults["com.wwhh.AdjustKerning.popup_1"] )
			self.w.value_1.set( Glyphs.defaults["com.wwhh.AdjustKerning.value_1"] )
			self.w.value_2.set( Glyphs.defaults["com.wwhh.AdjustKerning.value_2"] )
			self.w.value_3.set( Glyphs.defaults["com.wwhh.AdjustKerning.value_3"] )
			self.w.keepWindow.set( Glyphs.defaults["com.wwhh.AdjustKerning.keepWindow"] )
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

	def AdjustKerningMain( self, sender ):
		Font = Glyphs.font
		Master = Font.selectedFontMaster
		MasterID = Master.id
		MasterKernDict = Font.kerning[ MasterID ]

		Font.disableUpdateInterface()
		
		calculation = str( self.w.popup_1.getItems()[ self.w.popup_1.get() ] )
		valueL = float( self.w.value_1.get() )
		valueR = float( self.w.value_2.get() )
		kernGlyph = self.w.value_3.get()
		
		if calculation == optionList[0]:

			for leftGlyphID in MasterKernDict.keys():
				leftName = nameForID( Font, leftGlyphID )
				# Finds kernGlyph in Left glyph
				if leftName[0] =="@" and leftName[7:] == kernGlyph or leftName == kernGlyph:
					for rightGlyphID in MasterKernDict[ leftGlyphID ].keys():
						originalKerning = MasterKernDict[ leftGlyphID ][ rightGlyphID ]
						rightName = nameForID( Font, rightGlyphID )

						# Set kerning
						Font.setKerningForPair( MasterID, leftName, rightName, originalKerning * valueL )
						
				# Finds kernGlyph in Right glyph
				for rightGlyphID in MasterKernDict[ leftGlyphID ].keys():
					originalKerning = MasterKernDict[ leftGlyphID ][ rightGlyphID ]
					rightName = nameForID( Font, rightGlyphID )

					# Set kerning
					if rightName[0] =="@" and rightName[7:] == kernGlyph or rightName == kernGlyph:
						Font.setKerningForPair( MasterID, leftName, rightName, originalKerning * valueR )

		elif calculation == optionList[1]:
			
			for leftGlyphID in MasterKernDict.keys():
				leftName = self.nameForID( Font, leftGlyphID )

				for rightGlyphID in MasterKernDict[ leftGlyphID ].keys():
					originalKerning = MasterKernDict[ leftGlyphID ][ rightGlyphID ]
					rightName = self.nameForID( Font, rightGlyphID )

					Font.setKerningForPair( MasterID, leftName, rightName, originalKerning + value )
					
		elif calculation == optionList[2]:
			
			for leftGlyphID in MasterKernDict.keys():
				leftName = self.nameForID( Font, leftGlyphID )

				for rightGlyphID in MasterKernDict[ leftGlyphID ].keys():
					originalKerning = MasterKernDict[ leftGlyphID ][ rightGlyphID ]
					rightName = self.nameForID( Font, rightGlyphID )

					if originalKerning < 0:
						factor = -1
					else:
						factor = 1
					Font.setKerningForPair( MasterID, leftName, rightName, originalKerning + factor * value )
					
		elif calculation == optionList[3]:
			
			for leftGlyphID in MasterKernDict.keys():
				leftName = self.nameForID( Font, leftGlyphID )
				
				for rightGlyphID in MasterKernDict[ leftGlyphID ].keys():
					originalKerning = MasterKernDict[ leftGlyphID ][ rightGlyphID ]
					rightName = self.nameForID( Font, rightGlyphID )

					Font.setKerningForPair( MasterID, leftName, rightName, round( originalKerning / value, 0 ) * value )
			
		Font.enableUpdateInterface()
		
		if not self.SavePreferences( self ):
			print "Note: could not write preferences."
		
		if not self.w.keepWindow.get():
			self.w.close()

AdjustKerning()
