#!/usr/bin/python3
# panedwindow.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

# the paned window: 
#  new type of widget which can be used to split up sections of the user
#  interface, 
#  a geometry-management widget which can hold other widgets by stacking 
#    the vertically or horizontally. 
#  displays a divider between each of the widgets, which the user can click 
#  and drag to adjust the relative size of the widgets within the window.
# Although any type of widget can be added to the pane window, 
# it's commonly used to hold several frames next to each other,
# to allow the user to easily resize them. 

# import the Tkinter module, 
from tkinter import *
# import the theme TTK module, 
from tkinter import ttk        

# create my root top-level window.    
root = Tk()

# create a new paned window 
# use the paned window constructor method found in the TTK themed module. 
#    "Panedwindow" is spelled with a capital P, but the W is still lower-case. 
#    1st parameter parent of that widget I'm creating, 
#    a parameter for "orient." 
#        two options for "orient" are VERTICAL or HORIZONTAL
#        These represent how the widgets added to the pane will be stacked next to each other. 
#            vertical option will stack the panes on top of each other, 
#            horizontal option will put the panes next to each other. 
#    select horizontal using all caps. 

panedwindow = ttk.Panedwindow(root, orient = HORIZONTAL)

# To add that paned window to my top-level window, 
# use the pack manager
#    add a few properties 
#        this paned window to expand to fill the entire space inside of the top-level window, 
#            set the "fill" property to "both,"     
#            expand if that window is changed in size.

panedwindow.pack(fill = BOTH, expand = True)

# create some new frames to add to the paned window. 
#    first frame save in a variable called "frame1." 
#        frame a child of the paned window by parsing the paned window as the first parameter to the frame constructor method. 
#    set the width of that frame to be 100, 
#    the height of that frame to be 300 pixels.
#    its relief will be set to "sunken."    
frame1 = ttk.Frame(panedwindow, width = 100, height = 300, relief = SUNKEN)

# second frame called "frame2" 
#   a child of the paned window, 
#   change its width to be 400, 
#   as its height.
frame2 = ttk.Frame(panedwindow, width = 400, height = 400, relief = SUNKEN)

# add those frames to the paned window, 
#    use the paned window's add method. 
#        first parameter for the add method is the widget we want to add "frame1" 
#        the second parameter: set a property called "weight." 
#            The "weight" property specifies how much the frame                 will be scaled when the paned window is resized.
#            set weight for "frame1" =1 ,
#  "add" method on the paned window adds new widgets to the paned window 
# to the right of existing widgets here in the horizontal orientation.
panedwindow.add(frame1, weight = 1)

# configure the "frame2" weight = 4. 
# This means if I expand this window, "frame2" will be 
# expanded at four times the rate of "frame1." 
panedwindow.add(frame2, weight = 4)

# create a third frame to add to my paned window. 
# frame number three. 
#    a child of the paned window. 
#    width = 50 
#    relief = "sunken" 
frame3 = ttk.Frame(panedwindow, width = 50, height = 50, relief = SUNKEN)

# add the new frame or widget to a specific location within that paned window,     use the "insert" method 
#     two parameters.     
#        1st parameter: the index at which to insert the new widget,
#            indexes start with a 0 index on the left-most widget
#                          then go, one, two etc.  
#        index = 1  insert a new widget between the zeroth and first index;the new widget at the first index.
#        2nd parameter: the widget to insert - frame3.
#        By default, frame is going to have a weight = 0;
#        if I resize this window, it's not going to be resized at all. 
#        It will always remain as 50 pixels wide. 

#    the user can select the little sashes here, 
# to manually resize the windows as they deem fit, 
# and once they've resized that, since it has a weight of zero, 
# it'll maintain whatever size it has as the window is changed.

panedwindow.insert(1, frame3)


# "forget" method
#    to remove one of the widgets from the paned window, 
#    1 parameter - the index of the widget to forget. 
#        the frame at position 1, call "forget 1." 

#    that frame disappeared from my pane window. 
#    this does not destroy the frame. 
#    It still exists in the background. 
#    That widget's still alive, 

# panedwindow.forget(1)

root.mainloop()
