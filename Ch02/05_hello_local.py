#!/usr/bin/python3
# hello_local.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk

class HelloApp:
# The init method takes one parameter, called Master, 
# which is the Tk widget to use as the parent of all other widgets in the GUI.
# If we execute this Python script directly, 
# the piece of code at the bottom 
# if __name__ == "__main__": main()
# will detect that it is being run as main, 
# and will execute the main function.
 
    def __init__(self, master):
        
# label, which is a child of the master window, 
# assign it to the initial text value of Hello, Tkinter. 
# store a reference to this label in a class variable 
# so that we can access it later to change its text.
        self.label = ttk.Label(master, text = "Hello, Tkinter!")
        
# The label is then put into place using the grid command to put it at 
# Row 0, Column 0, represents the top right corner of that master window, 
# configure it to span across the 2 columns below it.         
        self.label.grid(row = 0, column = 0, columnspan = 2)
      
# After that, we create the Texas and Hawaii buttons for the program to use 
# use the grid geometry manager to place them at Row 1, Column 0 and Row 1, Column 1 respectively.
# When creating the buttons, we assign the command property to be the callback
# method to use for each one, so if the Texas button is clicked it will execute the Texas_hello method, 
# if the Hawaii button is clicked it will execute the Hawaii_hello method.        
        ttk.Button(master, text = "Texas",
                   command = self.texas_hello).grid(row = 1, column = 0)

        ttk.Button(master, text = "Hawaii",
                   command = self.hawaii_hello).grid(row = 1, column = 1)

# 2 methods down below, each of which uses the config method on the label 
# object to change its text to the appropriate local greeting
 
# Texas_hello changes the label to say Howdy Tkinter, 
    def texas_hello(self):
        self.label.config(text = 'Howdy, Tkinter!')
# Hawaii_hello method changes the text to say Aloha Tkinter.
    def hawaii_hello(self):
        self.label.config(text = 'Aloha, Tkinter!')

# main function , .             
def main():            
# use the Tk constructor method to create a top level Tk window named root    
    root = Tk()
# pass that to the Helloapp constructor method to use as the master window    
    app = HelloApp(root)
# Finally, we call the mainloop method on that top level window 
# to enter into the Tk event loop, where it will sit and wait to react 
# to the button presses.    
    root.mainloop()
    
if __name__ == "__main__": main()
