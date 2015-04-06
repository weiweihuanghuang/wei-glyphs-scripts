#MenuTitle: Show Each Metrics Type
# -*- coding: utf-8 -*-
__doc__="""
Show glyphs that have auto metrics, linked metrics key or are manually entered in selected glyphs in a new tab
"""
import vanilla
import GlyphsApp
from PyObjCTools.AppHelper import callAfter

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers

class ReportMetricKeys( object ):
	def __init__( self ):
		# Window 'self.w':
		left = 14
		top = 14
		leading = 36
		textW = 180
		textH = 20
		xSpace = 10
		buttonW = 100
		buttonTop = top-5
		buttonH = 30
		windowWidth  = left+textW+xSpace+buttonW+left
		windowHeight = top+leading+leading+leading
		self.w = vanilla.FloatingWindow(
			( windowWidth, windowHeight ), # default window size
			"Check & Fix Metric Keys", # window title
			autosaveName = "com.wwhh.MetricKeyChecker.mainwindow" # stores last window position and size
		)
		
		# UI elements:
		self.w.textManual = vanilla.TextBox( (left, top, textW, textH), "Manually set Metrics", sizeStyle='regular' )
		self.w.textAuto = vanilla.TextBox( (left, top+leading, textW, textH), "Automatic metrics", sizeStyle='regular' )
		self.w.textLinked = vanilla.TextBox( (left, top+leading+leading, textW, textH), "Linked metrics", sizeStyle='regular' )
		
		# Run Button:
		self.w.reportManual = vanilla.Button((left+textW+xSpace, buttonTop, buttonW, buttonH), "Report", sizeStyle='regular', callback=self.processMetrics )
		self.w.reportAuto = vanilla.Button((left+textW+xSpace, buttonTop+leading, buttonW, buttonH), "Report", sizeStyle='regular', callback=self.processMetrics )
		self.w.reportLinked = vanilla.Button((left+textW+xSpace, buttonTop+leading+leading, buttonW, buttonH), "Report", sizeStyle='regular', callback=self.processMetrics )
		
		# Open window and focus on it:
		self.w.open()
		self.w.makeKey()

	def processMetrics(self, sender):
		def processProcess( thisLayer ):
			thisLayerKey = (str(thisLayer.leftMetricsKeyUI()), str(thisLayer.rightMetricsKeyUI()))
			if sender == self.w.reportManual:
				# This layer does not have auto aligned width and no left and right layer or glyph metrics key
				if not thisLayer.hasAlignedWidth() and all(x is None for x in [thisLayer.leftMetricsKey(), thisGlyph.leftMetricsKey, thisLayer.rightMetricsKey(), thisGlyph.rightMetricsKey]):
					thisGlyphname = thisGlyph.name
			elif sender == self.w.reportAuto:
				# This layer has auto aligned width
				if thisLayer.hasAlignedWidth():
					thisGlyphname = thisGlyph.name
			elif sender == self.w.reportLinked:
				# This layer does not have auto aligned width and has either left or right layer or glyph metrics key
				if not thisLayer.hasAlignedWidth() and any(x is not None for x in [thisLayer.leftMetricsKey(), thisGlyph.leftMetricsKey, thisLayer.rightMetricsKey(), thisGlyph.rightMetricsKey]):
					thisGlyphname = thisGlyph.name
			print "%s\n %s" % (thisGlyphname, thisLayerKey)
			return thisGlyphname

		glyphList = ""

		# print "These glyphs have %s metrics\n" % metricsType
		for thisLayer in selectedLayers:
			thisGlyph = thisLayer.parent
			try:
				glyphList += "/" + processProcess( thisLayer )
			except:
				pass
		callAfter( Doc.windowController().addTabWithString_, glyphList )

ReportMetricKeys()