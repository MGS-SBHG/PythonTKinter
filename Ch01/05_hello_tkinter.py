#!/usr/bin/python3
# hello_tkinter.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

# imports all of the functions and variables from the TKinter package. 
# TKinter is spelled out using all lowercase letters. 
# In Python 2, TKinter is spelled with a capital T, 
# In Python 3, it's written using all lowercase.

from tkinter import * 

# TK constructor method to create a new top level widget, 
# the main window, and assign it to the variable named Root. 
root = Tk()

# After that, we create a label with the text hello TKinter 
# as a child of the root window, 
# and use the pack geometry management method to put it on the window. 
Label(root, text="Hello, Tkinter!").pack()

# run the main loop method for the root window.
root.mainloop()

