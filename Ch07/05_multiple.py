#!/usr/bin/python3
# multiple.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

# create two label widgets. 
#    Label one, which is a child of the root and has the text label one on it. 
#    Label two. 
#    add those to the window with the pack command. 
label1 = ttk.Label(root, text = 'Label 1')
label2 = ttk.Label(root, text = 'Label 2')
label1.pack()
label2.pack()

# label1.bind adds an event binding to label one that will print a message when it's clicked on.   
# use the mouse event of button press, which is triggered when any mouse button is pressed 
#    execute a lambda function which will print the message that button press 
#    occurred for a label. 
#    button press label. 
label1.bind('<ButtonPress>', lambda e: print('<BP> Label'))


# add another bind to label one
#    label1.bind and bind specific to just the left most button 
#    which is button one on the mouse. 
#    do a similar lambda function here to print out that this time 
#    button one was pressed and it was on a label.
label1.bind('<1>', lambda e: print('<1> Label'))

# to configure that left mouse click event to Both labels, 
#    bind it to the master window instead of just binding it to the label one. 
#    Binding an event to a top level window will propagate that binding to all of its child widgets. 
#    call root.bind pass in the string to trigger on the left button mouse click - button number one
#    a lambda function; 
#    print out that button one was pressed
#    pressed on the root instead of on a label.
# if I click on label one it actually triggered two events. 
#        One of those events is triggered for the label and 
#        the other is triggered for the master.
 
root.bind('<1>', lambda e: print('<1> Root'))

# can remove a previously configured event binding by using the unbind method.
#    remove those bindings from my label one by calling label1.unbind 
#        pass in the binding that I had configured. 
#        remove the left mouse button binding 
#        remove the general binding I created for that label with button press. 

label1.unbind('<1>')
label1.unbind('<ButtonPress>')


# if we have multiple top level windows in our program, 
#    can create an event binding that will apply to all of them by using the "bind all" method. 
#    call "root.binda_all" 
#        pass in my event binding. 
#        bind to the escape key 
#        lambda e and will print out escape.
# If I save and run this, 
#    if I had multiple windows in my program no matter which window has scope, 
#    if I press the escape key it'll execute that function.

root.bind_all('<Escape>', lambda e: print('Escape!'))


root.mainloop()
