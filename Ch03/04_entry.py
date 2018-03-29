#!/usr/bin/python3
# entry.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

# imported the TKinter package 
from tkinter import *
# the ttk inter module, 
from tkinter import ttk        
# created a top level route window      
root = Tk()

# call TTK module then entry constructor method.
#  1st parameter the parent widget, my top level window. 
#  2nd parameter the property for width = 30. 
entry = ttk.Entry(root, width = 30)

# let's use the pack method 
# to add the entry widget to our top level window. 
entry.pack()

# use the get method to retrieve the current contents 
# directly from the entry field.
# "entry.get()" returns a string of the contents of the entry field.  
entry.get()

# to change the contents of the entry field, 
# use the insert and delete methods.

# the delete method, 
#  pass in two parameters: 
#       the beginning and end indices 
#       of the characters I want to delete from that entry field. 
# Those indices are non inclusive, so whatever the last index is, 
# that character will not be deleted.
 
# index of zero to one will delete everything from 
# the zeroth character at the beginning to the first character. 
#   non inclusive - the first character will Not be included  
# which means it will delete the H off of my string.

entry.delete(0, 1)

# using the delete command w/ the key word "end" 
# will delete everything up to the end of that entry field. 
# from 0 to END will delete the entire contents of entry field.
 
entry.delete(0, END)

# To insert text into the entry field using the insert command, 
#    need to pass two parameters. 
#        first: index, characterwise, where in that entry field I want to insert the [new text], 
#        second: a string of the text to enter.
entry.insert(0, 'Enter your password')

# to use an entry field as a password input field, 
# a common application for it to hide the characters 
# that the users enter. 
# using the show property for the entry widget. 
# to configure a property, use the config command, 
# configure the show property and pass it a string '*' asterisk. 
# every character displayed within the entry field with that string. 
# as the user types in their password, it will be replaced with asterisks. 

entry.config(show = '*')

# the state method to enable and disable the entry field. 
# "entry.state," disabled, 
# will be grayed out;  
# can no longer select any text from it, 
# can't enter any text either.
entry.state(['disabled'])



# to undisable it, 
# the state command w/ the bang disabled string, 
# it functions normal again. 
entry.state(['!disabled'])


# "read only" state 
#  to select texts from the field, 
# can select and drag
# useful if you want the user to be able to copy something 
# like a generated key to their clipboard so they can use it 
# elsewhere in another program.
# they can NOT enter any text. 
entry.state(['readonly'])


root.mainloop()
