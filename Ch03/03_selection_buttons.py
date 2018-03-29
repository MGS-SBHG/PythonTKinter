#!/usr/bin/python3
# selection_buttons.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

# import the tkinter package
from tkinter import *
# import themed TK module,
from tkinter import ttk        

# create top-level root window using the Tk constructor method.    
root = Tk()

# creating a check button. 
#    use the ttk module and call the check button constructor method. 
#    first parameter is the parent i.e. the top-level window "root'
#    set the text property to say "spam."
checkbutton = ttk.Checkbutton(root, text = 'SPAM?')

# To display the check button on the window 
# use pack geometry manager - the pack method.
checkbutton.pack()

#To create a string variable  
#    call the string var constructor method, 
#    save it to a variable called "spam."   
spam = StringVar()

#    set the value of this variable, use the set method on spam, 
#        pass in a string - "spam" with an exclamation point. 
spam.set('SPAM!')

#    to check what the current value of a variable: use the get method. 
#    this will return the string that's stored within that spam variable. 
print(spam.get())

# checkbutton dot config. 
#    set the variable property to be the name of that variable = spam. 
#    default the check button values 1 - selected; 0 not selected 
#        and it will assign that to the variable spam. 
#    doesn't make sense with the meaning of spam: 
#        can actually specify an on value and off value be assigned to the variable, 
#    depending on whether the check button is selected or not selected. 
#    checkbutton selected, set spam = "spam please," 
#     not selected spam = "boo spam." 

checkbutton.config(variable = spam, onvalue = 'SPAM Please!',
		   offvalue = 'Boo SPAM!')
# look at the value of my spam variable by using the get method
if (checkbutton.state() == 1):
    print(spam.get())
elif(checkbutton.state() == 0):
    print(spam.get())        

# what makes check buttons and radio buttons unique 
# they can also store a value.

# make a variable called breakfast and create a string var to assign to it
breakfast = StringVar()

# create radio buttons
# use the ttk module, 
#    call the radio button constructor method. 
#        Pass in the parent = root. 
#        Set the text for that radio button. "spam." 
#    Configure variable associated with that radio button. 
#         variable = breakfast. 
#    specify value assigned to that variable if this radio button is selected.
#         value = SPAM'.
#    call the pack method on this call to the constructor method. 
#        constructor method call will return the object, 
#        the pack method will be called directly on that object. 
# Each radio buttons is its own object - all tied together by that common variable 
ttk.Radiobutton(root, text = 'SPAM', variable = breakfast,
		value = 'SPAM').pack()
ttk.Radiobutton(root, text = 'Eggs', variable = breakfast,
		value = 'Eggs').pack()
ttk.Radiobutton(root, text = 'Sausage', variable = breakfast,
		value = 'Sausage').pack()
ttk.Radiobutton(root, text = 'Cereal', variable = breakfast,
        value = 'Cereal').pack()
        
        
# if I select spam, since two of the radio buttons are associated 
# with the spam value - by selecting one they will both be selected.         
ttk.Radiobutton(root, text = 'SPAM', variable = breakfast,
		value = 'SPAM').pack()
        
# use the get method on that variable to get the value.         
print(breakfast.get()) # Note: value will be empty if no selection is made


# text variable property
# Assign the text variable property to a string var 
# can update the text of a label or button 
# by just changing the value of that variable.
# modify the check button object to use the text variable property
# the value of my check button is going to represent 
# whatever the value of my breakfast variable is.
# As I choose different items for breakfast, 
# that check button will change its text. 
checkbutton.config(textvariable = breakfast)

root.mainloop()
