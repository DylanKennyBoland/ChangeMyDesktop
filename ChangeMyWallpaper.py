#!/usr/bin/env python3

import random, os, ctypes # These will be helpful modules to have!
from PIL import Image # Our function will need the methods inside this module or library...

def CreateDesktopImage(DesktopImage, DesktopDimensions, BackgroundTemplate, Location):
    BackgroundTemplate = BackgroundTemplate.resize(DesktopDimensions)
    ResizedImage = DesktopImage.resize((DesktopDimensions[1], DesktopDimensions[1]))
    if Location in ['Centre', 'centre', 'C', 'c']:
        # In the centre of the desktop...
        # The x-coordinate will be found by taking the width of the resized image and subtracting it from that of the 
        # background template - the resultant value will then be halved... the y-coordinate is calculated in much the same way
        # except we take the heights of the resized image and background template instead of the width...
        # The int() function is changing the data type from 'float' to 'int'... sometimes referred to as 'type casting' or 'type conversion'...
        PasteLocation = (int((BackgroundTemplate.width - ResizedImage.width)/2), int((BackgroundTemplate.height - ResizedImage.height)/2))#
    elif Location in ['right-hand side', 'right side', 'RightSide', 'Right', 'right', 'R', 'r']:
        PasteLocation = (int((BackgroundTemplate.width - ResizedImage.width)), int((BackgroundTemplate.height - ResizedImage.height)))
    elif Location in ['left-hand side', 'left side', 'LeftSide', 'Left', 'left', 'L', 'l']:
        PasteLocation = (0, 0)
    else:
        print("ERROR: An invalid value was given for the 'Location' argument.")
        return -1
    # Now we'll perform the pasting of the resized image onto the background template:
    BackgroundTemplate.paste(ResizedImage, PasteLocation)
    FinishedDesktopImage = BackgroundTemplate
    return FinishedDesktopImage


user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1) # This will be useful if we need to resize images...


Root = "C:\\Users\\Kenny\\Pictures\\" # This is the root of the path...

Theme_list = {
	"Chess" : Root + "Chess\\",
	"Philosophy" : Root + "Philosophy\\",
	"Music" : Root + "Music\\",
	"Math" : Root + "Math\\"
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
			print("===========================")
			print("A theme has been chosen!")
			print("===========================")

# Some general print statements for clarity and in order to let
# the user know what the chosen theme is, as well as what its corresponding
# folder contains...
print("\n\nThe theme is: " + Elected_theme[0])
print("\n...And the folder contents are: ", Contents_list)
Chosen_Desktop_Image = random.choice(Contents_list)
print("\nThe new desktop image will be: " + Chosen_Desktop_Image)

# Now we'll check if we need to resize or format the chosen image (perhaps it's not the correct size or shape)...
Desktop_Image_Object = Image.open(Path_to_folder + Chosen_Desktop_Image)
print("INFO: The desktop image has the following size: ", Desktop_Image_Object.size)

Image_aspect_ratio = Desktop_Image_Object.width/Desktop_Image_Object.height
print("INFO: The image has an aspect ratio of: ", Image_aspect_ratio)

# The two print statements below are merely to box off the information being printed to
# the screen... hopefully making it appear less cluttered...
print("\n===========================================================================")
print("\n===========================================================================\n")

if (Image_aspect_ratio < 1.1) and (Image_aspect_ratio > 0.98):
	print("INFO: The image is more or less a square, as it has an aspect ratio near 1...")
	print("INFO: Going to attempt to resize and format the image...")
	print("INFO: First going to check if it's been resized and reformatted already before...")
	if os.path.isfile(Path_to_folder + os.path.splitext(Chosen_Desktop_Image)[0] + " " + "Resized and Formatted.jpg"):
		print("- The image has already been resized...")
		print("- Setting the resized version as the desktop...")
		ctypes.windll.user32.SystemParametersInfoW(20, 0, Path_to_folder + os.path.splitext(Chosen_Desktop_Image)[0] + " " + "Resized and Formatted.jpg", 1)
	else:
		print("- The image has not been resized... doing so now")
		BackgroundTemplate = Image.open('C:\\Users\\Kenny\\Desktop\\Black Desktop Background Template.jpg')
		NewDesktopImage = CreateDesktopImage(Desktop_Image_Object, screensize, BackgroundTemplate, "R")
		print("- The resized and reformatted image has a size of: ", NewDesktopImage.size)
		NewDesktopImage.save(Path_to_folder + os.path.splitext(Chosen_Desktop_Image)[0] + " " + "Resized and Formatted.jpg") # Saving our new desktop image...
		print("INFO: Saving" + os.path.splitext(Chosen_Desktop_Image)[0] + " " + "Resized and Formatted.jpg" + "...")
		ctypes.windll.user32.SystemParametersInfoW(20, 0, Path_to_folder + os.path.splitext(Chosen_Desktop_Image)[0] + " " + "Resized and Formatted.jpg", 1)
elif (Image_aspect_ratio > 1.7) and (Image_aspect_ratio < 1.8):
	print("- The image is in the shape of the desktop screen, as its aspect ratio is approximately 16:9")
	print("- Setting the desktop to be: ", Chosen_Desktop_Image)
	ctypes.windll.user32.SystemParametersInfoW(20, 0, Path_to_folder + Chosen_Desktop_Image, 1)
else:
	print("INFO: Setting the new desktop image now...")
	ctypes.windll.user32.SystemParametersInfoW(20, 0, Path_to_folder + Chosen_Desktop_Image, 1)
