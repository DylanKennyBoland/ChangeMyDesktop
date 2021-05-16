import ctypes # This will be needed if we decide to set the desktop in this script...
import os # This might be useful for parsing files into their names and extensions... (e.g. remove the .jpg from an Image file to get the name of the image...)
from PIL import Image # Our function will need the methods inside this module or library...

# Let's write the function and test it out before adding it to the main
# script...
def CreateDesktopImage(DesktopImage, DesktopDimensions, BackgroundTemplate, Location):
    BackgroundTemplate = BackgroundTemplate.resize((1920, 1080))
    ResizedImage = DesktopImage.resize((DesktopDimensions[1], DesktopDimensions[1]))
    if Location == "Centre":
        # In the centre of the desktop... with a nice jet-black background...
        # The x-coordinate will be found by taking the width of the resized image and subtracting it from that of the 
        # background template - the resultant value will then be halved... the y-coordinate is calculated in much the same way
        # except we take the heights of the resized image and background template instead of the width...
        # The int() function is changing the data type from 'float' to 'int'... sometimes referred to as 'type casting' or 'type conversion'...
        PasteLocation = (int((BackgroundTemplate.width - ResizedImage.width)/2), int((BackgroundTemplate.height - ResizedImage.height)/2))#
    if Location == "RightSide":
        PasteLocation = (int((BackgroundTemplate.width - ResizedImage.width)), int((BackgroundTemplate.height - ResizedImage.height)))
    # An 'else' condition would need to be placed here to catch erroneous inputs, and to make the function more robust... but we're simply
    # testing out some ideas and we know what the function expects, so I'll leave this addition for later...
    
    # Now we'll perform the pasting of the resized image onto the background template:
    BackgroundTemplate.paste(ResizedImage, PasteLocation)
    FinishedDesktopImage = BackgroundTemplate
    return FinishedDesktopImage

Image_FileName = 'e5 Let the Bishop out!.jpg' # Our image file name...
DesktopImage = Image.open('C:\\Users\\Kenny\\Desktop\\e5 Let the Bishop out!.jpg') # A test image
BackgroundTemplate = Image.open('C:\\Users\\Kenny\\Desktop\\Black Desktop Background Template.jpg')
# The dimensions of our desktop...
Dimensions = (1920, 1080)
# Now let's test out the function...
NewDesktopImage = CreateDesktopImage(DesktopImage, Dimensions, BackgroundTemplate, "Centre")
print("The new image has a size of: ", NewDesktopImage.size)

# When we create a new desktop image from one which was not the correct size, we want to retain its name but add on a tag to say
# that it was resized and formatted - that's what we'll do below! os.path.splitext(file_name) will take the just the name
# of a file, and leave out the extension (.jpg for image files)...
NewDesktopImage_FileName = os.path.splitext(Image_FileName)[0] + " " + "Resized and Formatted.jpg"
print("The new desktop image is called: ", NewDesktopImage_FileName)
NewDesktopImage.save('C:\\Users\\Kenny\\Desktop\\' + NewDesktopImage_FileName) # Saving our new desktop image...


