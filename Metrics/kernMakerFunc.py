# -*- coding: utf-8 -*-
# The function that creates the kerning text, define your own texts

if __name__ != '__main__':
	from __main__ import *
import GlyphsApp

def subCat(eachGlyph, subCat):
	if Glyphs.glyphInfoForName( eachGlyph ).subCategory == subCat:
		return True
	else:
		return False

def kernMaker(kernPair, Option=None):

	myGlyphs = kernPair.split('/')
	# Remove blank items in myGlyphs
	myGlyphs = filter(None, myGlyphs)
	# print myGlyphs

	# Default Fallback
	# return u"""HOH{0} non HOH{0} HOH non{0} npn\nHHH{0} nnn HHH{0} HHH nnn{0} nnn\nOOO{0} ooo OOO{0} OOO ooo{0} ooo\nXHX{0} xhx XHX{0} XHX xox{0} xox""".format(kernPair)
	# return u"""nn{0} nono{0} oo""".format(kernPair)
	# pass

	if Option == "Basic":
		return u"""non{0} nonnn{0} nnoo{0} ooo""".format(kernPair) # Basic

	# UC UC
	elif all(subCat(eachGlyph, "Uppercase") for eachGlyph in myGlyphs):
		return u"""HOH{0} HOH HHH{0} HHH OOO{0} OOO""".format(kernPair) # Basic
		# return u"""HH{0} HOHOO""".format(kernPair) # Basic Alt
		# return u"""HOH{0} HOH HHH{0} HHH OOO{0} OOO XHX{0} XHX""".format(kernPair) # Full

	# UC lc
	elif subCat(myGlyphs[0], "Uppercase") and subCat(myGlyphs[-1], "Lowercase") :
		# return u"""HOH{0} non\nHHH{0} nnn\nOOO{0} ooo\nXHX{0} xox""".format(kernPair) # \n
		return u"""HOH{0} non HHH{0} nnn OOO{0} ooo XHX{0} xox""".format(kernPair)

	# lc UC
	elif subCat(myGlyphs[0], "Lowercase") and subCat(myGlyphs[-1], "Uppercase") :
		return u"""non{0} HOH\nnnn{0} HHH\nooo{0} OOO\nxhx{0} XOX""".format(kernPair)

	# lc lc
	elif subCat(myGlyphs[0], "Lowercase") and subCat(myGlyphs[-1], "Lowercase") :
		return u"""non{0} nonnn{0} nnoo{0} ooo""".format(kernPair) # Basic
		# return u"""non{0} non nnn{0} nnn ooo{0} ooo xox{0} xox""".format(kernPair) # Full
		# return u"""non{0} nonnn{0} nnnooo{0} oooxox{0} xox""".format(kernPair) # Full Alt

	# UC sc
	elif subCat(myGlyphs[0], "Uppercase") and subCat(myGlyphs[-1], "Smallcaps") :
		return u"""HOH{0} /h.sc /o.sc /h.sc \nHHH{0} /h.sc /h.sc /h.sc \nOOO{0} /o.sc /o.sc /o.sc \nXHX{0} /x.sc /h.sc /x.sc """.format(kernPair)

	# sc sc
	elif all(subCat(eachGlyph, "Smallcaps") for eachGlyph in myGlyphs):
		return u"""/n.sc/o.sc/n.sc {0} /n.sc/o.sc/n.sc/n.sc/n.sc {0} /n.sc/n.sc/o.sc/o.sc {0} /o.sc/o.sc/o.sc""".format(kernPair)

	# sc sc symmetry

	# sc lc
	elif subCat(myGlyphs[0], "Smallcaps") and subCat(myGlyphs[-1], "Lowercase") :
		return u"""/h.sc/o.osc/h.sc {0} non\n/h.sc/h.sc/h.sc {0} nnn\n/o.sc/o.sc/o.sc {0} ooo\n/x.sc/h.sc/x.sc {0} xox""".format(kernPair)

	# fallback
	else:
		return u"""HOH{0} non HOH{0} HOH non{0} npn\nHHH{0} nnn HHH{0} HHH nnn{0} nnn\nOOO{0} ooo OOO{0} OOO ooo{0} ooo\nXHX{0} xhx XHX{0} XHX xox{0} xox""".format(kernPair)