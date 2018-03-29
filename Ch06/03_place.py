#!/usr/bin/python3
# place.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

# configure the main menu to be 640 by 480 pixels. 
# using the geometry method 
# configure it pass in a string of 640 by 480.
# provide the XY coordinates at which to place the window on the screen. 

root.geometry('640x480+200+200')

# create four labels to use in placing around the window. 
# children of the root, their text will be a color, and their background will be colored. 
#labels yellow, blue, green, orange. 
#use the place manager to place a label at an exact location within that master window by providing x and y coordinates. 
#yellow label at the x position of 100 and the y position of 50.

# These coordinates are in pixels relative to the top left corner of the parent window. 
# Positive x values move the widget to the right and positive y values move the widget down. 
# This placed the label 100 pixels to the right of the left side of the screen, 
# and 50 pixels down from the top of the screen. 
# These are absolute coordinates 
# and the label will not move relative to that corner of the screen as the window is resized.

# specify the widget's size:
#    configure the absolute size of a widget, use the width and height properties. 
#    configure yellow label: width = 100 pixels; height = 50 pixels. 

ttk.Label(root, text = 'Yellow', background = 'yellow').place(x = 100, y = 50, width = 100, height = 50)


# relx and rely properties:
# place the widget in relative locations based on the current size of the parent frame or window. 
#    specify the relx and rely properties
#    the blue label, relx = .5 and rely = .5. 
#    The values for relx and rely are fractional values between zero and one. They represent the percentage of the current width and height of the parent frame or window at which to place the widget.
# places the blue label at the center of the window. 
# if I resize the window the blue label stays at the center of the window. 
# if I make this window small, notice that blue label is near the middle of the window, 
# but not exactly centered. 
# TK is placing the top left corner of the label at the location defined 
# by the relx and rely properties.


# width represented in relative terms: 
#    use the relwidth and relheight properties. 
#    for blue label:    
#        relwidth = 0.5 
#        relheight = 0.5.
#    the blue label always be half the size of the window in both the x and y directions. 
#                 resized dynamically as the window is stretched and moved around. 

ttk.Label(root, text = 'Blue', background = 'blue').place(relx = 0.5, rely = 0.5, anchor = 'center', relwidth = 0.5, relheight = 0.5)


# Can combine relative and absolute coordinates within the place method. 
# When you do that, the relative location is calculated first, then the absolute coordinates are added onto that. 

# For the green label, call place and pass in a relx = .5;  
# an absolute location in the x = 100 pixels. 
# rely = .5, which is the middle of the window, 
# absolute y location = 50. 
# uses the relx and rely values to find the middle of the window, 
# then from that point it'll add an additional 100 pixels in the x direction and 50 pixels in the y direction. 

# the blue label always exists at the center of the window as we'd previously defined, 
# the green label is now always 100 pixels to the right of it and 50 pixels down.

ttk.Label(root, text = 'Green', background = 'green').place(relx = 0.5, x = 100, rely = 0.5, y = 50)

# Absolute coordinate values can also be negative: 
#    As the window's resized, those relative x and y values keep it in relative location to the blue label. 
#    Absolute coordinate values can also be negative. 
#        This will move the widget to the left in the x direction 
#        and upwards in the y direction. 

# example to use negative coordinates:
#    place a label in the top right corner of the window with a slight offset from the edge. 
# the orange label: 
#    specify its relative x location to be the right side, 
#    use the absolute x value with a negative value of 5 
#        to offset it by 5 pixels from the right.
#    offset it from 5 pixels from the top using y equals 5. 

#    by default the label will be anchored at this point using the top left corner of the label, 
#    change the anchor property to anchor this label using its top right corner. 

ttk.Label(root, text = 'Orange', background = 'orange').place(relx = 1.0, x = -5, y = 5, anchor = 'ne')

root.mainloop()
