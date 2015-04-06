#MenuTitle: Convert Kerning Groups to Small Caps
# -*- coding: utf-8 -*-
__doc__="""
Convert kerning groups to small caps in current master. I.e. A > a.sc
"""

import vanilla
import GlyphsApp

Glyphs.clearLog()
Glyphs.font.disableUpdateInterface()

try:

	Font  = Glyphs.font
	selectedLayers = Font.selectedLayers
	currentLayers = [ l for l in selectedLayers if l.parent.name is not None ]

	for l in currentLayers:
		g = l.parent
		g.beginUndo()

		# Left Group:
		if g.leftKerningGroup != None:
			newLeftGroup = g.leftKerningGroup.lower() + ".sc"
			g.leftKerningGroup = newLeftGroup
			print "%s: new left group: '%s'" % ( g.name, newLeftGroup )
		else:
			print "\tNote: No left group set for %s. Left unchanged." % g.name

		# Right Group:
		if g.rightKerningGroup != None:
			newRightGroup = g.rightKerningGroup.lower() + ".sc"
			g.rightKerningGroup = newRightGroup
			print "%s: new right group: '%s'" % ( g.name, newRightGroup )
		else:
			print "\tNote: No right group set for %s. Left unchanged." % g.name

		g.endUndo()	

except Exception, e:
	raise e

Glyphs.font.enableUpdateInterface()