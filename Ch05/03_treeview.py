#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

# Hierarchical Treeview:

# The tree view widget 
#    used to display a list of items that the user can interact with and make selections from. 
#    a single level or 
#    part of a multi-tiered hierarchy. 
    
# imported my TKinter package     
from tkinter import *

# the themed TK module
from tkinter import ttk        
    
# created a root window using the TK constructor method.     
root = Tk()

# create my tree view and store it in a variable called tree view
#    use the TK tree view constructor method 
#    pass it the root as the parent.
treeview = ttk.Treeview(root)

# add the tree view to my root window using the pack command. 
treeview.pack()


# the tree view is created currently empty. 
# To use it, you need to add one or more items to the tree. 
#    Each item represents a node in the tree and can be referenced by a unique item name or ID. 
#        item names and ID's can be chosen by the programer at the time when the item is created OR 
#        TKinter will automatically generate a unique ID itself. 

#call the insert method on the tree view object.
#    To insert an item into the tree, 
#    1st parameter: parent node of the new item I want to create. 
#        since my tree doesn't currently have anything in here, the tree view widget does automatically create a root node which gives the special ID of empty string. 
#        use that for this first item I'm adding. 
#    2nd parameter: the position in the list under the parent node in which to insert the new item. 
#    insert it at the zeroth position. 
#    3rd parameter: item's ID. - choose what I want to call this item;              "item1"
#    4th parameter set the text property to say "First Item". 
#        optional; don't have to do that. 

# can add more items under this tree view. use the insert method again. 
#    add another item under that root node of empty string. 
#    going to add at position one. 
#    item two. 
#    text "second item".

# add a third item under that same node. 
#    instead of using a zero, one, two, three, use the "end" keyword 
#        it will add it at the end of all of the items within that level of the hierarchy. 
#    call item3 
#    text property "third item". 

# So now we have three items within our field. 
# They're all on the same level because they all exist under that top level, no name root node.

treeview.insert('', '0', 'item1', text = 'First Item')
treeview.insert('', '1', 'item2', text = 'Second Item')
treeview.insert('', 'end', 'item3', text = 'Third Item')

# Add images next to the text of the items:
#    bring an image into my TKinter program with the photo image constructor method 
#    Pass in the path to my Python logo.gif 
#    since that Python logo .gif file is so large, use the sub sample method that we previously saw to shrink it down by a tenth of its size in the X and Y direction. 
#    insert a new item into my tree view, 
#        insert it as a sub item under item number two by passing in item two's node name 
#        insert it at the end of all of the items that are under there. 
#        name 'python'. name of the node. 
#        text property specifying what text that node will contain. 
#            'Python' 
#        set the image property = logo, the photo image object we just created. 

logo = PhotoImage(file = 'python_logo.gif').subsample(10,10)
treeview.insert('item2', 'end', 'python', text = 'Python', image = logo)


# the tree view config:     
#    When I execute that you notice now the second item, or item number two here, has a little plus sign, and that's because our new item just got placed under it in the tree view.
#    And you can see that small little Python icon next to the text. I'm going to change the height of my tree view widget to be a little bit smaller, because it is large for the number of items we have in there. 
#    change the height property to the number of entries want to display.             five; my tree view will be shrunk down so that I can display five entries at a time. 

treeview.config(height = 5)

# the move method.
#    can rearrange items in the tree view 
#    The only restriction: cannot move an item to be underneath one of its own children.
#        would create an unfortunate loop. 
#    call it on the tree view object, pass in the: 
#        1st parameter of item we want to move. 
#            'item2' 
#        2nd parameter: the new parent to move this item under. 
#            'item1'. 
#        last parameter: position under that new parent in which you want to place it. 'end' of the items under item one.
# this will take item two, move it under item one, and place it at the end of those items. And you see that when I did this, now we have everything located under item one. 

treeview.move('item2', 'item1', 'end')

# the open property:
#    By default, items in the tree view are created in the closed position. 
#    can change this by modifying the open property with the item method.         treeview.item(item I want to modify i.e. item1, open = True)

# item method - similar to the config method; used to configure the items within a tree view rather than configure properties of the tree view itself.

# When I execute that, you see it programatically opens up the hierarchy. 

treeview.item('item1', open = True)
treeview.item('item2', open = True)

# use the item method to check the status of the property for an item. 
#    call treeview.item checks the status for item one, and see what is the status of the open property. 
#        returns 1 representing true, letting me know that this tier is now opened.
print(treeview.item('item1', 'open'))

# the detach command:
#    to remove an item from the tree view,     
#    pass in the name of the node that we want to detach. 
#        item3 
#    And this will remove that node from the tree view, but it still exists.
treeview.detach('item3')

