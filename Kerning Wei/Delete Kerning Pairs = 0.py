#MenuTitle: Delete Kerning Pairs = 0
# -*- coding: utf-8 -*-
__doc__="""
"""

import GlyphsApp

def nameForID( Font, ID ):
	try:
		if ID[0] == "@": # is a group
			return ID
		else: # is a glyph
			return Font.glyphForId_( ID ).name
	except Exception as e:
		raise e

Font = Glyphs.font
Master = Font.selectedFontMaster
MasterID = Master.id
MasterKernDict = Font.kerning[ MasterID ]


Font.disableUpdateInterface()

LeftKeys = MasterKernDict.keys()[:]
for leftGlyphID in LeftKeys:
	leftName = nameForID( Font, leftGlyphID )
	RightKeys = MasterKernDict[ leftGlyphID ].keys()[:]
	for rightGlyphID in RightKeys:
		originalKerning = MasterKernDict[ leftGlyphID ][ rightGlyphID ]
		if abs(originalKerning) <= 0:
			rightName = nameForID( Font, rightGlyphID )
			print "Deleting %s %s %s kerning pair" % (leftName, originalKerning, rightName)
			Font.removeKerningForPair( MasterID, leftName, rightName )

Font.enableUpdateInterface()