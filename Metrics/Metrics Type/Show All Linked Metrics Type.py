#MenuTitle: Report All Linked Metrics Type
# -*- coding: utf-8 -*-
__doc__="""
Report the linked metrics type for each glyph in every master in the macro window
"""
import vanilla
import GlyphsApp

Glyphs.clearLog()

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers

namePrinted = False

# # For only thismaster
# for thisLayer in selectedLayers:
	# thisGlyph = thisLayer.parent

# For every master
for eachLayer in selectedLayers:
	thisGlyph = eachLayer.parent
	numberOfLayers = len( thisGlyph.layers )
	for i in range( numberOfLayers )[::-1]:
		thisLayer = thisGlyph.layers[i]
		if thisLayer.layerId == thisLayer.associatedMasterId:
			masterName = thisLayer.name
			thisLayerleftMetricsKey = thisLayer.leftMetricsKey()
			thisLayerrightMetricsKey = thisLayer.rightMetricsKey()
			thisGlyphleftMetricsKey = thisGlyph.leftMetricsKey
			thisGlyphrightMetricsKey = thisGlyph.rightMetricsKey

			if any(x is not None for x in [thisLayerleftMetricsKey, thisLayerrightMetricsKey, thisGlyphleftMetricsKey, thisGlyphrightMetricsKey]):
				if namePrinted == False:
					print thisGlyph.name
					namePrinted = True
				print "  %s\n\tLayer: %s %s\n\tGlyph: %s %s" % (masterName, thisLayerleftMetricsKey, thisLayerrightMetricsKey, thisGlyphleftMetricsKey, thisGlyphrightMetricsKey)
	namePrinted = False