# the move method
#    re-add it to the tree view
#    treeview.move 
#        1st parameter: the item to move. item3   
#        2nd parameter: the node under which we want to move item.
#            item2 
#        3rd parameter: the index of where under that item we want to                 place it. '0'

treeview.move('item3', 'item2', '0')

# delete command for the tree view, 
#    completely delete an item from the view.
#        on item3, 
#    it's removed from my view and the item disappears completely. 
#    It can Not be re-added.

treeview.delete('item3')


# To add new columns to the treeview, 
#    configure the "columns" property. 
#    "treeview"."config columns," 
#        parse the "columns" property a list of the names of the columns you want to include.
#        include one additional column called "version."
treeview.configure(column = ('version'))

# To configure the properties of a column, 
#    use the "column" method of the treeview. 
#        1st parameter: name of the column we want to modify
#            "version" column 
#        parse in one or more properties to change. 
#            change width = 50 pixels, 
#        anchor so that its contents and text are centered, 
#            anchor = "center" 

treeview.column('version', width = 50, anchor = 'center')
treeview.column('version', width = 50, anchor = 'center')

# configure the main treeview column with the "column" method 
#    refer to it with special name #0 
#        treeview.column(#0, width = 150)  
#        width of my main treeview column = 150

treeview.column('#0', width = 150)

# "heading" method 
#    configure the title to be displayed above columns 
#    treeview.heading("version", text = 'Version') 
#        parse in the name of the column that we want to configure, 
#        set "text" property to the name we want above that column. 
#        "version" column to say "Version" above it. 
        
treeview.heading('version', text = 'Version')


# the "set" method:
# configure the value contained within a slot of that column0
#    treeview.set
#    1st parameter: item on the hierarchy referencing "Python" item in my hierarchy.
#    2nd parameter: place contents into "version" column, 
#    3rd parameter: the contents to place 3.4.1. 
#        name of Python version using. 

treeview.set('python', 'version', '3.4.3')

# add tags to treeview items, to modify their properties as groups.
#         similar to what we saw with text, 
#    the canvas widgets. 
#    Tags can be added to an item at the time of creation by 
#        including the "tags" property or 
#        later by using the "item" method.

# add a tag to my Python item using the "item" method, 
#    1st parameter being "Python," referencing the item I'm going to change. 
#    set "tags" property. create a tag in here called "software." 
#        The tags property accepts a list of one or more strings 
# for the tags you want to associate with that item. 
        
treeview.item('python', tags = ('software'))

# use those tags to configure items with the "tag configure" method. 
#    1st parameter, which is the name of the tag you want to configure, 
# and then you can specify one or more properties.
#    2nd parameter: background of that tag = yellow

# the value of using tags = can have multiple items specified 
# to use the same tag, and so you can configure their property as groups.

treeview.tag_configure('software', background = 'yellow')

# determining which item in the treeview has been selected by the user:
#    The treeview widget does not support a command callback to execute code when an item is selected. 
#    Instead, you can listen to virtual events from the treeview.

# three virtual events that the treeview will produce for 
# when a selection is made and when the treeview items are opened or closed. 

# use the "bind" method to execute a callback when the selection is made. 

# define a simple callback function 
# this callback will simply print out using the treeview selection method, 
# the current item that's selected from the treeview.
def callback(event):
    print(treeview.selection())

# To configure the virtual event with the treeview, 
#    use the "bind" method, 
# parse in the name of that special treeview selection event that occurs.
# <<"TreeviewSelect">>
treeview.bind('<<TreeviewSelect>>', callback)

# Whether or not multiple items can be selected depends on the selection mode. 

# By default, the treeview uses the extended select mode, which allows for multiple items to be selected at once. 

# If I hold Control, I can click and choose multiple items. You see that the list that's returned includes strings for each of those items that were selected. 
# You can modify the select mode by setting the "select mode" property.

# "treeview"."config select mode"="browse." 
#    The "browse" select mode will allow one item to be selected at a time. 
#    If I try to hold Control and click and select multiple items, it won't let me. 

#    select mode "none." 
#        does not allow you to select any items from the tree. If I click, it won't highlight those items to show they're selected.

treeview.config(selectmode = 'browse')

# can programmatically select tree items by using 

# "selection add" method     
#        adds the specified item to the selected items. 
# add the "Python" item to be selected. 
# You notice that the previously-selected item, which was 
# "First item," still remains selected. 
print(treeview.selection_add('python'))

# "selection remove" method
#        programmatically unselect items by using the parsing 
# in the name of the item I want to unselect.
print(treeview.selection_remove('python'))

# "selection toggle" method.
#    toggle whether or not an item is selected 
# parse in the name of the item you want to select 
# and it will toggle that based on the current state of that item. 
print(treeview.selection_toggle('python'))

root.mainloop()
