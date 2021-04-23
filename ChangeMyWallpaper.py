#!/usr/bin/env python3
import random, os, ctypes # These will be helpful modules to have!

Root = "C:\\Users\\Kenny\\Pictures\\" # This is the root of the path...

Theme_list = {
	"Chess" : Root + "Chess",
	"Philosophy" : Root + "Philosophy",
	"Music" : Root + "Music",
	"Math" : Root + "Math"
}


Valid_theme_chosen = False

while Valid_theme_chosen is False:
	Elected_theme = random.choice(list(Theme_list.items())) # 'Randomly' pick a theme from the collection...
	Path_to_folder = Elected_theme[1] # This new assignment isn't too necessary, but it improves readability
	# which I feel is an important idea to keep in mind - I want strangers or anybody to easily read and understand
	# what's going on... what's happening...
	print(Path_to_folder)
	if len(os.listdir(Path_to_folder)) == 0:
		continue
	else:
		Contents_list = os.listdir(Path_to_folder)
		for item in Contents_list:
			if not item.endswith((".jpg", ".JPG")):
				Contents_list.remove(item)
		if len(Contents_list) == 0:
			continue
		else:
			Valid_theme_chosen = True
			print("A theme has been chosen!")

print("\n\nThe theme is: " + Elected_theme[0])


