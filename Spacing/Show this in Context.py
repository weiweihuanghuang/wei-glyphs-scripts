#MenuTitle: Show this in Context (New Tab)
# -*- coding: utf-8 -*-
__doc__="""
Show selected text in spacing context in a new tab.
"""
import GlyphsApp
import kernMakerFunc
import importlib
importlib.reload(kernMakerFunc)
from kernMakerFunc import kernMaker

Font = Glyphs.font
Doc = Glyphs.currentDocument
selectedLayers = Font.selectedLayers
namesOfSelectedGlyphs = [ "/%s" % l.parent.name for l in selectedLayers if hasattr(l.parent, 'name') ]

editString = "".join(namesOfSelectedGlyphs)

Glyphs.font.newTab( kernMaker(editString) )