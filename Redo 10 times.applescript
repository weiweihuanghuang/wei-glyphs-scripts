tell application "System Events"
	set activeApp to name of first process whose frontmost is true
end tell

tell application "System Events"
	repeat 11 times
		tell process activeApp to click (first menu item of menu "Edit" of menu bar 1 whose title starts with "Redo")
	end repeat
end tell