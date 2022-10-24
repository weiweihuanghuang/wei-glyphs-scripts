from __future__ import print_function
#MenuTitle: Compare Fonts 2
# -*- coding: utf-8 -*-
__doc__="""
- Compare 2 open files and opens a new tab (in the current font) for each master showing the glyphs that are different between the 2 files.

- A decomposed copy of each different glyph from the other file will also be pasted in the background of each glyph in the current file. 

*** WARNING *** This will clear the background in the current font. Change "copyToBackground" to 0

"""

import GlyphsApp
# from objectsGS import RFont
# from robofab.pens.digestPen import DigestPointPen

copyToBackground = 0
ignoreAlignedComponents = 1
closeAllTabs = 1

# Figure out which font is Glyphs.font and set thisFont as the file that is open
# if Glyphs.font.filepath == Glyphs.fonts[1].filepath:
    # thisFont = Glyphs.fonts[1]
    # otherFont = Glyphs.fonts[0]
# else:
    # thisFont = Glyphs.fonts[0]
    # otherFont = Glyphs.fonts[1]

thisFont = Glyphs.fonts[0]
otherFont = Glyphs.fonts[1]

if closeAllTabs == 1:
    # close all tabs
    for i in range(len(thisFont.tabs)):
        del thisFont.tabs[0]
    for i in range(len(otherFont.tabs)):
        del otherFont.tabs[0]

def copyPathsAndAnchorsFromLayerToLayer( sourceLayer, targetLayer ):
    # Copy Paths
    numberOfPathsInSource  = len( sourceLayer.paths )

    if numberOfPathsInSource > 0:
        for thisPath in sourceLayer.paths:
            newPath = thisPath.copy()
            targetLayer.paths.append( newPath )

    # Copy Anchors
    numberOfAnchorsInSource = len( sourceLayer.anchors )

    if numberOfAnchorsInSource > 0:
        for thisAnchor in sourceLayer.anchors:
            newAnchor = thisAnchor.copy()
            targetLayer.anchors.append( newAnchor )
            # print "   %s (%i, %i)" % ( thisAnchor.name, thisAnchor.position.x, thisAnchor.position.y )

thisFont_glyphset = set([g.name for g in thisFont.glyphs])
otherFont_glyphset = set([g.name for g in otherFont.glyphs])

commonGlyphs = list(thisFont_glyphset.intersection(otherFont_glyphset))
# print(commonGlyphs)

# check first font first master
glyphsToCheck = []
for g in commonGlyphs:
    if ignoreAlignedComponents == 1:
        # Check and filter out any automatic aligned glyphs
        notAutomaticAlignedComponentsGlyphList = []
        # automaticAlignedComponentsGlyphList = []
        componentGlyphList = []
        pathGlyphList = []

        for g in commonGlyphs:
            thisLayer = thisFont.glyphs[g].layers[thisFont.masters[0].id]
            # otherLayer = otherFont.glyphs[g].layers[otherFontMasterID]

            if len(thisLayer.components) > 0:
                componentGlyphList += [str(g)]
                for c in thisLayer.components:
                    if not c.automaticAlignment:
                        notAutomaticAlignedComponentsGlyphList += [str(g)]
                        break
            else:
                pathGlyphList += [str(g)]

        # automaticAlignedComponentsGlyphList = [glyph for glyph in componentGlyphList if glyph not in notAutomaticAlignedComponentsGlyphList]
        glyphsToCheck = pathGlyphList + notAutomaticAlignedComponentsGlyphList
    else:
        glyphsToCheck = commonGlyphs

