#!/usr/bin/python3
# callback.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        


# callback function to accept a parameter of a number 
#    and to print that to the console.
#    Number is its input and it'll print out that number. 
def callback(number):
    print(number)
    
root = Tk()


# create three numbered buttons 
# a child of the root window 
# the button will simply say "click me"
# call the Pack Geometry Manager to place it on my window. 
# configure the command callback for this button, 
# w/ a function or method to point to. 

# create a lambda function for each of these calls:
#    The lambda keyword creates an anonymous function 
#        containing the callback method which we can use to configure the command callback. 
#    configure each command property to be an anonymous lambda function 
#        which points to the callback function passing the correct parameters for that number.
ttk.Button(root, text = 'Click Me 1', command = lambda: callback(1)).pack()
ttk.Button(root, text = 'Click Me 2', command = lambda: callback(2)).pack()
ttk.Button(root, text = 'Click Me 3', command = lambda: callback(3)).pack()

root.mainloop()
