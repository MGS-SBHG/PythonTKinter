#!/usr/bin/python3
# label.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

# import the Tkinter package
from tkinter import *
# the themed TK module, or TTK module
from tkinter import ttk        
    
# create a top-level TK window, use the TK constructor method 
# store that top-level window, or reference to it, 
# the variable called "root."     
root = Tk()


# create a label & store in a variable called "label," 
# access that theme TK module, so I type "ttk," 
# use the label constructor method. 
# Note that "Label" is spelled with a capital L. 
# This is common amongst all the constructor methods. 
# As with all constructor methods, 
# the first parameter is the parent widget of this label - 
#    the root top-level window, 
# add additional properties "Hello, Tkinter," 
# That creates the label widget object,
label = ttk.Label(root, text = "Hello, Tkinter!")

# To make it display on the screen:  
# use the pack geometry manager - call the pack method  
label.pack()

# change the text with the "config" command
# label.config(text = 'Howdy, Tkinter!')
label.config(text = 'Howdy, Tkinter! It\'s been a really long time since we last met.  Great to see you again!')

# cause this label to wrap the text onto multiple lines 
# by configuring the "wraplength" property. 
# configured this label to wrap the text within a 150 pixels' width.
label.config(wraplength = 150)

# by default text is justified and aligned to the left side of the label. 
# configure which side it's justified to by configuring the "justify" property.
# Options for the "justify" property: left, right and center, 
# type them in in all capital letters. 
# text is centered:
label.config(justify = CENTER)

# The "foreground" property sets the color of the text, 
# the input is going to be a string, and you can insert a hex value here, 
# or the name of common colors, such as blue, red, yellow and so on.
# the "background" property sets the color of the label area.
label.config(foreground = 'blue', background = 'yellow')


# the "font" property: to set the value of "font," 
# you parse it a list, the first item a string 'name of font' i.e. 'Courier'. 
# nbr: size of the font
# third string containing additional modifiers:
# 'bold', 'underline', 'italic' 
label.config(font = ('Courier', 18, 'bold'))

label.config(text = 'Howdy, Tkinter!')


# create a "PhotoImage" object.
# The "PhotoImage" class is used to display color images within Tkinter. 
# It can accept GIF, PGM or PPM files.
# use the "PhotoImage" constructor method.

logo = PhotoImage(file = 'python_logo.gif') # change path to image as necessary

# if we'd create the "PhotoImage" object in a class constructor method, 
# and stored it to a "class" variable, when the object instance in which 
# the photo image was created and stored loses scope, 
# it'll be garbage collected, and the "PhotoImage" object will be taken away too.


# apply it to my label
# The call "image" equal "logo," to configure the image property 
# is not actually saving a copy or reference to the "PhotoImage" object. 
# It's only using the name of the "PhotoImage" object to parse to TK. 
# This means if our logo image goes out of scope, 
# Python will garbage collect it, and TK won't be able to display it anymore. 
label.config(image = logo)

# Our label has two properties configured. 
# It has the text property, configured to a value for text, 
# and it also has an image associated with it.
# control which one is displayed by changing the "compound" property.
label.config(compound = 'text')

# options for "compound" are: "top," "bottom," "left" and "right." 
# display the text on the center of that image.
label.config(compound = 'center')

# display the image to the left of the text.
label.config(compound = 'left')

# always make sure that you store the image object to a variable location 
# that will not be garbage collected as long as you need to use it. 
# store a reference to the "PhotoImage" object in the TK label widget object 
# itself, since TK is holding onto that widget, and preventing it from 
# being garbage collected.
label.img = logo

# typing "label," and creating an image variable within that label object, 
# and parsing in "logo," so that we've saved a reference to that logo 
# inside that image variable. 
# configure the label to use that image instead: image = label.img. 
label.config(image = label.img)

root.mainloop()
