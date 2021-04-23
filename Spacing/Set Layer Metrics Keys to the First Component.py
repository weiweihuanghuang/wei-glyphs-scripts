#MenuTitle: Set Layer Metrics Keys to the First Component
# -*- coding: utf-8 -*-
__doc__="""
"""

import GlyphsApp

Glyphs.clearLog() # clears macro window log
thisFont = Glyphs.font # frontmost font
thisFontMaster = thisFont.selectedFontMaster # active master
listOfSelectedLayers = [ l for l in thisFont.selectedLayers if hasattr(l.parent, 'name')]
 # active layers of selected glyphs

def process( thisLayer ):
	if len(thisLayer.components)>=1 and len(thisLayer.paths)==0:
		baseComponentGlyph = thisLayer.components[0].name
		thisLayer.leftMetricsKey = baseComponentGlyph
		thisLayer.rightMetricsKey = baseComponentGlyph
		return baseComponentGlyph

thisFont.disableUpdateInterface() # suppresses UI updates in Font View

for thisLayer in listOfSelectedLayers:
	print "Setting metrics keys: %s to" % thisLayer.parent.name,
	# thisLayer.beginUndo() # begin undo grouping
	print process( thisLayer )
	# thisLayer.endUndo()   # end undo grouping

thisFont.enableUpdateInterface() # re-enables UI updates in Font View
