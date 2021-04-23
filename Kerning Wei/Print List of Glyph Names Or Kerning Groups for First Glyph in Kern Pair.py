#MenuTitle: Print List of Glyph Names Or Kerning Groups for First Glyph in Kern Pair
# -*- coding: utf-8 -*-
__doc__="""
"""
import GlyphsApp

Font = Glyphs.font
Doc = Glyphs.currentDocument
selectedLayers = Font.selectedLayers

def uniquify(seq):
    seen = set()
    return [x for x in seq if x not in seen and not seen.add(x)]


list = []
for l in selectedLayers:
	g = l.parent

	if g.rightKerningGroup:
		list += [u"@MMK_L_{0}".format(g.rightKerningGroup)]
	else:
		list += [g.name]

f = open("firstGlyphList.py","w+")
fileText = u"firstGlyph = "
fileText += str(uniquify(list))
f.write(fileText)
f.close() 