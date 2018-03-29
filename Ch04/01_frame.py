#!/usr/bin/python3
# frame.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

# import the TkInter package 
from tkinter import *
# the TkInter module 
from tkinter import ttk        
# created my root top level Tk window.     
root = Tk()

# create a frame, 
#    use the frame constructor found in the Ttk module, spelled with F,
#    1st paramenter of top level root window to use as the parent for this frame.
frame = ttk.Frame(root)

# use the pack geometry manager within that top level window 
# to place the frame inside of it. 
frame.pack()

# manually configure the width and height of the frame: 
# 100 pixels high by 200 pixel wide frame.
frame.config(height = 100, width = 200)

# the frame border  
#    six different types of frame relief:  
#        the FLAT relief No border; default  
#        RAISED frame appear either elevated 
#        SUNKEN relief: frame appear depressed, 
#        SOLID
#        RIDGE 
#        GROOVE border different styles of lines around your frame.
# configure the type of relief for our frame,  
frame.config(relief = RIDGE)

# create a button widget using the Ttk button constructor. 
#        make its parent the frame created. 
#        configure the text of the button to say "click me" 
#        use the grid geometry manager here instead of the pack manager. 
#        configured the top level root window to use the pack manager 
#        by using it on the frame, 
#        By using the grid geometry manager on this widget 
#        I'm adding to the frame, any other widgets I add to the frame later 
#        will also need to be done so by using the grid geometry manager.
ttk.Button(frame, text = 'Click Me').grid()

# add padding to my frame to create a buffer around the button on the inside of the frame by configuring the padding property. 
#    Padding accepts a list of two values: 
#        the number of pixels in the X direction and 
#        the number of pixels in the Y direction of padding to add around that frame. 
#        a frame with 
#            30 pixels padding on the inside in the X direction  
#            15 pixels of padding in the Y direction.
frame.config(padding = (30, 15))

# the label frame. 
#        create a label frame using the Ttk label frame constructor method 
#        both the L and F are capitalized in label frame. 
#        make the top level root window the parent for this frame. 
#        properties  
#            height and width 
#            text property  

ttk.LabelFrame(root, height = 100, width = 200, text = 'My Frame').pack()

root.mainloop()
