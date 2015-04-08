Glyphs Scripts
==============

###About
---
Some scripts for [Glyphs font editor](http://glyphsapp.com/) – tested with V2 beta only.

Put the scripts into the Scripts folder which appears when you choose Open Scripts Folder from the Scripts menu.

For some scripts, you will also need to install Tal Leming's Vanilla. Here's how.

In Glyphs 2.0 or later, go to Glyphs > Preferences > Addons > Scripts and click the Install Modules button. You are done and can skip the rest of these installation instructions.

###About the Scripts
---
- **Uppercase** – Converts the selected text in a tab to uppercase.
- **Lowercase** – Converts the selected text in a tab to lowercase.
- **Zoom Wide** – Zooms the viewport to 50pts.


####Metrics

- **Adjust Kerning in Glyph** – Adjusts kerning values for a specified glyph by a specified amount *(edit the script manually to select glyph and adjustment amount)*.
- **Delete Kerning Pairs In Text** – Deletes all selected kerning pairs present in selected text
- **Delete Kerning Pairs Smaller Than Popup** – Delete all kerning pairs equal to or smaller than # in selected master
- **Show All Kerning Pairs With** – Show All Kerning Pairs for this Master with searchString in a new tab in context *(edit the script manually to select glyph)*.
- **Show All Kerning Pairs**
- **Show Glyphs in Kerning Groups** – Show all glyphs in the kerning groups of the selected glyph in a new tab.
- **Show Kerning Pairs** – Show Kerning Pairs for this glyph in a new tab.
- **Show Kerning Pairs Context** – Show Kerning Pairs in context for the selected glyphs in a new tab.
- **Show this in Context** – Show selected text in spacing context in a new tab.
- **Show these in Context-Space** – Show selected items, each separated by /space, in spacing context in a new tab. i.e. selecting "av aw af fe" and running this script will put each pair in kerning context
- **Sync All Metrics in All Masters**
- **Unlink Metrics**
- **kernMakerFunc.py** - The script that defines the context pattern (HOHnon etc) for kerning pairs for many of the above scripts.

Metrics Type:

- **Show All Linked Metrics Type** – Report the linked metrics type for each glyph in every master in the macro window
- **Show All Metrics Type** – Report the metrics type for each glyph in every master in the macro window
- **Show Each Metrics Type** – Show glyphs that have auto metrics, linked metrics key or are manually entered in selected glyphs in a new tab
- **Show Linked Metrics**
- **Show Manual Metrics**
- **Show Non Automatic Alignment**

Smallcaps:

- **Convert Kerning Groups to Small Caps** – Converts kerning groups to smallcaps. I.e. A > a.sc
- **Convert Metric Keys to Small Caps** – Converts metrics key glyphs to smallcaps in all masters. I.e. =A > =a.sc
- **scCAPdict.py** - The dictionary that defines the small caps for 'Convert Metric Keys to Small Caps' – there's a better way to do this but this is how I do it at least now.

####Masters:

- **Clear Every Master Layer** – Clears every master layer and places content in background.
- **Copy Layer to All Layers** – Copies one master to every master layer in selected glyphs.
- **Find and Delete Layers** – Find layers with the search string and deletes them.
- **Find In Layer Names** – Find layers with the search string in them and creates a new tab with the glyphs (haven't yet figured out how to show the correct layer). Useful for finding [bracket layers](http://www.glyphsapp.com/tutorials/alternating-glyph-shapes).

Thanks to [Georg Seifert](https://github.com/schriftgestalt) and [Rainer Erich Scheichelbauer](https://github.com/mekkablue/) for their help and for providing a great API and example scripts.

###AppleScripts
---
These are AppleScripts that do exactly as they say. Assign them to a keyboard shortcut through Automator as a Service or with Fascripts (this is what I use, Automator seems to repeat the action if they keys are pressed a tiny bit too long), Quicksilver, etc.

- Redo 10 times
- Undo 10 times

(These scripts could be used in any appliction actually)
