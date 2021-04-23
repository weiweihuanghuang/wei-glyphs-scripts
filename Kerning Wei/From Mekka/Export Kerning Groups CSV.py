#MenuTitle: Export Kerning Groups CSV
# -*- coding: utf-8 -*-
__doc__="""
Export a CSV containing info about the glyphs.
"""

import GlyphsApp
import commands
from types import *

thisFont = Glyphs.fonts[0]
otherFont = Glyphs.fonts[1]

thisFont_glyphset = set([g.name for g in thisFont.glyphs])
otherFont_glyphset = set([g.name for g in otherFont.glyphs])

in_thisFont_butNot_otherFont = thisFont_glyphset.difference(otherFont_glyphset)
in_otherFont_butNot_thisFont = otherFont_glyphset.difference(thisFont_glyphset)
in_thisFont_and_otherFont = thisFont_glyphset.intersection(otherFont_glyphset)

in_thisFont_butNot_otherFont = [g.name for g in thisFont.glyphs if g.name in in_thisFont_butNot_otherFont]
in_otherFont_butNot_thisFont = [g.name for g in otherFont.glyphs if g.name in in_otherFont_butNot_thisFont]
in_thisFont_and_otherFont = [g.name for g in otherFont.glyphs if g.name in in_thisFont_and_otherFont]

selectedLayers = thisFont.selectedLayers
filename  = thisFont.familyName + ' metrics'  # filename without ending
ending    = 'csv'       # txt|csv
myDelim   = ";"         # use "\t" for tab
myExportString = ""

def saveFileDialog(message=None, ProposedFileName=None, filetypes=None):
	if filetypes is None:
		filetypes = []
	Panel = NSSavePanel.savePanel().retain()
	if message is not None:
		Panel.setTitle_(message)
	Panel.setCanChooseFiles_(True)
	Panel.setCanChooseDirectories_(False)
	Panel.setAllowedFileTypes_(filetypes)
	if ProposedFileName is not None:
		Panel.setNameFieldStringValue_(ProposedFileName)
	pressedButton = Panel.runModalForTypes_(filetypes)
	if pressedButton == 1: # 1=OK, 0=Cancel
		return Panel.filename()
	return None

def process( thisGlyphName ):
	thisLEFT = thisRIGHT = otherLEFT = otherRIGHT = "None"

	thisGlyph = thisFont.glyphs[thisGlyphName]

	# thisGLyph
	if hasattr(thisGlyph, "leftKerningGroup"):
		thisLEFT = str(thisGlyph.leftKerningGroup)
		thisRIGHT = str(thisGlyph.rightKerningGroup)
	else:
		thisLEFT = thisRIGHT = "NO GLYPH"

	otherGlyph = otherFont.glyphs[thisGlyphName]

	# otherGlyph
	if hasattr(otherGlyph, "leftKerningGroup"):
		otherLEFT = str(otherGlyph.leftKerningGroup)
		otherRIGHT = str(otherGlyph.rightKerningGroup)
	else:
		otherLEFT = otherRIGHT = "NO GLYPH"

	myExportList = [
		str( thisGlyphName ),
		thisLEFT,
		otherLEFT,
		thisRIGHT,
		otherRIGHT,
		]
	return myExportList

for thisListOfGlyphs in [in_thisFont_and_otherFont, in_thisFont_butNot_otherFont, in_otherFont_butNot_thisFont]:
	for thisGlyphName in thisListOfGlyphs:
		print "Processing", thisGlyphName
		myExportString = myExportString + ( myDelim.join( process( thisGlyphName ) ) + '\n' )

filepath = saveFileDialog( message="Export Metrics CSV", ProposedFileName=filename, filetypes=["csv","txt"] )

f = open( filepath, 'w' )
print "Exporting to:", f.name
f.write( "Glyph;this LEFT;other LEFT;this RIGHT;other RIGHT\n" + myExportString )
f.close()
