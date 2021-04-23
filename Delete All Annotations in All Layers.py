#MenuTitle: Delete All Annotatoins in All Layers
# -*- coding: utf-8 -*-
__doc__="""
"""

Font = Glyphs.font

def process( thisLayer ):
	thisLayer.annotations =[]
	thisLayer.background.annotations = []

for eachGlyph in Font.glyphs:
	for thisLayer in eachGlyph.layers:
		process(thisLayer)