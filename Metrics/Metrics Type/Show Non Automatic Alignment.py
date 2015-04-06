#MenuTitle: Show Non Automatic Alignment 
# -*- coding: utf-8 -*-
__doc__="""
Shows which glyphs do not have automatic alignment on components in selected glyphs in a new tab.
"""
import GlyphsApp
from PyObjCTools.AppHelper import callAfter

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers
glyphList = ""

def process( thisLayer ):
	disabledComps = ""
	thisGlyph = thisLayer.parent

	if thisLayer.components:
		for thisComp in thisLayer.components:
			if thisComp.disableAlignment:
				disabledComps += str(thisComp.componentName) + " "
	if disabledComps:
		print "%s:\n\t%s\n" % (thisGlyph.name, disabledComps)
		return thisGlyph.name

print "These glyphs have components not automatically aligned\n"
for thisLayer in selectedLayers:
	thisGlyph = thisLayer.parent
	try:
		glyphList += "/" + process( thisLayer )
	except:
		pass

# print glyphList
callAfter( Doc.windowController().addTabWithString_, glyphList )