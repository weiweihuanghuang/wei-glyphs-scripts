#MenuTitle: Show All Kerning Pairs With searchString in Context
# -*- coding: utf-8 -*-
__doc__="""
Show All Kerning Pairs for this Master with searchString in a new tab in context
"""
import GlyphsApp
from PyObjCTools.AppHelper import callAfter
from kernMakerFunc import kernMaker

Glyphs.clearLog()
Font = Glyphs.font
Doc = Glyphs.currentDocument
selectedLayers = Font.selectedLayers
selectedMaster = Font.selectedFontMaster
masterID = selectedMaster.id

editString = ""
searchString = u".sc"
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
		if str(nameMaker(L)).endswith(searchString):
			for R in Font.kerning[masterID][L]:
				# print str(nameMaker(R))
				kernPair = "/%s/%s" % (nameMaker(L), nameMaker(R))
				editString += kernMaker(kernPair)
				kerningCount += 1
		# if searchString is in R
		for R in Font.kerning[masterID][L]:
			if str(nameMaker(R)).endswith(searchString):
				kernPair = "/%s/%s" % (nameMaker(L), nameMaker(R))
				editString += kernMaker(kernPair)
				kerningCount += 1
	except:
		pass

callAfter( Doc.windowController().addTabWithString_, editString )
# print editString
print "%s kerning pairs found" % kerningCount