#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

# imported regular Tkinter package 
from tkinter import *

# the themed ttk module, 
from tkinter import ttk        

# created my top logo window.     
root = Tk()

# created two themed buttons named button one and button two, 
# text button1 and button1  

button1 = ttk.Button(root, text = 'Button 1')
button2 = ttk.Button(root, text = 'Button 2')      
button1.pack()
button2.pack()

# create the style - create a style object. 
#    use ttk style constructor method & store style object 
#    in variable called style.
style = ttk.Style()

# view the styles available on your system, 
# use the style theme names method.     
# returns the list of all the available themes on the system. 
# i.e. system has a theme called the wind native, 
#      clan, alt, default, classic, vista, and xpnative. 
print(style.theme_names())

# theme system is currently using use the theme_use method
#    called without any parameters.
print(style.theme_use())

# change the theme used, 
#    use theme_use method & pass in a string of theme name 
#        'classic' theme. 
style.theme_use('classic')

# return back to that vista theme.
# style.theme_use('vista')


# selecting a theme, you're modifying the default styles for each 
# of the widgets to have a similar appearance. 

# each of these widget styles have a specific name to refer to  

# The names for widget styles typically follow the convention of 
#  placing a capital T in front of the widget's name. 
#    i.e. Tbutton is the default style for the button 
#         Tframe is the default style for frames. 

#    few exceptions to this standard: style for Treeview only has one T 
#        just Treeview, not T Treeview.

# Unlike the widgets constructor method, 
#    the style for the Panedwindow only uses a lowercase w. 

# widgets that have a horizontal and vertical orientation option 
#    have a separate style defined for each. 
#    styles named 
#        horizontal.widgetname or 
#        vertical.widgetname 
#    depending on the orientation. 

# find out the name of the default style that a widget uses 
#    call winfo class method on an object. 
#        button1.winfo_class() no parameters.
#    as expected, I use Tbutton style as its default style. 

print(button1.winfo_class())


# configure T button style to change the look of all the buttons in our program, 
#    use style object created earlier call the configure method. 
#        pass in 1st parameter the name of the style I want to configure. 
#        pass a string with T button 
#    can change one or more properties about that style. 
#        change the foreground property which changes text color = blue
# it should change the text on both of my buttons to be blue 
#   because they're both using the T button style. 

style.configure('TButton', foreground = 'blue')


# reate customs styles derived from other existing styles.
#    create a custom button style for an alarm button 
#        bold so the user can easily find it on the interface. 
#        use  style.configure command. 
#            define a new style name in the form of 
#            new-name.existing-style-name which is going to be             
#      derived from: 'Alarm.TButton'
#    additional properties to configure. 
#        foreground = orange 
#        font = Arial, 
#        size = 24
#        bold. 
# all the other existing properties from the T button will 
# be inherited into my new alarm dot T button style.
style.configure('Alarm.TButton', foreground = 'orange',
                font = ('Arial', 24, 'bold'))

# use the custom style configured the 
# style property of the widget object:
#    button two, call the config method set the style property 
#     to string 'alarm.Tbutton. 
button2.configure(style = 'Alarm.TButton')


# to modify my alarm button to look 
#    pink when pressed and 
#    grey when it's disabled
# map to the alarm style. 
# call style.map. 

#  specify style to be mapped "alarm.Tbutton" style.     
#  changing the foreground on this style. 
#    for the map function, each of the properties to be configuring, 
#       pass a list of list. 
#    Each of those lists inside the list of list, contains 
# a pair of the state in value for that property.

# can pass as many as different state and property value pairs 
#   and the foreground will be changed according to the state 
# that the buttons in. 

style.map('Alarm.TButton', foreground = [('pressed', 'pink'),
                                         ('disabled', 'grey')])

# can disable the button by using the state command. 
#    the text is grey. 
# button2.state(['disabled'])


# the layout method 
# Each Tk style is composed of one or more elements.
#    see what those elements are that composed of a specific style, 

#    call style.layout and pass it the name of a style
#        use the Tbutton 
#    it will give me back a list of all of the elements within that style. 

#    The output from this layout method can be a little tricky to interpret at first. 
#    there are four elements that composed a button and they exist in a hierarchy. 
#        The top level button element will represent the border around the widget.

#    The focus element: the part that changes color when the widget has input focus. 
#    The padding element used to space things out. 
#    The label element contains the button text indoor image. 

#    Each of these elements has "sticky" attributes 
#      set to north, south, east, west - 
#     means that the element will expand in all four directions 
#     to fill the space around it. 

print(style.layout('TButton'))

# element_options method on the style object
# see what configuration options are available for each of these 
#     four elements,
#     pass in the name of the element we want to look at. 
#     i.e button.label item returns the list of all the options 
#     that are available for that element. 

# see the options that are available for elements of any widget 
#    so we can fully customize their appearance with custom styles. 
#        i.e. elements that make up a button.
#        Other widget types will be comprised of different elements             
# with different associated element options.

print(style.element_options('Button.label'))


# use the look up method:
#    see what values have been configured to one of those options 
#        for a specific style.  
#    call style.lookup 
#        pass in the name of a style or T button
#        pass in the name of a property that looks like a Tbutton                 
#        foreground property
#     it will return to current value of that property which is blue.
#        that's what we configured earlier. 
        
print(style.lookup('TButton', 'foreground'))

root.mainloop()
