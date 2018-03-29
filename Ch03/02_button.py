#!/usr/bin/python3
# button.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

# importing the Tkinter package
from tkinter import *

# import the themed TTK module. "from Tkinter import TTK.
from tkinter import ttk        
    
# call the TK constructor method, to create my top-level root window    
root = Tk()

# create a button by callng the themed TTK button constructor method
# "Button" is spelled with a capital B.
# parent is the first parameter
# the property for the button called "text"
button = ttk.Button(root, text = "Click Me")


# use pack geometry manager 
button.pack()

# create a function containing the code to execute when the button is pressed.
def callback():
    print('Clicked!')
    
# configure the command property of the button 
# to tell it to execute that button whenever the button is pressed.
# use the "button.config" method on my button object, 
# set the command property to name of function to execute.
button.config(command = callback)

# programmatically simulate a button click by using the "invoke" method. 
button.invoke()

# a state which determines whether active and can be used or 
# disabled and unusable.
# call will disable the button:
button.state(['disabled'])

# check what the current state of a button is
# using the "instate" method
# "Is my button in this state?"
print(button.instate(['disabled']))

# re-enable my button; 
# use "state" method the "!disabled" flag.
# "Set the state to 'Not disabled.' 
button.state(['!disabled']) # bang "disabled" flag

# check that it's in this non-disabled state
# "instate" method, by calling "instate" bang "disabled."
print(button.instate(['!disabled']))

# add an image to the button.
# create image using the "PhotoImage" constructor. 
# parse in the directory to the file with that image Python logo.gif
logo = PhotoImage(file = 'python_logo.gif') # change path to image as necessary

# use the "config" method on the button to set the image property to that logo 
# configure the "compound" property to be "LEFT" 
# places the logo image to the left of the text.
button.config(image = logo, compound = LEFT)

# "subsample" method of the "PhotoImage" object to resize images within Tkinter
#  parse in two values, an X and Y - use every Xth and every Yth pixel in each direction.
#  parsed in the values five and five 
#  it'll subsample and take every fifth pixel in the X direction, 
#  and every fifth pixel in the Y direction of that image, 
#  and create a new "PhotoImage" object here named "small logo."  
small_logo = logo.subsample(5, 5)

# reconfigure my button, to use this smaller logo
button.config(image = small_logo)

root.mainloop()
