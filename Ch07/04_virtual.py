#!/usr/bin/python3
# virtual.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

# create a basic text entry widget using the ttk entry constructor and 
# putting that in the top level window with the pack method.

entry = ttk.Entry(root)
entry.pack()

# to bind to an event for the entry box: "entry.bind" 
#        first parameter is a string with the name of that event. 
# For virtual events, it has the double angle brackets and the name of this event is "copy".  
#        next the function that will be executed when this event occurs. i.e. use a lambda function.

# to bind to a virtual event,
#    enclose the name of the event in double angle brackets. 

# This lambda function we'll simply call the print function. 
#    for copy as well as paste. 
#    This copy and paste two virtual events are basically just pre-configured keyboard events for the entry widget. 

# these event bindings basically represent a pre-configured set of keyboard and mouse events, 
entry.bind('<<Copy>>', lambda e: print('Copy'))
entry.bind('<<Paste>>', lambda e: print('Paste'))



# create a new event binding for the entry widget, 
#    type entry dot event underscore add. 
#    provide a name for my new event binding. 
#        create an event binding that will be triggered whenever I type an odd number into the entry field. 
#        called "odd number"
#            pass in the various keyboard and mouse events that will trigger this new virtual event I'm creating. 
#        If the user types 1 or 3 or 5, 7, or 9 it'll trigger this event.
# Each of these represents the syntax for keyboard events of pressing one, three, five, seven, and nine. I close that statement. 

entry.event_add('<<OddNumber>>', '1', '3', '5', '7', '9')


# After I created my virtual event, I'll also need to bind to it. 
#    entry dot bind odd number, close string, and then I need to provide a function for the bind method to execute if odd number occurs. 
#    use a lambda function
#    print out that we saw an odd number.

entry.bind('<<OddNumber>>', lambda e: print('Odd Number!'))


# To view details about a virtual event: use the event underscore info method. 
#   After I've created my odd number event, 
# I'll call print, entry, and then I'll use the event info method to print out 
# the event information about my newly created odd number virtual event.
# it prints out the information about that virtual event  
# shows which keys will trigger the event. 1,3,5,7,9  

print(entry.event_info('<<OddNumber>>'))


# programmatically trigger them from within our code. 
#    call "entry dot event underscore generate" 
#        pass in the name of the virtual event 
#        will programatically trigger that event. 
# trigger an odd number event.
# trigger the paste event
 
entry.event_generate('<<OddNumber>>')
entry.event_generate('<<Paste>>')


# created a virtual event that we don't need to use anymore 
# delete it by using the "event delete" method. 
# "entry dot event underscore delete" 
#    pass in the name of the virtual event I want to delete.
#        delete "odd number" 
#        and it will no longer exist as a virtual event.
 
entry.event_delete('<<OddNumber>>')


root.mainloop()
