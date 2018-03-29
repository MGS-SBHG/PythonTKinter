#!/usr/bin/python3
# pack.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

# import the standard Tk enter package 
from tkinter import *
# import Ttk module 
from tkinter import ttk        
# root top level window    
root = Tk()

# creating a basic layout label using the Ttk label construction method. 
    # a child of my root window, 
    #use our familiar text of "Hello Tkenter," 
    # set the background in my label to be yellow.
label = ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'yellow').pack(side = LEFT, anchor = 'nw')

# creating blue label           
ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'blue').pack(side = LEFT, padx = 10, pady = 10)
# create green label          
ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'green')

# add padding around the widgets, 
#    can do so with the padx and pady properties. 
#        blue widget:
#        add external padding around the outside of the widget. 
#            i.e.  add 10 pixels of padding to each side in the X direction; 
#                      10 pixels of padding to each side in the Y direction 
label.pack(side = LEFT, ipadx = 10, ipady = 10)
print(label)


# Since this program has multiple widgets inside of the master window, which are being managed by the pack manager,     
#    the pack slaves method 
#        returns a list of all widgets contained within a parent widget that are using the pack manager.

#to configure some property for all the widgets for a single parent. 
#     to configure all of my widgets to use the fill and expand property to completely fill the space around them, 
#        create a for loop over the widgets that are found in my root window, 
#        call the pack slaves method which will return a list of all of the labels being managed by the pack manager.
#        For each of those widgets in pack slaves, call the pack configure method, 
#            configure the properties 
#                fill = BOTH 
#                expand = True. 

#        pack slaves method called on the parent widget returns a list of all the child widgets managed by the pack manager      
#       on each of those widgets, call the pack configure method to set the packing properties on the widget. 
#       for loop will cycle through all of the widgets in that master window.

for widget in root.pack_slaves():
    widget.pack_configure(fill = BOTH, expand = True)
    print(widget.pack_info())


# the pack forget method:
# no longer want to display the yellow label, remove it from the GUI 
label.pack_forget()

root.mainloop()
