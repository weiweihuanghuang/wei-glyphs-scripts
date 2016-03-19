#MenuTitle: Show All Kerning Pairs With searchString
# -*- coding: utf-8 -*-
__doc__="""
Show All Kerning Pairs for this Master with searchString
"""
import GlyphsApp
import kernMakerFunc
reload(kernMakerFunc)
from kernMakerFunc import kernMaker

Glyphs.clearLog()
Font = Glyphs.font
Doc = Glyphs.currentDocument
selectedLayers = Font.selectedLayers
selectedMaster = Font.selectedFontMaster
masterID = selectedMaster.id

editString = ""
searchString = u"colon"
kerningCount = 0

def nameMaker(kernGlyph):
	if kernGlyph[0] == "@":
		return kernGlyph[7:]
	else:
		return Font.glyphForId_(kernGlyph).name	

for L in Font.kerning[ masterID ]:
	# print str(nameMaker(L))
	try:
		# if searchString is in L
		if str(nameMaker(L)) == searchString:
			for R in Font.kerning[masterID][L]:
				# print str(nameMaker(R))
				kernPair = "/%s/%s" % (nameMaker(L), nameMaker(R))
				editString += kernPair + "  " # kernMaker(kernPair)
				kerningCount += 1
		# if searchString is in R
		for R in Font.kerning[masterID][L]:
			if str(nameMaker(R)) == searchString:
				kernPair = "/%s/%s" % (nameMaker(L), nameMaker(R))
				editString += kernPair + "  " # kernMaker(kernPair)
				kerningCount += 1
	except:
		pass

Font.newTab(editString)
# print editString
print "%s kerning pairs found" % kerningCount