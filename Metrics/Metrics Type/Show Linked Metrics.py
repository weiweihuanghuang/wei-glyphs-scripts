#MenuTitle: Show Linked Metrics
# -*- coding: utf-8 -*-
__doc__="""
Shows glyphs that have a linked metrics key in selected glyphs in a new tab.
"""
import GlyphsApp
from PyObjCTools.AppHelper import callAfter

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers
glyphList = ""

glyphList = ""

print "These glyphs have manual metrics\n"
for thisLayer in selectedLayers:
	thisGlyph = thisLayer.parent
	try:
		thisLayerKey = (str(thisLayer.leftMetricsKeyUI()), str(thisLayer.rightMetricsKeyUI()))
		if not thisLayer.hasAlignedWidth() and any(x is not None for x in [thisLayer.leftMetricsKey(), thisGlyph.leftMetricsKey, thisLayer.rightMetricsKey(), thisGlyph.rightMetricsKey]):
			glyphList += "/" + thisGlyph.name
		print "%s\n %s" % (thisGlyphname, thisLayerKey)		
	except:
		pass

# print "\n %s" % glyphList
callAfter( Doc.windowController().addTabWithString_, glyphList )