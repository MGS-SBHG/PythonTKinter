#!/usr/bin/python3
# progressbar_scale.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

# import the TK inter package 
from tkinter import *
# import the themed TK module. 
from tkinter import ttk        

# created my top level of root window.    
root = Tk()


# wehn pgm takes significant amount of time to perform an operation,  
# provide feedback to your user regarding the progress of that task. 
# The progress bar widget provides a familiar looking linear progress bar 
# themed to match the standard look of your operating system. 
# how to configure the progress bar to provide the user feedback 
# for task that you can estimate the remaining time for. 
# for task that may continue to run for an indeterminate amount of time. 

# To create a progress bar, 
# call the ttk.Progressbar constructor method.
# pass in the root as the parent widget. 
#    configure two properties. 
#    first: the orient property, 
#      two possible options, 
#      vertical or horizontal - how that bar is going to be oriented. The most common one is horizontal, 
#      in all capitals. 
#    second property: the length = 200. 
#      length specifies the number of pixels in the longest direction. 
#       if it's a horizontal bar - X direction, 
#       if it's a vertical bat - Y direction.
progressbar = ttk.Progressbar(root, orient = HORIZONTAL, length = 200)

# use the pack method to add it to my window 
progressbar.pack()

# two modes that the progress bar can use. 
#    Determinate and indeterminate. 
# the determinate mode: 
#    If you know how many steps the operation your tracking will take, and can calculate its progress, 
#    will allow you to manually update the value of the progress bar to represent how many steps are left. 
# the indeterminate mode:
#    If you cannot determine how much more time might remain for an operation
#    will just show the activity is still taking place without specifying the time that remains. 

# configure the progress bar for indeterminate mode, 
#    use the config method, 
#    set the mode property to be the string 'indeterminate'
progressbar.config(mode = 'indeterminate')

# use the start and stop methods to basically 
# turn on and off the progress bar. 
progressbar.start()
progressbar.stop()


# using determinate mode:
#    If you know how many steps are involved in the operation 
# you're displaying a progress bar for, 
#    and you can determine how many other steps have been completed, 
#    will give your user more information. 
# two other properties to configure. 
#    1. maximum - the number of steps in the task you're performing. 
#        The default for maximum is 100. 
#        set it to 11; there's 11 steps in this task. 
#        set value - which is our current progress along that task.
#        both maximum and value are float type values. 

progressbar.config(mode = 'determinate', maximum = 11.0, value = 4.2)

# can update value of progress bar configure value property. 
progressbar.config(value = 8.0)

# Call the step function on the progress bar object. 
#    without any parameters increases the value of the progress bar by one.
#        So now the progress bar just went from eight to nine. 
progressbar.step()

# with parameter = number by which to increment the value.  
#      If I increment my step by five, exceed the maximum of 11;  
#       the progress bar wraps back around.
#        So now the value is set at three. 
progressbar.step(5)

# create a variable called value
#        as a double variable, 
#        the value is stored as a double. 
value = DoubleVar()

# To configure the progress bar to look to that double variable,
# configure the variable property to be that value variable.
progressbar.config(variable = value)


# the scale widget input  allows the user to select the value from within a range 
# by moving a marker along a linear slide bar.
# i.e. volume and brightness controls. 

# create a scale widget to control the value of the double variable. 
# To create a scale, 
#    use the theme TK scale constructor, 
#        first parameter is the root window.
#        orient parameter functions same as progress bar. 
#        a horizontal bar. 
#        the length = 400 - to the number of pixels wide to make the bar.             set a variable = value, just like we saw with the progress bar. 
#        set two parameters 
#            from_ = 0.0
#        and to = 11.0
#        specify the minimum and maximum range of this scale. 

scale = ttk.Scale(root, orient = HORIZONTAL,
		  length = 400, variable = value,
		  from_ = 0.0, to = 11.0)
# add the scale to my window by using the pack geometry manager 
scale.pack()

# programmatically move the scale slider by using 
# the set method to change the value of that value variable. 
# set it to 4.2, 
scale.set(4.2)

# use the get method to programmatically retrieve the value of it. 
print(scale.get())

root.mainloop()
