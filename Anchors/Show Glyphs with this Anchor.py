#MenuTitle: Show Glyphs with this Anchor
# -*- coding: utf-8 -*-
__doc__="""
New Tab with all Glyphs that have the selected anchor.
"""

thisFont = Glyphs.font # frontmost font
selectedLayer = thisFont.selectedLayers[0]
selection = selectedLayer.selection

editString = ""

for i, anchor in enumerate(selection):
	if i > 0:
		editString += "\n\n"
	if type(anchor) == GSAnchor:
		anchorName = anchor.name
		editString += "%s:\n" % anchorName # add anchor name to the text string
		for glyph in thisFont.glyphs:
			thisLayer = glyph.layers[selectedLayer.associatedMasterId]
			if anchorName in thisLayer.anchors.keys():
				editString += "/" + glyph.name

if len(editString) > 0:
	thisFont.newTab(editString) ### Open Tab with all Characters