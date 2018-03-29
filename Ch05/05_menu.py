#!/usr/bin/python3
# menu.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

# cascading/dropdown menus

# import the tkinter package. 
from tkinter import *
 
from tkinter import ttk        

# create my top-level root window with the Tk constructor.    
root = Tk()

# When using menus, configure a second option with the root menu, 
# using the root.option_add method.
#    tells the Tk menu to not create a tearable menu. 
#    If we don't do this then each of the menus in our interface will have a dash line at the top which allows it to be torn off. 
#    Tkinter defaults to using tearoff menus because of legacy and maintaining backwards compatability with its original look and feel
#    tearoff menus are not part of modern GUIs
#    include this line in your code before you start creating your menus.

root.option_add('*tearOff', False)

# reate the menu, 
# save it in a variable called "menubar" by using the menu constructor method,
# and passing it the root window as its parent.
menubar = Menu(root)

# add menu bar to the root window by configuring the root window 
# itself to use that menu item as its menu. 
#    Use the config method and set the menu property to that menu bar object 
#     just created. 
#    The menu is currently empty, 
root.config(menu = menubar)

# add some new menu items. 
#    Each menu item will be a new menu object which is a child of 
#    this menu bar object we just created.

# create one object called "file". 
#    use the menu constructor and pass it menu bar as the parent. 

#create another one called "edit". 
#    use the menu bar constructor with the menu parent. 

#create "help_" 
#    help with an underscore, 
#    help without the underscore is a keyword in Python, 
#    pass it menubar as the parent. 
file = Menu(menubar)
edit = Menu(menubar)
help_ = Menu(menubar)

# To add the menu objects just created to the parent menu bar,
#    use the add_cascade method on the menubar object.
#    the underscore in the name. 

#specify the menu that we want to add to the menu property. 
#    add that menu created and called "file." 
#        add the name of the label we want to have with that menu.                  "file." 
#    add the menu called "edit", name "edit." 
#    add the menu called "help_", with underscore to avoid using a keyword, the label "help." 

menubar.add_cascade(menu = file, label = 'File')
menubar.add_cascade(menu = edit, label = 'Edit')
menubar.add_cascade(menu = help_, label = 'Help')

# add commands to the file menu. 
#    call the "add_command" method calling it on the file menu itself
#        not the menu bar. 
#    pass in the name of the command. "new." 
#    set the command property what function to execute when the command is 
# called. use a lambda function to call print method from a single line of 
# code.
file.add_command(label = 'New', command = lambda: print('New File'))

# add_separator method 
#    add a separator line between menu elements 
file.add_separator()

# create open command - "open file." 
# TK automatically takes those three periods after the open 
# and converts it to an ellipsis. 
file.add_command(label = 'Open...', command = lambda: print('Opening File...'))

# create "save." 
file.add_command(label = 'Save', command = lambda: print('Saving File...'))

# .entryconfig
#    keyboard shortcuts associated with these commands 
#    notate them on the menu by setting the accelerator property 
#        to the text of the shortcut. 
#        "Control+N"  a common shortcut for creating a new file. 
#       displays "Control.N" next to the new line. 
#        this does not actually set up that keyboard command, 
#  or create that keybinding in event binding section 
#  - how to create those sort of shortcuts
file.entryconfig('New', accelerator = 'Ctrl+N')

# Menu commands similar to buttons - have images added next to them. 
#    create a photo image object stored in the variable called logo 
#    use the photo image constructor method 
#    pass in the file path to my python_logo.gif. 
#    use the subsample method to shrink it down to a 10th of its original size. 
#    add to file menu by using the entry config method.
logo = PhotoImage(file = 'python_logo.gif').subsample(10, 10)


# configure open menu item, 
#    configure the image property to point to that logo. 
#    set the compound = 'left' property 
#        like buttons and labels 
#        it will place that logo to the left of the text for that             entry. 
#    my Python logo to the left of my open text. 
file.entryconfig('Open...', image = logo, compound = 'left')


# menu entries can be enabled or disabled by configuring 
# the state property using that entry config method.

# configure the state of the open entry 
#pass in the name of the entry
# set this state to be disabled. 
#    it's disabled, grayed out; the user can't select it from the menu. 
file.entryconfig('Open...', state = 'disabled')

# add other menus effectively creating sub-menus. 
#    create a save sub-menu containing commands for 
# different forms of save, such as save as and save all.

# delete the current save command entry. 
#    delete a menu item using the delete method. File.delete. 
#        pass in the name of the command I want to delete 'Save'
#    save is no longer part of that menu! 
file.delete('Save')

# create a new menu object called save, 
# which will be a child of the file menu. 
save = Menu(file)

# add that to the file menu using the add cascade method 
#    menu = save, 
#    label will also be 'save'
# sub-menu w/ the little arrow to the side.
 
file.add_cascade(menu = save, label = 'Save')

# add commands to that save sub-menu by using the add command method. 
#    save.add command. save as.
#    print "Saving As." 
save.add_command(label = 'Save As',command = lambda: print('Saving As...'))

# create a command called "save all."  print "Saving All." 
save.add_command(label = 'Save All', command = lambda: print('Saving All...'))

# add radio buttons and check buttons.
# behave the same as the check button and radio button widgets. 
 


# create a variable called "choice" using the int var constructor method. 
choice = IntVar()

# add the radio buttons to my edit menu. 
# add radio button method. 
#    pass in the name for the radio button. "one." 
#    specify the variable that's associated with that radio button "choice" 
#    specify value this radio button will assign to the variable if it's selected.  value of 1 to variable choice 
# create two
# create three.
edit.add_radiobutton(label = 'One', variable = choice, value = 1)
edit.add_radiobutton(label = 'Two', variable = choice, value = 2)
edit.add_radiobutton(label = 'Three', variable = choice, value = 3)

# can use the add_check buttons menu to add check buttons 
help.add_checkbutton(root, text = 'Four')
help.add_checkbutton(root, text = 'Five')
help.add_checkbutton(root, text = 'Six')


# the post method 
#    the ability to create popup menus at a specific location on the screen  
#    useful for creating contextual, right-click-type menus. 
#        the process for capturing a right click in the later event binding section, 
#    drawing the menu at a specific location on screen. 
#        capture that location from the event handler when a right click occurs. 
#        To draw a menu on the screen we use the post method. 

# draw file menu, call file.post & pass the x y coordinates                 of where to draw the menu.
#    create a popup menu at 400 by 300 pixels. 
#    400 pixels in the x direction from the left of the screen, 
#    300 pixels in the y direction, downwards. 
#    These coordinates are in relation to the entire screen, 
#    not just in relation to the TK window 
file.post(400, 300)

root.mainloop()
