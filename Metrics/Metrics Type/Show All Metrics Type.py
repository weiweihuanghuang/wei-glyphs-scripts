#MenuTitle: Report All Metrics Type
# -*- coding: utf-8 -*-
__doc__="""
Report the metrics type for each glyph in every master in the macro window
"""
import vanilla
import GlyphsApp

Glyphs.clearLog()

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers

# # For only thismaster
# for thisLayer in selectedLayers:
	# thisGlyph = thisLayer.parent

# For every master
for eachLayer in selectedLayers:
	thisGlyph = eachLayer.parent
	numberOfLayers = len( thisGlyph.layers )
	print thisGlyph.name
	for i in range( numberOfLayers )[::-1]:
		thisLayer = thisGlyph.layers[i]
		if thisLayer.layerId == thisLayer.associatedMasterId:
			masterName = thisLayer.name
			thisLayerleftMetricsKey = thisLayer.leftMetricsKey()
			thisLayerrightMetricsKey = thisLayer.rightMetricsKey()
			thisGlyphleftMetricsKey = thisGlyph.leftMetricsKey 
			thisGlyphrightMetricsKey = thisGlyph.rightMetricsKey
			metricsKeyUI = u"[%s, %s]" % (thisLayer.leftMetricsKeyUI(), thisLayer.rightMetricsKeyUI())
			# This layer does not have auto aligned width and no left and right layer or glyph metrics key
			if not thisLayer.hasAlignedWidth() and all(x is None for x in [thisLayerleftMetricsKey, thisGlyphleftMetricsKey, thisLayerrightMetricsKey, thisGlyphrightMetricsKey]):
				print "  %s\n\tManual: %s" % (masterName, metricsKeyUI)
			# This layer has auto aligned width
			elif thisLayer.hasAlignedWidth():
				print "  %s\n\tAuto  : %s" % (masterName, metricsKeyUI)

			# This layer does not have auto aligned width and has either left or right layer metrics key
			if any(x is not None for x in [thisLayerleftMetricsKey, thisLayerrightMetricsKey]):
				print "  %s\n\tLayer : %s" % (masterName, metricsKeyUI)

			# This layer does not have auto aligned width and has either left or right glyph metrics key
			elif any(x is not None for x in [thisGlyphleftMetricsKey, thisGlyphrightMetricsKey]):
				print "  %s\n\tGlyph : %s" % (masterName, metricsKeyUI)