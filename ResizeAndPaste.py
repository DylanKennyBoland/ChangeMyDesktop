import ctypes
from PIL import Image

image = Image.open('C:\\Users\\Kenny\\Desktop\\e5 Let the Bishop out!.jpg') # Just opening a file that I have on my desktop... this can be changed...
print("The image has a size of: ", image.size)
resized_image = image.resize((1080, 1080)) # The height of my screen in pixels... the image is square, so I'm simply increasing its size so that it fits my screen fully
Desktop_background = Image.open('C:\\Users\\Kenny\\Desktop\\Grey Desktop Background Template.jpg')
print("\n\nThe grey desktop background image has a size of: ", Desktop_background.size)
Background_copy = Desktop_background.copy() # Making a copy of this image which we'll paste onto...
Paste_location = ((Background_copy.width - resized_image.width), (Background_copy.height - resized_image.height))
#print(Paste_location) # The position where we'll paste the chess image that we opened on line 4...
Background_copy.paste(resized_image, Paste_location)
Background_copy.save('C:\\Users\\Kenny\\Desktop\\Pasted Chess Image.jpg')
ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Users\\Kenny\\Desktop\\" + "Pasted Chess Image.jpg", 0)
