#MenuTitle: Print List of Glyph Names Or Kerning Groups for Second Glyph in Kern Pair
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

	if g.leftKerningGroup:
		list += [u"@MMK_R_{0}".format(g.leftKerningGroup)]
	else:
		list += [g.name]

f = open("secondGlyphList.py","w+")
fileText = u"secondGlyph = "
fileText += str(uniquify(list))
f.write(fileText)
f.close() 