#MenuTitle: Get All Components in Selected Glyphs
# -*- coding: utf-8 -*-
"""Returns the selected text with all components available in each glyph"""

from AppKit import NSRange

Font = Glyphs.font
Doc = Glyphs.currentDocument

# Replace selected text
TextStorage = Font.currentTab.graphicView().textStorage()
Range = Doc.windowController().activeEditViewController().graphicView().selectedRange()

editList = []

for l in Font.selectedLayers:
	# editList += ["/%s" % l.parent.name]
	if len(l.components)>0:
		for c in l.components:
			editList += ["/%s" % c.componentName]

# Remove duplicates
def f7(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]

editList = f7(editList)

# Sort editList according to file order
editList = ["/%s" % g.name for g in Font.glyphs if "/%s" % g.name in editList]

editString = "".join(editList)
editString = "\n" + editString

# Convert text string into character string
charString = Font.charStringFromDisplayString_(editString)
TextStorageString = Font.currentTab.graphicView().textStorage().text().string()
finalTextString = TextStorageString + charString

TextStorage.replaceCharactersInRange_withString_(Range, finalTextString)

# Set cursor at start of TextStorage
Font.currentTab.textRange = 0
Font.currentTab.textCursor = 0