#!/usr/bin/python3
# keyboard.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        


# create callback method called "KeyPress." 
#    need to give it one input parameter, which the event handler will use to parse an object containing information about the keyboard event. 
#    the keyboard event handler is expecting a single input parameter, so if you forget it or add extra parameters, then Python will throw an exception.
#       event" (can name it whatever you want to)
# the different information that's available in "event," 
# and print those to the console. 
#    type of event. event.type
#    name of the widget which triggered the event. 
#    the character if it's printable that was pressed to trigger the event. 
#    "keysym," event.keysym which is the "key sym" that was pressed, or the symbol of the key.
#    key code contains the numeric code of the key that was pressed. 

def key_press(event):
    print('type: {}'.format(event.type))
    print('widget: {}'.format(event.widget))
    print('char: {}'.format(event.char))
    print('keysym: {}'.format(event.keysym))
    print('keycode: {}\n'.format(event.keycode))


# create my "shortcut" function. 
#    parse in an action, "print action." 

def shortcut(action):
    print(action)
    
root = Tk()

# To make my program listen for a keyboard event, 
# use the "bind" method on the master root window. 
#    first parameter is a string containing specially-formatted descriptions of the events you want to listen for. 
#    use the "KeyPress" event. 
#        open and closed angle brackets on either side.
#    second parameter: the name of the callback function or method you want to execute. 

root.bind('<KeyPress>', key_press)


# Control-C:
#    common keyboard combination, Control-C.
        
#        root.bind('<Control-c>', key_press)
 
#    type, "control" dash "C," so this will trigger an event when the user holds Control and presses C. 

# create a function called "shortcut," 
#    parse in the string "copy," because that's what Control-C typically refers to.

root.bind('<Control-c>', lambda e: shortcut('Copy'))


#Control-V:
#    bind to the event of the user pressing Control-V, which typically refers to "paste." 

root.bind('<Control-v>', lambda e: shortcut('Paste'))

root.mainloop()
