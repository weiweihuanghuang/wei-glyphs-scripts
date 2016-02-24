#MenuTitle: Set Transform Origin to Centre of Selection
# -*- coding: utf-8 -*-
__doc__="""
Sets origin point for Rotate tool to the centre of the selection.
"""
import GlyphsApp

Font = Glyphs.font
selectedLayer = Font.selectedLayers[0]

if len(selectedLayer.selection) > 0:
	selection = selectedLayer.selectionBounds
else:
	selection = selectedLayer.bounds

newOriginX = selection.origin.x + selection.size.width / 2
newOriginY = selection.origin.y + selection.size.height / 2

Glyphs.defaults["GSTransformOriginX"] = newOriginX
Glyphs.defaults["GSTransformOriginY"] = newOriginY

Glyphs.redraw()

# print newOriginPoint
# print selection.origin.x, selection.origin.y, selection.size.width/2, selection.size.height/2

# except Exception, e:
# 	# brings macro window to front and reports error:
# 	Glyphs.showMacroWindow()
# 	print "Set Transform Origin Error: %s" % e