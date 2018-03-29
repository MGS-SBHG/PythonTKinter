#!/usr/bin/python3
# grid.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()



#create more complicated arrangements with the grid manager:
#    certain widgets span across multiple rows or columns. 
# the blue is centered below the green and orange labels, 
# and the yellow label is centered vertically off to the right side.

#           Columns
#        Green    Orange        
# Rows    0,0    0,1
#                         Yellow 0,2 - 1,2      
#         Blue          
#    span 1,0 - 1,1         

# the blue label spans across two columns, configure the "column span" property = 2. 
#     origin the left-most cell, row 1, column 0, with column span = 2

# the yellow label spans across two rows, configure the row span property = 2.
#     origin will be the top-most cell it's in, row 0, column 2 with a row span of 2.
 
# the sticky property:
#    control which side of the cell the widget will be anchored to by configuring the sticky property. 
#    The value for the sticky property is a string containing one or more cardinal directions represented as lowercase: n, s, e and w. 
#    refer to the top, bottom, right and left sides of the cell respectively.
     
ttk.Label(root, text = 'Yellow', background = 'yellow').grid(row = 0, column = 2, rowspan = 2, sticky = 'nsew')
ttk.Label(root, text = 'Blue', background = 'Blue').grid(row = 1, column = 0, columnspan = 2, sticky = 'nsew')

# adding padding around the widget.
#    grid geometry manager by using the pad x and pad y commands. 
# add padding to the green label by using 
#    padx = 10 
#    pady = 10. 
# adds, external to the label, 10 pixels of padding on each side in the x direction 
# and 10 pixels of padding in the y direction. 
ttk.Label(root, text = 'Green', background = 'Green').grid(row = 0, column = 0, sticky = 'nsew', padx = 10, pady = 10)

# add padding internal to the label - using the ipad property. 
#    ipadx = 25 pixels of padding around the orange label, 
#    ipady = 25 pixels in the y direction. 
ttk.Label(root, text = 'Orange', background = 'Orange').grid(row = 0, column = 1, sticky = 'nsew', ipadx = 25, ipady = 25)


# the weight property:
#    To make the cells themselves resize when the window is resized, we need to configure the weight property for each column and row.
#    The weight property tells the row or column how much it should grow relative to the other rows or columns to fill the space created when the parent widget is resized. 
#    By default all rows and columns have a weight of zero, meaning that they will not resize to fill the parent. 
#    configure weights by calling the "row configure" and "column configure" on the parent widget. 

# the root widget is our parent widget:  
# root.rowconfigure, 
# row number 0, the first parameter, the index of the row.
# set weight property = 1 

# rowconfigure row number 1 
# set 1st parameter = 1,
# set the weight for row one = 3 
#    configures row one to expand at a rate of three pixels for every one pixel that row zero expands 
# to fill the parent widget. 

root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 3)
root.columnconfigure(2, weight = 1)

root.mainloop()
