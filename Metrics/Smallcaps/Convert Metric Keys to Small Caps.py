#MenuTitle: Convert Metric Keys to Small Caps
# -*- coding: utf-8 -*-
__doc__="""
Convert metric keys to small caps in all masters. i.e. =A > =a.sc
"""

# Unfinished, can not deal with equations, or "=|" style metrics

import GlyphsApp

Glyphs.clearLog()
Glyphs.font.disableUpdateInterface()

import scCAPdict

Font  = Glyphs.font
selectedLayers = Font.selectedLayers

def keyMaker(keyGlyph):
	if keyGlyph[:2] == u"=|": # if metrics starts with "=|"
		return "=|%s" % scCAPdict.scCAPdictionary[keyGlyph[2:]]
	elif keyGlyph[0] == u"|": # if metrics starts with "|"
		return "|%s" % scCAPdict.scCAPdictionary[keyGlyph[1:]]
	elif keyGlyph[0] == "=": # if metrics starts with "="
		return scCAPdict.scCAPdictionary[keyGlyph[1:]]
	else:
		return scCAPdict.scCAPdictionary[keyGlyph]

for eachLayer in selectedLayers:
	thisGlyph = eachLayer.parent
	numberOfLayers = len( thisGlyph.layers )
	# For every master of the selected glyphs
	for i in range( numberOfLayers )[::-1]:
		thisLayer = thisGlyph.layers[i]
		if thisLayer.layerId == thisLayer.associatedMasterId:
			thisGlyph.beginUndo()
			# If this layer has a left metricKey
			if thisLayer.leftMetricsKey():
				thisLayer.setLeftMetricsKey_(keyMaker(thisLayer.leftMetricsKey()))
				print "%s %s has been set to %s" % (thisGlyph.name, thisLayer.name, str(thisLayer.leftMetricsKey()))
			# If this layer has a right metricKey
			if thisLayer.rightMetricsKey():
				thisLayer.setRightMetricsKey_(keyMaker(thisLayer.rightMetricsKey()))
				print "%s %s has been set to %s" % (thisGlyph.name, thisLayer.name, str(thisLayer.rightMetricsKey()))
			# If this glyph has a left metricKey
			if thisGlyph.leftMetricsKey and thisGlyph.leftMetricsKey[-3:] != ".sc":
				thisGlyph.setLeftMetricsKey_(keyMaker(thisGlyph.leftMetricsKey))
				print "%s has been set to %s" % (thisGlyph.name, str(thisGlyph.leftMetricsKey))
			# If this glyph has a right metricKey
			if thisGlyph.rightMetricsKey and thisGlyph.rightMetricsKey[-3:] != ".sc":
				thisGlyph.setRightMetricsKey_(keyMaker(thisGlyph.rightMetricsKey))
				print "%s has been set to %s" % (thisGlyph.name, str(thisGlyph.rightMetricsKey))
			thisGlyph.endUndo()	

Glyphs.font.enableUpdateInterface()