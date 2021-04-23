#MenuTitle: Round Kerning to units of 5
# encoding: utf-8

__doc__="""
Rounds the kerning values to units of 5.

In addition, values smaller than MIN_VALUE are erased.
"""

MIN_VALUE = 2

from GlyphsApp import *
font = Glyphs.font

def myround(x, base=5):
	return int(base * round(float(x)/base))

printString = """"""

for eachFontMaster in font.masters:
	eachFontMasterId = eachFontMaster.id
	to_be_removed = []

	for first, seconds in dict( font.kerning[eachFontMasterId] ).items():
		if not first.startswith('@'):
			first = font.glyphForId_( first ).name
		for second in seconds:
			if not second.startswith('@'):
				second = font.glyphForId_( second ).name
			# round towards 5
			existingValue = font.kerningForPair( eachFontMasterId, first, second )
			value = myround( existingValue, 5)
			if abs( existingValue ) < MIN_VALUE:
				to_be_removed.append( ( first, second, existingValue ) )
			elif existingValue != value :
				font.setKerningForPair( eachFontMasterId, first, second, value )
				printString += "%s\t%s: %s, %s, %s\n" % (value, eachFontMaster.name, first, second, existingValue) 

	for first, second, existingValue in to_be_removed:
		font.removeKerningForPair( eachFontMasterId, first, second )
		printString += "0\t%s: %s, %s, %s\n" % (eachFontMaster.name, first, second, existingValue) 

print printString