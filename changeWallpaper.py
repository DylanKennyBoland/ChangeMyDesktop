#!/usr/bin/env python3

# Modules that we will need:
import random
import os
import sys
import ctypes
import json
import argparse

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
# Strings that are used in the "main" function
root = "C:\\Users\\Kenny\\Pictures\\" # root of the folder

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
            themeSpecified = False # unsetting this flag variable for in case we
            # enter there is another iteration of this while loop...
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
    
        