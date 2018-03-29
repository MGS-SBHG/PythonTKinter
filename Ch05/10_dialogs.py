#!/usr/bin/python3
# dialogs.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

# To use the message box, 
# import the message box module from the TKinter package. 
from tkinter import messagebox

# create a message box by typing 
#    messagebox.show info. 
#        pass in two parameters
#        1 the title. "a friendly message"
#        2 the message to be contained within that window. 
#            message = "hello TKinter". 
# it creates a pop-up window. 
# Even though the message box is not a new TK widget, 
# the TK module still creates a new TK root window in the background. 

messagebox.showinfo(title = "A Friendly Message", message = 'Hello, Tkinter!')


# Message boxes are also modal. 
#    If I bring back up Idle, you'll see that it's waiting on execution.        
#    Modal means that the execution to your program will be paused 
#     until the user has responded to the message box. 
#    You respond to the message box by clicking OK. 

# Three variations of the message box which can be used to deliver information to the user. 
#    showinfo message box  
#    showwarning message box 
#    showerror message box
 
# each generate a pop-up window with a specified title in-text, 
# and only give the user the option to acknowledge the message with an OK button.

# each play a different sound and display a different icon to alert 
# the user of the severity of the message. 

# create message boxes which gather a simple yes or no type response from the user. 
#    the ask yes/no message box. 
#    pass in a title "Is the user hungry?" 
#    pass in the message "Do you want spam?" 
# when I execute this window, you see it gives me a message box with two options.
# The ability to click a yes or no button. 
#    If the user gives the positive response, then the dialogue box will return a true value to the program. 
#    If the user gives a negative response, it'll return false. 

print(messagebox.askyesno(title = 'Hungry?', message = 'Do you want SPAM?'))


# use the file dialogue method:
#    prompt the user to browse for a file or dialogue path 
#    import the file dialogue module from the TKinter package, 
from tkinter import filedialog

# create a file dialogue:
# askopenfile method returns an IO object containing the file name 
# the name filed is  saved to a variable called "filename"
# it creates the standard pop-up open file dialogue.
filename = filedialog.askopenfile()

# display filename:
print(filename.name)



# the color chooser. import the color chooser
from tkinter import colorchooser

# create a color chooser 
#    colorchooser.askcolor. 
#        several properties can set 
#            1. initial color - the color that the color chooser is initially set to show. 
#    # hex value as a string FFFFFF, the color white. 

# the color chooser created by default shows white color 
#     can go in and select any other color I want to.

# i.e. select blue. hit OK, the color chooser returns a list with two items. 
#    1st item in that list is a list containing the RGB, or red, green, and blue values of the color that was selected. 
#    2nd item in the list is a string containing the hex representation of the color that was selected. 
# i.e. ((94.3671875, 255.99609375, 255.99609375), '#5effff')

# if the user cancels the color chooser dialogue without selecting a color, still return to two element list;
#     BOTH of those elements will be empty. 
# i.e. (None, None)
#    important that you check for that case to avoid running into errors later in your program.

print(colorchooser.askcolor(initialcolor = "#FFFFFF"))

