#!/usr/bin/python3
# mouse.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        


# create a function called mouse press. 
#    mouse events will also pass an event object containing information about the event. 
#    the event object for mouse events has different fields than for the keyboard event. 
#    those events so we can see what's contained. 
#    print the values to the console. 
# type: event dot type.
# the widget which triggered it. access that with event dot widget. 
# a number for the mouse button that was pressed: event.num, 
# pass in X and Y coordinates for where the mouse was pressed: event dot X; event dot Y

# Getting the X and Y coodinates in relation to the entire screen can be useful 
# if you want to do something like move a window to that location or spawn a right click menu. 
#    event dot X underscore root and 
#    event dot Y underscore root.
# These root values will give you the coordinates related to the entire screen. 
# Getting the X and Y coordinates in relation to the entire screen can be useful 
# if you want to do something like move a window to that location or spawn a right click menu.
 
def mouse_press(event):

    global prev # track the previous and current locations that the mouse is at. 

    print('type: {}'.format(event.type))
    print('widget: {}'.format(event.widget))
    print('num: {}'.format(event.num)) 
    print('x: {}'.format(event.x))
    print('y: {}'.format(event.y))
    print('x_root: {}'.format(event.x_root))
    print('y_root: {}\n'.format(event.y_root))
    prev = event


def draw(event):
    # track the previous and current locations that the mouse is at
    global prev 
    
    # use that global previous and use it with the create line method to draw a line 
    # from the previous X and previous Y coordinates 
    # to the new current event X and event Y coordinates.
    # line width = 5 
    canvas.create_line(prev.x, prev.y, event.x, event.y, width = 5)
    
    # after I've used that previous X and Y coordinate, 
    # save the current event to that previous variable. 
    prev = event
    
root = Tk()

# create a new canvas object 
#    assign to a variable called canvas
#    a child of the root, 
#    width of 640 pixels and a height of 480 pixels
#    background that's white.
canvas = Canvas(root, width = 640, height = 480, 
                background = 'white')
# call the canvas dot Pack method to place it on our window. 
canvas.pack()

# create an event binding for when the user clicks on the canvas with any mouse button. 
#    call this on the canvas rather than the top level window, 
#    use the bind method
#        pass in the string, open angle brackets, button, press, notice the capital B and capital P, 
#        the second parameter we pass is the function that will be executed when the user presses a button.
canvas.bind('<ButtonPress>', mouse_press)

# press and hold Btn1 and move the mouse
canvas.bind('<B1-Motion>', draw)

root.mainloop()
