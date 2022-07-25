#!/usr/bin/env python3

# Modules that we will need:
import random
import os
import sys
import ctypes
import json
import argparse
from PIL import Image

# Some general-info strings
helpMsg = """The desktop theme. The valid options are:
Philosophy,
Math,
Music,
Chess.
"""
noArgsMsg = """No theme specified. Picking one at random from the list
of possible themes."""

invalidThemeMsg = """Invalid theme specified. The valid options are:
Philosophy,
Math,
Music,
Chess.
"""
themeChosenMsg = """================================
The theme chosen is {} !
================================"""
imageChosenMsg = """The image chosen is {}."""

# Strings that are used in the "main" function
root = "C:\\Users\\Kenny\\Pictures\\" # root of the folder
templatePath = "C:\\Users\\Kenny\\Desktop\\Black Desktop Background Template.jpg" # path to the background template
resizedImageTag = "Resized and Formatted.jpg" # the tag used when renaming resized images

# Necessary for interacting with Windows desktop
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1) # get the screensize of computer

# Function to handle the input arguments
def parsingArguments():
    parser = argparse.ArgumentParser(description = "Theme for the new wallpaper.")
    parser.add_argument('--theme', type = str, help = helpMsg)
    return parser.parse_args()

def readInThemes():
    with open('Themes.json') as p:
        try:
            print("Reading in themes.json file...")
            themes = json.load(p)
        except:
            print("The themes.json file seems to be empty...")
            themes = {
                "Chess" : {"Path to Folder": root + "Chess\\",
                "Last Image Chosen": "None"},
                "Philosophy": {"Path to Folder": root + "Philosophy\\",
                "Last Image Chosen": "None"},
                "Math" : {"Path to Folder": root + "Maths\\",
                "Last Image Chosen": "None"},
                "Music" : {"Path to Folder": root + "Music\\",
                "Last Image Chosen": "None"}
            }
    return themes

def setDesktop(path, image):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path + image, 1)

def createDesktopImage(image, screensize, backgroundTemplate, location):
    backgroundTemplate = backgroundTemplate.resize(screensize)
    resizedImage = image.resize((screensize[1], screensize[1]))
    if location in ['Centre', 'centre', 'C', 'c']:
        # In the centre of the desktop...
        # The x-coordinate will be found by taking the width of the resized image and subtracting it from that of the 
        # background template - the resultant value will then be halved... the y-coordinate is calculated in much the same way
        # except we take the heights of the resized image and background template instead of the width...
        # The int() function is changing the data type from 'float' to 'int'... sometimes referred to as 'type casting' or 'type conversion'...
        pasteLocation = (int((backgroundTemplate.width - resizedImage.width)/2), int((backgroundTemplate.height - resizedImage.height)/2))
    elif location in ['right-hand side', 'right side', 'RightSide', 'Right', 'right', 'R', 'r']:
        pasteLocation = (int((backgroundTemplate.width - resizedImage.width)), int((backgroundTemplate.height - resizedImage.height)))
    elif location in ['left-hand side', 'left side', 'LeftSide', 'Left', 'left', 'L', 'l']:
        pasteLocation = (0, 0)
    else:
        print("ERROR: An invalid value was given for the 'Location' argument.")
        return -1
    # Now we'll perform the pasting of the resized image onto the background template:
    backgroundTemplate.paste(resizedImage, pasteLocation)
    finishedDesktopImage = backgroundTemplate
    return finishedDesktopImage


if __name__ == "__main__":
    themes = readInThemes() # read in the themes dictionary
    titles = [*themes] # get the titles into a list
    args = parsingArguments() # parse the input arguments (if there are any)
    # === Check if any input arguments have been specified ===
    themeSpecified = False
    if len(sys.argv) == 1:
        print(noArgsMsg)
    else:
        themeSpecified = True
        if args.theme not in titles:
            print(invalidThemeMsg)
            exit()
    validTheme = False
    while validTheme is False:
        if themeSpecified is True:
            theme = args.theme # get the theme title
            themeSpecified = False # unsetting this flag variable in case
            # there is another iteration of this while loop...
        else:
            theme = random.choice(titles)
        path = themes[theme]["Path to Folder"] # get the path to the folder
        lastImage = themes[theme]["Last Image Chosen"] # get the last image chosen for this theme
        # === Check if the theme's folder has any valid images ===
        if len(os.listdir(path)) == 0: # the theme's folder is empty
            titles.remove(theme) # remove theme so it is not picked again
            continue
        else:
            contents = [file for file in os.listdir(path) if file.endswith((".jpg", ".JPG", ".png", ".PNG"))] # get the folder contents
            if lastImage in contents:
                contents.remove(lastImage)
            if len(contents) == 0:
                continue
            else:
                validTheme = True
                print(themeChosenMsg.format(theme))
    
    # === Choose an image from the folder ===
    chosenImage = random.choice(contents) # pick an image from the list
    print(imageChosenMsg.format(chosenImage)) # display the name of the image that was chosen

    # === Update the "last image chosen" key ===
    themes[theme]["Last Image Chosen"] = chosenImage # updating the key's value to be the image just selected

    # === Update themes.json file ===
    with open("Themes.json", "w+") as p:
        json.dump(themes, p, indent=4)
    
    imageObj = Image.open(path + chosenImage) # open image as an object
    aspectRatio = imageObj.width/imageObj.height # get the aspect ratio of the image

    # === Set the desktop ===
    if 0.98 <= aspectRatio <= 1.2:
        # === Check if the image has already been resized ===
        if os.path.isfile(path + os.path.splitext(chosenImage)[0] + " " + resizedImageTag):
            setDesktop(path, os.path.splitext(chosenImage)[0] + " " + resizedImageTag)
        else:
            backgroundTemplate = Image.open(templatePath) # open the background template image as an object
            newDesktopImage = createDesktopImage(imageObj, screensize, backgroundTemplate, "R") # create the resized desktop image
            newDesktopImage.save(path + os.path.splitext(chosenImage)[0] + " " + resizedImageTag) # save it with new name
            setDesktop(path, os.path.splitext(chosenImage)[0] + " " + resizedImageTag)
    elif 1.7 <= aspectRatio <= 1.8:
        setDesktop(path, chosenImage)
    else:
        setDesktop(path, chosenImage)

    


    
        