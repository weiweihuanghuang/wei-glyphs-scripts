#MenuTitle: Unlink Metrics
# -*- coding: utf-8 -*-
__doc__="""
Unlinks metrics key glyph and expands the metrics number
"""

import GlyphsApp

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers

glyphList = ""

for thisLayer in selectedLayers:
	thisGlyph = thisLayer.parent
	thisGlyph.setLeftMetricsKey_(None)
	thisGlyph.setRightMetricsKey_(None)
	# print thisLayer.leftMetricsKeyUI(), thisLayer.leftMetricsKey()
	# thisLayerKey = (str(thisLayer.leftMetricsKeyUI()), str(thisLayer.rightMetricsKeyUI()))
	# if not thisLayer.hasAlignedWidth() and all(x is None for x in [thisLayer.leftMetricsKey(), thisGlyph.leftMetricsKey, thisLayer.rightMetricsKey(), thisGlyph.rightMetricsKey]):
		# glyphList += "/" + thisGlyph.name
	# print "%s\n %s" % (thisGlyphname, thisLayerKey)		