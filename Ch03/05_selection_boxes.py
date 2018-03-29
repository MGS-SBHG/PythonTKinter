#!/usr/bin/python3
# selection_boxes.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com


# The combo box widget is your basic drop down selection tool. 
#    The user can click on a side button, which presents them with a drop down list of all the available options.
#    useful for making a selection from a series of choices that may or may not have an obvious order to them. 

# With a spin box
#    the user only sees one option at a time, which represents their current selection. 
#    can cycle through the available choices by clicking the up and down arrow buttons on the side of the widget. 
#    useful for choosing from a list of options that have an inherent order. 
#    For example, a range of numbers. 

# imported my TK enter package
from tkinter import *

# imported the TTK module
from tkinter import ttk        

# created top level root window using the TK constructor method.    
root = Tk()

# create a variable which will store the value from that combo box. 
# month use the StringVar constructor method to create a string variable.
month = StringVar()

# use the TTK modules themed combo box constructor method, 
# 1st parameter being the parent, or the root window, 
# 2nd parameter: the property for text variable. 
# the variable tied to the value that's selected in the combo box. 
# set that to month. 
combobox = ttk.Combobox(root, textvariable = month)

#use pack geometry manager to place it in the window. 
combobox.pack()

# selected values from the combo box will be stored 
# in that month string variable.
# the combo box values to select. 
#    configure the values available to select from the combo box, 
#    configure the values property. 
#        the config method to configure values, 
#            for values you pass in a list of strings
#         which will be the optional values for that combo box.
# a list of strings for the twelve months out of the year pass that in. 
combobox.config(values = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# To get the value that's currently in the combo box, 
# use the get method on that month variable. 
print(month.get())

# use the set method on that variable 
# programmatically change the value 
# that's showing up in the combo box.
# set it to December, 
month.set('Dec')

# little dangerous because 
# I could use this set method to set it to 
# something that's not one of the standard values for the combo box. 
month.set('Not a month!')

# create another variable call it the year using the StringVar 
# constructor method. 
year = StringVar()

# create spin box
#        NOT available as a theme TK widget. 
#        ONLY available as one of the original TK widgets. 
# use Spinbox, pass in the parameters
#     1st: root, or the top level window, 
#     2nd: properties - the beginning and end range of value for the spin box.
#    from 1990 up to 2020. 
# "from_" from w/ an underscore on the end of it; regular "to" 
# Since I don't need to save a reference to the spin box, 
# just call the pack command directly on the output of this constructor method.

Spinbox(root, from_ = 1990, to = 2020, textvariable = year).pack()

# To get the value from the spin box, 
# use the get method on that year variable 
print(year.get())

root.mainloop()
