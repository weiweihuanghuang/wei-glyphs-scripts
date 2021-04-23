#MenuTitle: Get Random Featured Article of the Day
# -*- coding: utf-8 -*-
__doc__="""
Gets the first paragraph of a random Featured Wikipedia Article of the Day from English Wikipedia
"""
import GlyphsApp
import html2text
import feedparser
from random import randint

d = feedparser.parse("https://en.wikipedia.org/w/api.php?action=featuredfeed&feed=featured&feedformat=atom")

# Get random featured article
html = d['entries'][randint(0,len(d['entries'])-1)]['summary_detail']['value']

# Remove the header image and caption
htmlStart = html.find("<p>")
html = html[htmlStart:]

h = html2text.HTML2Text()
h.ignore_links = True
h.ignore_images = True
h.ignore_emphasis = True
h.body_width = 0
plaintext = h.handle(html)

# Remove the "(Full article...)" text
plaintextEnd = plaintext.find(u"""(Full""")
plaintext = plaintext[:plaintextEnd]

# Fix slashes
plaintext = plaintext.replace("/", "//")

Glyphs.font.newTab(plaintext)