for thisMasterIndex in range( len(thisFont.masters) ):

    # fonts = AllFonts()
    # thisFont = RFont(Glyphs.fonts[0])
    # otherFont = RFont(Glyphs.fonts[1])

    # thisFont = RFont(Glyphs.documents[0].font, thisMasterIndex)
    # otherFont = RFont(Glyphs.documents[1].font, thisMasterIndex)

    notSameGlyphsList = []
    sameGlyphsList = []
    blankGlyphsList = []
    blankGlyphsString = ""
    notSameGlyphsString = ""
    sameGlyphsString = ""
    # glyphsToCheck = []

    # Get correct IDs
    thisFontMasterID = thisFont.masters[thisMasterIndex].id
    otherFontMasterID = otherFont.masters[thisMasterIndex].id

    # # check first font every master
    # for g in commonGlyphs:
    #     if ignoreAlignedComponents == 1:
    #         # Check and filter out any automatic aligned glyphs
    #         notAutomaticAlignedComponentsGlyphList = []
    #         automaticAlignedComponentsGlyphList = []
    #         componentGlyphList = []
    #         pathGlyphList = []

    #         for g in commonGlyphs:
    #             thisLayer = thisFont.glyphs[g].layers[thisFontMasterID]
    #             # otherLayer = otherFont.glyphs[g].layers[otherFontMasterID]

    #             if len(thisLayer.components) > 0:
    #                 componentGlyphList += [str(g)]
    #                 for c in thisLayer.components:
    #                     if not c.automaticAlignment:
    #                         notAutomaticAlignedComponentsGlyphList += [str(g)]
    #                         break
    #             else:
    #                 pathGlyphList += [str(g)]

    #         automaticAlignedComponentsGlyphList = [glyph for glyph in componentGlyphList if glyph not in notAutomaticAlignedComponentsGlyphList]
    #         glyphsToCheck = pathGlyphList + notAutomaticAlignedComponentsGlyphList
    #     else:
    #         glyphsToCheck = commonGlyphs

    for g in glyphsToCheck:
        l1 = thisFont.glyphs[g].layers[thisFontMasterID]
        l2 = otherFont.glyphs[g].layers[otherFontMasterID]

        # # check structure
        # d1 = g1.layers[thisFont.masters[thisMasterIndex].id].compareString()
        # d2 = g2.layers[otherFont.masters[thisMasterIndex].id].compareString()

        # check paths
        p1 = [(node.position, node.type) for paths in l1.paths for node in paths.nodes] 
        p2 = [(node.position, node.type) for paths in l2.paths for node in paths.nodes] 

        if p1 != p2:
            notSameGlyphsList += [str(g)]
            pass

        # check components
        c1 = [(component.position, component.componentName) for component in l1.components] 
        c2 = [(component.position, component.componentName) for component in l2.components] 

        if c1 != c2:
            notSameGlyphsList += [str(g)]
            pass

        # check anchors
        a1 = [anchor.position for anchor in l1.anchors] 
        a2 = [anchor.position for anchor in l2.anchors] 

        if a1 != a2:
            notSameGlyphsList += [str(g)]
            pass

        if l1.width != l2.width:
            notSameGlyphsList += [str(g)]

        else:
            sameGlyphsList += [str(g)]

    # Sort the lists
    notSameGlyphsListSorted = [g.name for g in thisFont.glyphs if g.name in notSameGlyphsList]

    blankGlyphsString = '/{0}'.format('/'.join(blankGlyphsList))
    notSameGlyphsString = '/{0}'.format('/'.join(notSameGlyphsListSorted))
    sameGlyphsString = '/{0}'.format('/'.join(sameGlyphsList))

    print("\n%s" % Glyphs.fonts[0].masters[thisMasterIndex].name)
    print("\tDifferent Glyphs\n%s" % notSameGlyphsString)
    print("\n\tDifference is that one file is blank Glyphs\n%s" % blankGlyphsString)
    ## print "\n\tSame Glyphs\n%s" % sameGlyphsString

    if copyToBackground == 1:

        # Add glyphs to background

        for thisGlyphName in notSameGlyphsListSorted:
            # if thisGlyphName not in blankGlyphsList:

            # Get the current layer for the current glyph
            thisLayerInThisFont = thisFont.glyphs[thisGlyphName].layerForKey_(thisFontMasterID)
            thisLayerInOtherFont = otherFont.glyphs[thisGlyphName].layerForKey_(otherFontMasterID)
            thisGlyphInThisFontLayerBackground = thisLayerInThisFont.background
            sourceLayer = otherFont.glyphs[thisGlyphName].layerForKey_(otherFontMasterID).copyDecomposedLayer()

            # Clear the background and copy the paths, components and anchors
            thisLayerInThisFont.background.clear()
            copyPathsAndAnchorsFromLayerToLayer(sourceLayer, thisGlyphInThisFontLayerBackground)

    # Open new tabs with different glphs
    if notSameGlyphsListSorted != []:

        thisFont.newTab(notSameGlyphsString)
        # Change to the correct master
        thisFont.currentTab.setMasterIndex_(thisMasterIndex)

        otherFont.newTab(notSameGlyphsString)
        # Change to the correct master
        otherFont.currentTab.setMasterIndex_(thisMasterIndex)