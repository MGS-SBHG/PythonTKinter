#!/usr/bin/python3
# canvas.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

# The Canvas widget 
#    gives you space on which to draw and organize various shapes, 
# images and even other widgets. 
# Its power and flexibility make it suitable for all sorts of tasks. 
# From creating a basic drawing space, or displaying a diagram, 
# to building your own custom widgets with a unique look and feel.

# the Canvas is not one of the themed Tk widgets, 
# only need to import the tkinter package. 
from tkinter import *
from tkinter import ttk        

# create my top level Tk window using the constructor method     
root = Tk()

# create a Canvas use the Canvas constructor method. 
#    pass it that top level window as the parent
canvas = Canvas(root)

# use the pack method to put my canvas in the window. 
# By default the canvas is just a blank area of this size. 
canvas.pack()

# specify the size of the canvas by configuring the width and height properties.
#    set the width of my canvas to be 640; the height to be 480. 
#       both of these values are represented in pixels. 
canvas.config(width = 640, height = 480)

# create a line and save it to a variable called "line". 
#    canvas.create_line method. 
#    several parameters
#        1st X,Y pairs of coordinates for the line.
#                begin at point 160, 360, 
#        2nd X, Y pair of pixels
#                end point 480 by 120. 
#            pixels are referenced from the top left corner of the Canvas.
#        set the fill property of my line to make my line blue 
#        width of the line - change how thick it is. 5 pixels wide.
# this created a line with the start being 160 by 360 pixels, 
# from the top left corner, and than 480 by 120 pixels down is where it ended.
# variable "line" stores create method returned ID used to reference that item
# later to make changes 
# can use that stored ID with the Canvases item configure method 
# to modify the properties about the line. 

line = canvas.create_line(160, 360, 480, 120, fill = 'blue', width = 5)


# to change the color of the line with the item configure method.     
#    Pass in the line object itself, 
#    then specifying the property I want to change. 
#    the fill property set that line to be green.
canvas.itemconfigure(line, fill = 'green')

# get the coordinates associated with the line by using the 
#    canvase.cords method. pass in that line object 
#    it will return a list of the coordinates associated with that line.
print(canvas.coords(line))

# pass coordinates to that cords method to change the coordinates of the line. 
# call canvas.cords specify the line object I want to change, 
#    pass in new set of coordinates for the line. 
#        start this line at 0,0. 
#        add coordinates 320, 240. 
#        add multiple sets of coordinates to the point 640, 0
# draws a line going from the top left corner from the center of the Canvas up to the top right. 
canvas.coords(line, 0, 0, 320, 240, 640, 0)

# configuration option: smooth them out. 
#    call canvas.item configure method
#        specify the line I want to smooth
#        configure smooth property = true 
#causes the Canvas to draw multiple line segments 
# in order to create a smooth appearance of the line.
canvas.itemconfigure(line, smooth = True)

# configure the spline steps property
#    control how many lines segments it uses to try represent this line  
#    item configure method set the splines step property to 5. 
#        draws that line using five steps to try and smooth it out. 
#    with five spline steps it still looks pretty rough. 
canvas.itemconfigure(line, splinesteps = 5)

# upping our spline steps to something larger = 100. 
# fairly smooth looking line. 
canvas.itemconfigure(line, splinesteps = 100)

# Canvases delete method
#    done using an item on the Canvas - delete it,   
#    passing in that object to delete
# use the "all" keyword to completely clear the Canvas 
canvas.delete(line)

#  draw a rectangle on the canvas
#    canvas.create_rectangle 
#        4 different perimeters x, y pairs of coordinates 
#            for the two opposite corners of the rectangle. 
#        160 and 120 one corner of my rectangle 
#        480 and 360 other corner of my rectangle. 
# method creates the rectangle object and stored a variable. 

rect = canvas.create_rectangle(160, 120, 480, 360)

#configure properties of that object by using the item configure method.
#    1st perameter: the object to configure. 
#    fill property: change rectangle to yellow. 
canvas.itemconfigure(rect, fill = 'yellow')

# the oval:
#    using create_oval method of the canvas object. 
#    The oval takes a similar set of perimeters as what we saw with the rectangle. 
#    define a bounding box around that oval by defining the top left 
#    and bottom right corners of the oval; draw an oval within that.
#    use that same set of points that we used for the rectangle 
#        define an oval that stays exactly inside of that rectangular area. 
#    did not specify a fill, the yellow box is visible through the oval. 

oval = canvas.create_oval(160, 120, 480, 360)

# an arc:     
#    use canvas.create_arc method. 
#        parameters passed to the arc method 
#            same as oval and rectangle methods. 
#        defining the area in which we will draw specific piece of             that oval.
#    By default, draw from 0 to 90 degrees. 
#    coordinates: 160, 1  1st x and y coordinates 
#    2nd set of x, y coordinates, use 480 by 240. 

