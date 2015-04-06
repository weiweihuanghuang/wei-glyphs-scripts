#MenuTitle: Show this in Context
# -*- coding: utf-8 -*-
__doc__="""
Show selected text in spacing context in a new tab.
"""
import GlyphsApp
from PyObjCTools.AppHelper import callAfter
from kernMakerFunc import kernMaker

Font = Glyphs.font
Doc = Glyphs.currentDocument
selectedLayers = Font.selectedLayers
namesOfSelectedGlyphs = [ "/%s" % l.parent.name for l in selectedLayers ]

editString = "".join(namesOfSelectedGlyphs)

callAfter( Doc.windowController().addTabWithString_, kernMaker(editString) )