#MenuTitle: Adjust Kerning in specified glyph only WORKING MANUAL
# -*- coding: utf-8 -*-
__doc__="""
Adjusts kerning values for a specified glyph by a specified amount.
"""

import vanilla
import GlyphsApp

optionList = [ "Multiply by", "Add", "Add Absolute", "Round by" ]

def nameForID( Font, ID ):
	try:
		if ID[0] == "@": # is a group
			return ID
		else: # is a glyph
			return Font.glyphForId_( ID ).name
	except Exception as e:
		raise e

try:
	Font = Glyphs.font
	Master = Font.selectedFontMaster
	MasterID = Master.id
	MasterKernDict = Font.kerning[ MasterID ]
	kernGlyph = "t"
	Font.disableUpdateInterface()

	valueL = float( 10 ) # glyph is on left
	valueR = float( 0 ) # glyph is on right

	for leftGlyphID in MasterKernDict.keys():
		leftName = nameForID( Font, leftGlyphID )
		# Finds kernGlyph in Left glyph
		if leftName[0] =="@" and leftName[7:] == kernGlyph or leftName == kernGlyph:
			for rightGlyphID in MasterKernDict[ leftGlyphID ].keys():
				originalKerning = MasterKernDict[ leftGlyphID ][ rightGlyphID ]
				rightName = nameForID( Font, rightGlyphID )

				# Set kerning
				if Font.kerningForPair( MasterID, leftName, rightName ) != 0:
					Font.setKerningForPair( MasterID, leftName, rightName, originalKerning + valueL )
					print "Setting kerning for %s, %s, %s" % (leftName, originalKerning + valueL, rightName)
		# Finds kernGlyph in Right glyph
		for rightGlyphID in MasterKernDict[ leftGlyphID ].keys():
			originalKerning = MasterKernDict[ leftGlyphID ][ rightGlyphID ]
			rightName = nameForID( Font, rightGlyphID )

			# Set kerning
			if rightName[0] =="@" and rightName[7:] == kernGlyph or rightName == kernGlyph:
				if Font.kerningForPair( MasterID, leftName, rightName ) != 0:
					print "Setting kerning for %s, %s, %s" % (leftName, originalKerning + valueR, rightName)
					Font.setKerningForPair( MasterID, leftName, rightName, originalKerning + valueR )

	Font.enableUpdateInterface()
	
except Exception, e:
	raise e