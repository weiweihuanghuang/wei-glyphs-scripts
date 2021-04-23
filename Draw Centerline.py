#MenuTitle: Draw Centreline
# -*- coding: utf-8 -*-
__doc__="""
Draw centre line
"""

import GlyphsApp
# Glyphs.clearLog()

Font = Glyphs.font
FontMaster = Font.selectedFontMaster
selectedLayers = Font.selectedLayers

def drawPath( myCoordinates ):
	try:
		myRect = GSPath()

		for thisPoint in myCoordinates:
			newNode = GSNode()
			newNode.type = thisPoint[1]
			newNode.connection = thisPoint[2]
			newNode.position = ( thisPoint[0][0], thisPoint[0][1] )
			myRect.nodes.append( newNode )

		# myRect.closed = True
		return myRect

	except Exception as e:
		return False

def process( thisLayer ):
	myPaths = []
	
	# selection = thisLayer.selection()
	# if selection == None:
	# 	selection = thisLayer.paths

	# dump each path as a list
	for path in thisLayer.paths:
		# new path
		thisPath = []
		for node in path.nodes: 
			thisPath += [ [ (node.position.x, node.position.y), node.type, node.connection ] ]
		# re-arrange list to put last item first (GA returns list this way, not sure why)
		thisPath.insert(0, thisPath.pop())
		# appen path to myPaths
		myPaths += [thisPath]

	for eachPath in myPaths:
		counter = len(eachPath)
		myNewCoordinates = []
		for i, coordinate in enumerate(eachPath):
			# only do this for half the number of points
			if counter > len(eachPath)/2:
				# average each pair point
				myNewCoordinates += [ [ ( (coordinate[0][0]+eachPath[(-1-i)][0][0])/2, (coordinate[0][1]+eachPath[(-1-i)][0][1])/2 ), coordinate[1], coordinate[2] ] ]
				counter -= 1

		layerCentrePath = drawPath(myNewCoordinates)
		thisLayer.paths.append( layerCentrePath )

Font.disableUpdateInterface()

for thisLayer in selectedLayers:
	thisGlyph = thisLayer.parent
	thisGlyph.beginUndo()
	print "Drawing centreline for %s: %s." % ( thisGlyph.name, process( thisLayer ) )
	thisGlyph.endUndo()

Font.enableUpdateInterface()