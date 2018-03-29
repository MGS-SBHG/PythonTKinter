#!/usr/bin/python3
# notebook.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

# import the Tkinter package  
from tkinter import *
# import the TTK module 
from tkinter import ttk        
# create top level root window using the TK constructor.    
root = Tk()

# create a notebook 
#    use the notebook constructor, which is found inside the TTK module.             spelled with a capital N, 
#        pass in the parent of the top level root window. 
notebook = ttk.Notebook(root)

# use the pack geometry manager to add it to window. 
notebook.pack()

# create a couple frames to add to our notebook. 
#    frame one, use the frame constructor method, 
#        frame needs to be a child of the notebook 
#    frame two 
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

# add these frames to the notebook, 
#    use the add method on the notebook object. 
#        1st parameter: the frame that I want to add 
#        2nd parameter: the text, which will be the label of each tab                 in the notebook. 
#            label one        
#            label two
notebook.add(frame1, text = 'One')
notebook.add(frame2, text = 'Two')

# add a button to frame one, 
#    calling the button constructor. 
#    a child of frame number one, 
#    button text say 'click me'
# use the pack geometry manager on that button, to add it to frame one. 

ttk.Button(frame1, text = 'Click Me').pack()

 # third frame called frame3 - a child of the notebook 
frame3 = ttk.Frame(notebook)

# using the insert method: insert new notebook tags at specific locations
# call the insert method on the notebook object, 
#        1st parameter: the index at which to insert a pane into the notebook 
#            the notebook is a zero index starting in the left, 
#            the leftmost tab is the zero's tab, 
#            the next one over is the first tab etc
#                by inserting it at position one, it'll insert 
#                   it just to the right of this leftmost tab.
#        2nd parameter: the widget I want to insert: third frame widget, 
#        3rd parameter: the text to display on that notebook tab. 
#            call this "three", because it contains frame three.
notebook.insert(1, frame3, text = 'Three')

# the forget method:
#    If we don't like where we've inserted a tab, can remove it from the notebook 
#    takes one parameter: the index of the tab to remove, 
#   call forget(1) will remove that tab at position one.
#    not actually deleting that frame widget, or any of its contents, 
#    it's just removing it from the notebook. 
#    we could re-add that frame widget to another position 
# or use it elsewhere within our program. 

# notebook.forget(1)

# the add method: 
#    adding frame three back to the notebook, using 
#    set text = "three"
# it adds it at the rightmost position of the tabs in the notebook. 
#notebook.add(frame3, text='Three')

# the notebook's select method
#    to see which tab is currently selected by the user    
#    call it without any parameters will return the tab ID of the selected tab.
# notebook.select() will give us an ID of that widget. 
print(notebook.select())

# convert the result of the notebook.select() method 
# [widget id ]into a tab number. 
print(notebook.index(notebook.select()))

# programmatically select which notebook tab is selected 
#    pass the index value of that tab to the select method. 
#    call notebook.select(2)
#    causes notebook to switch over to show the second index tab. 
notebook.select(2)

# modify the properties of a notebook tab after they've been inserted 
#    use the tab method on the notebook. 
#    the state of a tab - disabled. 
#        notebook.tab, configuration of a tab.
#            1st parameter: the index of the tab I want to configure. 1 
#        tab one is grayed out, and it won't allow me to select it. 
#notebook.tab(1, state = 'disabled')

# change the state of tab one: hidden 
#        using the tab method, state equals hidden, 
#        tab one is no longer visible on the notebook, 
#        but it still does exist in the background at index 1
#notebook.tab(1, state = 'hidden')

# return the tab back to normal state, 
#      call notebook.tab change one, and set its state back to normal. 
#notebook.tab(1, state = 'normal')

# current value of a property for a specific tab
#        use tab method, 
#        1st arg: pass in the index of the tab, 
#        2nd arg: pass in the name of a property. 
#        see what the text property is for tab 1 , 
#        with the text option, and you'll see that the tab at index
#notebook.tab(1, 'text')

# call tab method without specifying a specific property, 
#    gives list of all the properties that exist for that tab. 
#notebook.tab(1)

root.mainloop()
