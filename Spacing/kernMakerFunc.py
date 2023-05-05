# -*- coding: utf-8 -*-
# The function that creates the kerning text, define your own texts

if __name__ != '__main__':
	from __main__ import *
import GlyphsApp

caseList = ["NoCase", "Uppercase", "Lowercase", "Smallcaps", "Minor", "OtherCase"]

def checkGlyphInfo(eachGlyph, glyphProperty, GlyphInfoValue):
	if glyphProperty == "category":
		if Glyphs.glyphInfoForName( eachGlyph ).category == GlyphInfoValue:
			return True
		else:
			return False
	if glyphProperty == "subCategory":
		if Glyphs.glyphInfoForName( eachGlyph ).subCategory == GlyphInfoValue:
			return True
		else:
			return False
	if glyphProperty == "case":
		if caseList[Glyphs.glyphInfoForName( eachGlyph ).case] == GlyphInfoValue:
			return True
		else:
			return False
	if glyphProperty == "script":
		if Glyphs.glyphInfoForName( eachGlyph ).script == GlyphInfoValue:
			return True
		else:
			return False

def kernMaker(kernPair, Option=""):

	myGlyphs = kernPair.split('/')

	# Split ligatures "_"
	myGlyphs = [g.split('_') for g in myGlyphs ]
	# Flatten lists within lists due to ligatures
	myGlyphs = [item for sublist in myGlyphs for item in sublist]
	# Remove blank items in myGlyphs
	myGlyphs = list(filter(None, myGlyphs))

	try:
		if Option == "Basic":
			return u"""non{0} nonnn{0} nnoo{0} ooo""".format(kernPair)

		elif Option == "BasicCaps":
			return u"""{0}   HH{0} HHOH""".format(kernPair)

		# superscript/subscript
		elif any(checkGlyphInfo(eachGlyph, "case", "Minor") for eachGlyph in myGlyphs):
			return u"""dd{0} bonn""".format(kernPair)

		# currency
		elif any(checkGlyphInfo(eachGlyph, "subCategory", "Currency") or checkGlyphInfo(eachGlyph, "subCategory", "Math") or eachGlyph in ["degree", "uni2300", "diameterSign", "uni2113", "literSign"] for eachGlyph in myGlyphs):

			numSuffix = ""
			periodPos = myGlyphs[0].find(".")
			if periodPos > 0:
				numSuffix = myGlyphs[0][periodPos:]

			return u"""/zero{1}/zero{1}{0}/zero{1}/zero{1}  {0}/six{1}/zero{1}  {0}/one{1}/zero{1}  {0}/seven{1}/zero{1}  {0}/two{1}/zero{1}  {0}/three{1}/zero{1}  {0}/eight{1}/zero{1}  {0}/nine{1}/zero{1}  {0}/five{1}/zero{1}  {0}/four{1}/zero{1}\n/zero{1}/nine{1}{0}  /zero{1}/one{1}{0}  /zero{1}/seven{1}{0}  /zero{1}/four{1}{0}  /zero{1}/two{1}{0}  /zero{1}/six{1}{0}  /zero{1}/five{1}{0}  /zero{1}/eight{1}{0}  /zero{1}/three{1}{0}  /zero{1}/eight{1}{0}/eight{1}/zero{1}""".format(kernPair, numSuffix) 

		# .case
		elif any(".case" in eachGlyph for eachGlyph in myGlyphs):
			return u"""HH{0} HOHOO{0} OO""".format(kernPair)

		# UC lc
		elif checkGlyphInfo(myGlyphs[0], "case", "Uppercase") and checkGlyphInfo(myGlyphs[-1], "case", "Lowercase") :
			return u"""{0} nonoo {0} nn {0} oo""".format(kernPair)

		# lc UC
		elif checkGlyphInfo(myGlyphs[0], "case", "Lowercase") and checkGlyphInfo(myGlyphs[-1], "case", "Uppercase"):
			return u"""nn{0} non""".format(kernPair)

		# UC sc
		elif checkGlyphInfo(myGlyphs[0], "case", "Uppercase") and checkGlyphInfo(myGlyphs[-1], "case", "Smallcaps"):
			suffix = ""
			periodPos = myGlyphs[1].find(".")
			if periodPos > 0:
				suffix = myGlyphs[1][periodPos:]
			return u"""{0}/h{1}/h{1}/o{1}/h{1}  {0}/o{1}/o{1}""".format(kernPair, suffix) 

		# sc sc symmetry

		# sc lc
		elif checkGlyphInfo(myGlyphs[0], "case", "Smallcaps") and checkGlyphInfo(myGlyphs[-1], "case", "Lowercase") :
			return u"""/h.sc/h.osc/h.sc {0} nnn\n/h.sc/o.sc/h.sc {0} non\n/o.sc/o.sc/o.sc {0} ooo\n/x.sc/h.sc/x.sc {0} xox""".format(kernPair)

		# number
		elif any(checkGlyphInfo(eachGlyph, "category", "Number") for eachGlyph in myGlyphs):
			numSuffix = ""

			numSuffix = ""
			periodPos = myGlyphs[0].find(".")
			if periodPos > 0:
				numSuffix = myGlyphs[0][periodPos:]

			return u"""/zero{1}/zero{1}{0} /zero{1}/zero{1}  /one{1}/one{1}{0} /one{1}/one{1}  /two{1}/two{1}{0} /two{1}/two{1}  /three{1}/three{1}{0} /three{1}/three{1}  /four{1}/four{1}{0} /four{1}/four{1}  /five{1}/five{1}{0} /five{1}/five{1}  /six{1}/six{1}{0} /six{1}/six{1}  /seven{1}/seven{1}{0} /seven{1}/seven{1}  /eight{1}/eight{1}{0} /eight{1}/eight{1}  /nine{1}/nine{1}{0} /nine{1}/nine{1}""".format(kernPair, numSuffix)

		# fallback
		else:
			suffix = ""
			periodPos = myGlyphs[0].find(".")
			if periodPos > 0:
				suffix = myGlyphs[0][periodPos:]

			# UC 
			if any(checkGlyphInfo(eachGlyph, "case", "Uppercase") for eachGlyph in myGlyphs):
				# UC quote UC
				if any(checkGlyphInfo(eachGlyph, "subCategory", "Quote") for eachGlyph in myGlyphs):
					nonQuoteGlyph = ""
					for eachGlyph in myGlyphs:
						if not checkGlyphInfo(eachGlyph, "subCategory", "Quote"):
							nonQuoteGlyph = eachGlyph
					return u"""/H/H/{0}/comma/H/H/quotedblleft/{0}/quotedblright/H/H/quotedblright/{0}/quotedblright/H/H/space/space/quotedblbase/{0}/quotedblright/H/H/space/space/quotedblbase/{0}/quotedblleft/H/H/quotedbl/{0}/quotedbl/H/H\n/H/H/guillemetleft/{0}/guillemetright/H/O/H/guillemetright/{0}/guillemetleft/H/H""".format(nonQuoteGlyph)
				else:
					return u"""HH{0} HHOH{0} OO{0} OO""".format(kernPair, suffix)

			# lc
			elif any(checkGlyphInfo(eachGlyph, "case", "Lowercase") for eachGlyph in myGlyphs):
				# quote lc quote
				if any(checkGlyphInfo(eachGlyph, "subCategory", "Quote") for eachGlyph in myGlyphs):
					nonQuoteGlyph = ""
					for eachGlyph in myGlyphs:
						if not checkGlyphInfo(eachGlyph, "subCategory", "Quote"):
							nonQuoteGlyph = eachGlyph
					return u"""/n/u/{0}/comma/space/n/u/quotedblleft/{0}/quotedblright/n/u/quotedblright/{0}/quotedblright/n/u/space/quotedblbase/{0}/quotedblright/n/u/space/quotedblbase/{0}/quotedblleft/n/u/quotedbl/{0}/quotedbl/n/u\n/n/u/guillemetleft/{0}/guillemetright/n/o/u/guillemetright/{0}/guillemetleft/n/u""".format(nonQuoteGlyph) 

				else:
					return u"""uu{0} nnon{0} oo{0} oo""".format(kernPair)
			# sc sc
			elif any(checkGlyphInfo(eachGlyph, "case", "Smallcaps") for eachGlyph in myGlyphs):
				return u"""/h{1}/h{1}{0}/h{1}/h{1}/o{1}/h{1}{0}/o{1}/o{1}{0}/o{1}/o{1}""".format(kernPair, suffix)

			else:
				return u"""HH{0} HHOH{0} OO{0} OO uu{0} nnon{0} oo{0} oo""".format(kernPair)

	except:
		import traceback
		print(traceback.format_exc())
		return u"""HH{0} HHOH{0} OO{0} OO uu{0} nnon{0} oo{0} oo""".format(kernPair)
