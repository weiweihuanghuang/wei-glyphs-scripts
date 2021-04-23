#MenuTitle: Show Glyphs Using This Glyph as Metrics Key
# -*- coding: utf-8 -*-
__doc__="""
"""

import GlyphsApp
import collections
thisFont = Glyphs.font 
selectedLayers = [l for l in thisFont.selectedLayers if l.parent.name != None]

stringOfGlyphs = ""

for l in selectedLayers:
	for g in thisFont.glyphs:
		thisGlyphsLayer = g.layers[thisFont.selectedFontMaster.id]
		if l.parent.name in [g.rightMetricsKey, g.leftMetricsKey, g.widthMetricsKey, thisGlyphsLayer.rightMetricsKey, thisGlyphsLayer.leftMetricsKey, thisGlyphsLayer.widthMetricsKey]:
			stringOfGlyphs += "/" + g.name

# print editString
Glyphs.font.newTab(stringOfGlyphs)