#can configure where my arc starts and ends by using the 
#    item.configure method 
#    change the start and extent properties.

#    canvas.itemconfigure 
#        pass arc item 
#        start = 0  my arc start at zero degrees 
#        extent property = 180  for a 180 degrees. 
#        fill = green. 
# have a green arc which extends from zero to 180 degrees. 
arc = canvas.create_arc(160, 1, 480, 240)
canvas.itemconfigure(arc, start = 0, extent = 180, fill = 'green')


# draw polygons on the canvas: 
#    define the individual points along the item.
#    canvas.create_polygon method. 
#        pass in a series of x, y coordinates defining the points along that polygon. 
#        draw a triangle 
#            1st coordinate pair 160 by 360. 
#            2nd coordinate pair 320 by 480. 
#            3rd coordinate pair 480 by 360. 
#        fill = color blue. 
# can add as many of these x, y coordinate pairs as you want to for the vertices of the polygon.

# similar to creating a line segment in which we saw we could add multiple x, y pairs if we wanted to, except that it also connects to beginning and end pairs. 

# three points created a single triangle; a closed shape, 
# can also use the fill property to add color to it.

poly = canvas.create_polygon(160, 360, 320, 480, 480, 360, fill = 'blue')


# add text to the canvas 
#    use the canvas.create_text method.
#        1st two parameters the x and y coordinates of which I place the text and those will be the center of where the text is located. 
#            coordinates 320 by 240 
#        define the text to put there by using the text property. 
#            the word "Python" 
#        font property: Courier font, size 32, bold

text = canvas.create_text(320, 240, text = 'Python', font = ('Courier', 32, 'bold'))

# add an image to my canvas, 
#    create an image object using the photo image constructor method.
#        pass in the path to my gift file and it's created the photo image object 
#        store it in a variable called logo. 
logo = PhotoImage(file = 'python_logo.gif') # Change path as needed

# use  canvas.create_image method to create the image. 
#     pass in the coordinates in which I want to place the image.
#            represent the center of where the image will be placed.
#    specify the image property to be that logo file we just created.           
#          Python logo. 

image = canvas.create_image(320, 240, image = logo)

# Items are added to the canvas in the order that they're created 
# with the most recently created items being on top.
# can modify their order after created using: the lift and lower methods.

# use the lift method on the text item to raise it. 
#    call canvas.lift 
#        pass in that text item which I stored in a test variable 
#    this raises up the very top position within my stack of items 
# on the canvas.  
canvas.lift(text)

# use the lower method to move the image down in the stack. 
#    call canvas.lower 
#        pass in that image
#    it actually pushes that image all the way down below all the objects 
# including the rectangle in the stock so we can no longer see it.
canvas.lower(image)

# use the lower method with an additional perimeter of text 
# to specify that we want to lower that image just below the text item. 
#    call canvas.lower, I say I want to lower the image 
# and I can also specify to where I want to lower - text 
#    it will put the image at the position just below the text object. 
canvas.lower(image, text)

# add to the canvas include other Tk widgets.

# create a button using the button constructor method 
#    make it a child of the canvas, 
#    text =  "click me" 

button = Button(canvas, text = 'Click Me')

# can add it to the canvas by using the canvas.create_window method. 
#    pass in the coordinates of where I want to place that button. 
#         at 320 by 60. 
#    set the window perimeter to be that button object. 

canvas.create_window(320, 60, window = button)


# to reference multiple items at once, 
#    create tags - to use as custom identifiers when you attach to a canvas item. 
#    Each canvas item can have multiple tags 
#    the same tag can be used by multiple canvas items.
# an easy way to logically group and modify multiple items at the same time. 

#    Any methods which use item IDs as parameters can also accept a tag instead of the items ID. 
#    This allows us to execute the method on all items having that specific tag at the same time. 
#    add tags to items after creation by using the item configure method.

# a rectangle - a single tag 
#    call canvas.item configure specify my rectangle object
#        pass ID 'rect' 
#        set the tag's property - "shape".
#            a list of strings for the tags to apply to that item.                 
              
canvas.itemconfigure(rect, tags = ('shape'))


# for oval - multiple tags
#        call canvas.itemconfigure 
#            pass in 'oval' identifier
#            tag's property to "shape"; oval is "round"

canvas.itemconfigure(oval, tags = ('shape', 'round'))

# create tags to reference groups of items at the same time. 
#    call canvas.itemconfigure with "shape", 
#        change the fill color for both the oval and the rectangle at the same time to grey. 
canvas.itemconfigure('shape', fill = 'grey')


# get a list of all the tags that are associated with an item, 
#    use the canvas.gettags method and pass in the name of that item. 
#        "oval"
#    returns all of the tags associated with the oval 
# it has both the shape tag and the round tag associated with it

print(canvas.gettags(oval))

root.mainloop()
