#!/usr/bin/python3
# toplevel.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

# import the tkinter module using the from tkinter package command.
# Not going to import the themed TTK module, 
# because top level windows are not part of the themed widget set. 
from tkinter import *      

# use the Tk constructor method to create my root top-level window.     
root = Tk()

# create a second top-level window with top-level window constructor. 
#    T is capitalized; the L is lowercase. 
#    a child of that original root window; 
#        set variable called "window."
# this new window is a separate entity. 
#    It can contain its own children widgets, which it will geometry manage separately, 
#    it is still a slave to that root top-level window because we specified the root window as its parent. 
window = Toplevel(root)

# use the title method and pass in a string of the new title 
# we want for that window. call it my "New Window." 
# My new window says "New Window" in the title bar. 
window.title('New Window')

# call the lower method will send it down to the very bottom 
# of the stack of all of my windows.
# optional parameter to the lift and lower methods, 
# of another window will lift or lower that window to be just above or below the window which I pass as a parameter.
window.lower()

# If I call window.lift(root) will lift this window to be at the position 
# just above the root window.
window.lift(root)

# Make the window maximized by setting its state to "zoomed." 
window.state('zoomed')

# To hide a window we can set its state to be withdrawn. 
# the window will be hidden from the user. 
# not even visible in the taskbar. 
window.state('withdrawn')

# minimize the window so that it's still accessible in the taskbar, 
# use the iconic state. 
window.state('iconic')

# programmatically return the window out of that iconic state 
# we can set its state back to normal.
# it went back to that zoomed position, and this makes sense. 
# If you had a window fullscreen and you send it down to the taskbar, 
# you'd expect it to return to fullscreen if you select it from the taskbar 
# and deiconify it. 
window.state('normal')

# check what the current state of a window is by 
#calling that state method without any parameters. 
print(window.state())

# call the normal state on it one more time, 
# and that will return it back to its original size as we created it.
window.state('normal')


# same as calling the state method 
# with the iconic and normal parameters, respectively:

# send the window down so that it's visible in the taskbar. 
window.iconify()

# will return it back to the normal state. 
window.deiconify()

# By default an empty window is created w/ 200 by 200 pixels.
# to change the size and/or relocate the window programmatically, use
#    the geometry method. 
#        window.geometry('width x height+x+y')
#        takes one parameter, which is a string containing the new width and height in pixels of the window, 
#        as well as the new x and y location in pixels of the window's top-left corner, and that position is relative to the top left corner of the screen. 
#        The string is formatted as width in pixels, x, height in pixels, plus symbol, the x position, plus symbol, the y position.
# 640 pixels wide x 480 pixels tall. 
#    top-left corner to be 50 pixels to the right of the left edge of the screen 
#    top-left corner to be 100 pixels down from that top-left corner of the screen. 

window.geometry('640x480+50+100')

print(window.geometry())


# control whether or not we'll allow the user to be able to resize
# two parameters both booleans, 
#        representing whether or not it's resizable in the x and in the y direction. 
#        1st parameter controls whether/not resizable in x direction,
#        2nd parameter controls y direction.
# both of those to false:
#     I can no longer click and drag on the edge or corner of the window to resize it. 
window.resizable(False, False)

# Maxsize takes two parameters, 
#    the x value in pixels and the y value in pixels - 
# maximum allowable size of that window. 
window.maxsize(640, 480)

# Min size method parameters of 
# the minimum x and y value in pixels want the window to be.
window.minsize(200, 200)

# let my window be resizable again by calling the resizable method 
# with true in both directions. 
window.resizable(True, True)


# The destroy method 
#    can be used on all kinds of widgets, not just windows, to delete them. 
#    will also destroy all child widgets. 
#    If I use the destroy method on my new window, 
#        it will only delete the new window and any widgets contained within it.
#    If I use that destroy method on my top level root window, 
#        it will also destroy my new window, 
#   because the new window is a child of that top level window. 

# destroy that top level root window, and call it with zero parameters.
root.destroy()

root.mainloop()
