#!/usr/bin/python3
# scrollbar.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

# imported the Tk intro package 
from tkinter import *
# import Ttk module,
from tkinter import ttk        

# created my root top level window.     
root = Tk()

# create the canvas, 
#    rather then defining the width and height of the canvas, 
#    define the scroll region. 
#    a rectangular area, seen and unseen, over which the canvas will scroll. 
#    create the x and y scroll bars as usual by using the scroll bar 
#    constructor method and I configure the command property 
#    to use the canvas.xview and canvas.yview accordingly.
canvas = Canvas(root, scrollregion = (0, 0, 640, 480), bg = 'white')

# configure the canvases 
#    xscroll command to use my xscroll bars set command 
#    yscroll command to execute the yscroll.set method from the y scroll bar.
xscroll = ttk.Scrollbar(root, orient = HORIZONTAL, command = canvas.xview)
yscroll = ttk.Scrollbar(root, orient = VERTICAL, command = canvas.yview)
canvas.config(xscrollcommand = xscroll.set, yscrollcommand = yscroll.set)


# use the grid geometry manager to place the canvas 
#    place my x scroll bar below it 
#    place the y scroll bar to the right of it. 
canvas.grid(row = 1, column = 0)
xscroll.grid(row = 2, column = 0, sticky = 'ew')
yscroll.grid(row = 1, column = 1, sticky = 'ns')

def canvas_click(event):
    # call canvas.canvasx and canvas.canvasy methods 
    #    will translate those x and y coordinates 
    # to where they actually appear on the canvas. 
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    
    # code which breaks out those x and y values and 
    # uses the canvas.create_oval method to draw an oval 
    # on that point of the canvas. 
    canvas.create_oval((x-5, y-5, x+5, y+5), fill = 'green')

# call the bind method on the canvas widget to bind it 
# to whenever the user clicks their mouse button.
# if the user clicks on the canvas, 
#    it will execute the canvas click method and pass in event information, 
#    contains the x and y location on the canvas where that click occurred.
canvas.bind('<1>', canvas_click)

root.mainloop()
