#MenuTitle: Delete Kerning Pairs Between these Categories for All Masters
# -*- coding: utf-8 -*-
__doc__="""
"""
import GlyphsApp

Font = Glyphs.font
Doc = Glyphs.currentDocument
selectedLayers = Font.selectedLayers
selectedMaster = Font.selectedFontMaster

import firstGlyphList, secondGlyphList
reload(firstGlyphList)
reload(secondGlyphList)
from firstGlyphList import firstGlyph
from secondGlyphList import secondGlyph

pairsToBeDeleted = []

for l in firstGlyph:
	for r in secondGlyph:
		pairsToBeDeleted += [(l, r)] 

Font.disableUpdateInterface()

totalNumberOfDeletions = 0

for m in Font.masters:
	print "\t{0}".format(m.name)
	# uniquify so that it doesn't try to delete the same kerning pair again
	for thisDeletionGroup in pairsToBeDeleted:
		firstGlyphName = thisDeletionGroup[0]
		secondGlyphName = thisDeletionGroup[1]

		try:
			Font.removeKerningForPair( m.id, firstGlyphName, secondGlyphName )
			totalNumberOfDeletions += 1
			print "Deleting pair: %s %s ..." % ( firstGlyphName, secondGlyphName )
		except Exception, e:
			print "-- Error: could not delete pair %s %s (%s)" % ( firstGlyphName, secondGlyphName, e )

	print "Done: %i pairs deleted in %s." % ( totalNumberOfDeletions, selectedMaster.name )

Font.enableUpdateInterface()