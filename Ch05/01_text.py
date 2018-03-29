#!/usr/bin/python3
# text.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

# Multi-line Text Widget: creates a multi-line area for text entry.

# import the Tk enter package
from tkinter import *      
# NOT import themed ttk module b/c text widget is Not a themed widget.

# create a top level window using the Tk constructor method.    
root = Tk()

#create my text widget. 
#    use the text constructor. 
#    NO ttk because it's not a themed module. 
#    pass in that root window as the parent    
#    configure two properties
#        width = 40
#        height = 10
#    of my text box. 
#    Width and height: specified in nbr of characters tall & wide 
#    text box will be.  
text = Text(root, width = 40, height = 10)

# display 40 chars wide x 10 chars tall text box
text.pack()

# control where the text box will wrap by configuring the wrap property. 
# use the config method to do that. 
# three options for wrap.    
#    char: the default option; it will wrap at the character which hits the end of the line. 
#    none:  no wrapping 
#    word:  cause the text box to wrap at the spaces between words. 
#        it no longer breaks up my words. It'll wrap at the nearest space. 

text.config(wrap = 'word')


# Get method: 
# reqs one or two input paramaters - the indices of a place in the text.
#    1 parameter: returns the character at that index 
#    2 parameters, returns the string of characters between those indices.

# the text widget needs to index characters across multiple lines which is effectively a two dimensional space. 
#    accepts indices arguments of specially formatted strings. 
#    The syntax includes a base which gives a starting point for reference and zero or more optional modifiers which adjust that index from the starting point.

# There are many different ways to build this index strings but for this course, I'm going to focus on the most commom. 
#    base index: a common format is to use the line.char, 
#        where line and char are replaced with the index numbers of the line and character you wish to index. 
#        i.e. 4.2 would refer to the position in front of character 2 two, line 4. 
#    Keep in mind:
#        lines are numbered starting with 1 
#        characters are numbered starting with 0.
#    I.E. historical programming conventions. 

# base 1.0 - the position at the beginning of the text box. 

# common base term is "end" 
#    used by itself - the position after the last character in the whole text box. 
#    with a line - syntax "line_number.end" refers to the position after the last character in that line. 
#    referring to logical lines not display lines.
#        logical lines always end with the invisible new line character; may be different then the lines that are displayed in the text widget due to word wrapping. 

# optional modifiers to the expression:
#    Plus or minus a number of chars or lines is commonly used to increment or decrement the character that's being indexed from the base. 
#    line start or line end modifiers: move the pointer to the start or end of a currently indexed line.

#the words "start" and word "end" modifiers: move the pointer to the starter end of the word that's currently indexed. 
#    can string together as many of these modifiers as you need to 
#    be evaluated in order from the left to the right. 

#I've just touched on some of the common index bases and modifiers but there are many other ways to express indices. If you want to learn more about that, I recommend looking at the indices section of Tk documentation for the text widget. 

#use the Get method of the text widget with these indices by passing them in as strings.

# call text.get, 
#    pass the first index of the start of the area I want to get. 
#    use 1.0 which represents the beginning of my text box 
#    the "end" index of the section I want to get "end". 
#        returns the entire contents of the text widget from beginning to end. 
        
# You notice that as it does it the new lines are included as well and IDOL displays them as slash end characters. 

# get the contents of just the first line 
#text.get
#    Start with the index of the beginning of the first line = 1.0 
#    to the index at the end of the first line = 1.end 

# this retrieves all of the information from that first logical line in the text. 

# So even though this message is spread across two lines in the widget because of word wrapping, there's only one new line character at the end and so that's one logical line. 

print(text.get('1.0', 'end'))
print(text.get('1.0', '1.end'))


# the Insert method 
# insert text into the text widget:
#    two parameters. 
#        1st parameter: the index I wish to insert.
#            1.0 as my base and then I'm going to add an additional modifier to that of two lines. 
# So this creates an index starting from the first position in the text entry field 
# down two additional logical lines. 
#        2nd: text I want to insert. "inserted message". 

# it inserts it at the position down two lines from the start of the text entry field.


# insert a multi-line message by using the slash N new line character within the message that we're inserting: 
#    insert a message to the end of the message just inserted a moment ago. 
#    use 1.0. 
#    add the modifier again of going down two lines so I'm looking at the third line down. 
#    add another modifier of line N. 
#    going down to that same line that we originally inserted into but now we're indexing at the end of that line. 
#    add in the message of and more and more.

# If we insert it like that our text box now reads, inserted message and more and more and more. So by having those new line characters within the inserted string, they'll be placed on seperate lines and displayed that way in the text entry box. 

text.insert('1.0 + 2 lines', 'Inserted message')
text.insert('1.0 + 2 lines lineend', 'and\n more and \nmore.')


# the Delete method. 
# To delete text from the text widget 
#    one index: it will delete the character at that index. 
#        pass the index of 1.0 deletes the first character within my text box which is this capital T. 
#    two indices: it will delete the characters from the beginning index to just before that last index.

#    a noninclusive delete. 
#        use the index 1.0 which represents the beginning of that first line and with the line.end modifier which represents the end of that first line. 
#        I delete everything up to that end of the first line; 
# it will Not delete the last character in that first line which is the new line character. 
#    two blank lines: include that new line character for deletion, we can add one more modifier to our index.

# to delete everything from the beginning of my text box to the third line using line.end. 
#    deleting the top three lines of my text box 
#        add one additional modifier here for "+ one char". 

#So go down to the index at the end of this first line. It will go one character beyond that; Delete method is noninclusive; it won't include the last character that's referenced here in this index. 
#Now it deletes those top three lines and the new line character at the end of that third line as well.

text.delete('1.0')
text.delete('1.0', '1.0 lineend')
text.delete('1.0', '3.0 lineend + 1 chars')


# Using the Replace method: 
# Replace sections of text within my text widget:
#    two indices. 
#        the beginning and end of the section of text you want to replace. 
#    to replace everything on the first line of text here 
#    the third parameter: the actual string you want to replace it with.

# "more" w/ "this is the first line". 
#    basically the same as calling the Delete command on that first line;
#    then inserting the text in it's place.
  
text.replace('1.0', '1.0 lineend', 'This is the first line.')


# the text widget is not a themed widget and therefore it doesn't have the same state and in-state methods that we saw with the entry widget. 
#    has a state property using the text.config method: 
#        set to "disabled' or "normal" 

#    state = 'disabled' 
#        my text field is disabled; can no longer type text into it.             Disabling a text widget also prevents other methods from             programatically modifying the text.
#            if I had tried to delete the text while it's currently disabled. 
#            try delete everything out of my text field with 1.0 to the end; doesn't do anything because it's disabled. 

#    re-enable the text field
#         use config method state = 'normal'.

text.config(state = 'disabled')
text.delete('1.0', 'end')
text.config(state = 'normal')


# Can identify and name sections of the text with tags and and marks. 
# Tags describe a range or collection of characters and 
# Marks specify a specific location between two characters within the text widget. 
# Can use those tags and marks to change properties such as the font and color.
# For section of text and control where to insert or delete text. 


# tag_add method 
# To add a tag to the text widget, 
#    use the add underscore tag method. 
#    takes three parameters. 
#        1st parameter: name of the tag we want to create as a string.                 "my tag". 
#        start and end for that tag expand. 
#        So at my tag to expand starting with the first character within text widget, and I want it to go all the way to the end of the first word at that first character is in.

text.tag_add('my_tag', '1.0', '1.0 wordend')

# the tag_configure method.
#    configure properties about that tag 
#        pass in the 1st parameter - the name of the tag we want to configure 
#        specify one or more properties. 
#            change the background to yellow. 
#            this tag expands from the beginning of the text field to the end of the first word.  see now the word this is highlighted in yellow. 
#    Other tag configuration options:
#        include font, foreground, justify, over strike, underline, wrap and more other common text options. 
#    It's possible to create multiple tags that reference the same section of text. If the configuration options for those tags have a conflict, it will be settled based on a priority system where the most recently created tag has the highest priority. 
#    If you need to modify the priority of your tags, you can do so by using the "tag_raise", and "tag_lower" methods.

text.tag_configure('my_tag', background = 'yellow')


# tag_remove method:
#    remove the tag from a section of text
#    pass in the name of the tag you want to remove
#        "my tag"
#    pass in the start and end index of the section you want to remove it from.     
#        remove everything from character 1.1, which is line one, character one to 1.3. 
#        index is noninclusive; not actually going to remove the tag from the character 1.3. So remove the tag on character 1.1 and 1.2.

# If I execute this, you'll notice since that tag from my tag got removed. Those two characters are no longer highlighted yellow. 

text.tag_remove('my_tag', '1.1', '1.3')


# the tag ranges method
#    to find out what characters are included within a tag
#    pass in the name of a tag i.e. "my tag"
#        return to you the start and end locations of the sections covered by that tag. 
#        "my tag" currently covers character 1.0 to 1.1, and then it covers character 1.3 to 1.4.

print(text.tag_ranges('my_tag'))


# the tag names method:
#    To get a list of all of the tags that exist within my text widget, 
#        returns the list of all the tags that exist in my text, 
#        "my tag" 
#        this special tag called "sel", stands for select.
#            This tag is automatically updated to expand whatever the selected area of the text is. 
#            can use the select tag when binding to the virtual selection event of the text widget, 
#                which will be covered in the later virtual event section of the course.

# the tag names method with an index:
#    return all of the tags that are included within that index. 
#        provided the index of 1.0, which is the first character, 
#        and this will return my tag because my tag is the only tag that currently covers that character. 

# use as indices.
#    another reason to create tags,  
#    But since tags span multiple characters, an indices have to refer to a single character, 
#       you have to specify whether you want to use the start or into the tag for an index.

print(text.tag_names())


# use the tag as an index within the replace command. 
#    first index: my_tag specify the first character within that tag. 
#     my_tag last refers to the last character that's within that tag. 
#    add the text I'm going to replace it with
#         replacing the word "this" with "that"
         
text.replace('my_tag.first', 'my_tag.last', 'That was')


# tag delete method:
#    can manually specify to delete a tag 
#    taking the tag you wanted to delete as it's only parameter. 
#         ie my_tag. 

text.tag_delete('my_tag')


# Marks:
# using tags to create marks to indicate a particular place in the text. 
#    marks specify a single position which exist between two characters.
#        vs. tags which have a start and an end, 

# Marks follow that position between characters as text is inserted or deleted from the text widget. 

#mark_names method:
#    to get a list of the marks that are present in a text widget, 
#    two marks TK automatically keeps track of. 
#        1 "insert"  marks the current index of the insert cursor. 
#        2 "current" specifies the index that is currently under the mouse.
text.mark_names()

# insert method
#    use that automatically tracked insert mark as index 
#        set for the index of where I want to insert my text. 
#    reference that insert mark by entering a string with insert in it.
#          pass the insert method the text I want to insert there. 
#         insert an underscore at the position of the insert marker.              
#            place that insert marker right here before the word "first".

text.insert('insert', '_')

# mark set method:
#    can also create and modify the location of marks 
#    pass in the name of the mark you want to create. 
#        i.e. "my mark". 
#    pass in the index of where you want that mark to be. 
#        i.e. at the end of the text widget. 

# marks follow their relative location in the text widget as additional text is inserted or deleted

text.mark_set('my_mark', 'end')

# mark underscore gravity method
#    Marks have a property called gravity which determines whether the mark 
#      will stick to the character on its left or right if things shift around. 
#    configure the gravity
#        pass in the name of the mark we want to configure. 
#            i.e. "my mark" 
#        pass in a string "left" or "right" 
#            2 options available for gravity; specify which side the mark will follow. 
#        "my mark" to right. 
text.mark_gravity('my_mark', 'right')

# the mark unset method:
#    When we're done using a mark, we can remove it 
#    only parameter needed to pass - the name of mark to remove. 
text.mark_unset('my_mark')

# text widget can also contain pictures and even other TK widgets. 
#    enables it to function somewhat like a geometry manager. 
# To add an image to the text widget, 
#    first create the image in the TK using the photo image constructor method. 
#    passed in the path to my python_logo.gif file. 
#    created this photo image object and stored it in variable called image.
image = PhotoImage(file = 'python_logo.gif').subsample(5, 5) # Change path as needed

# add it to my text box, 
#    call text.image_create. 
#    pass in the index of where I want to insert that image. 
#        So I'm going to use the insert mark here. 
#        set the image property to that image I'm going to be inserting. 
#    this references the image property, 
#    this references the name of the variable I stored that image in. 

#    insert it at the end of the first line by moving my insert cursor there. 
#    You can see now we added that python logo.gif.
    
text.image_create('insert', image = image)
text.image_create('insert', image = image)


# add other TK widgets to the text field in a similar fashion.
#    create a button using the button constructor 
#        as a child of the text widget 
#        text of this will say "Click me." 

button = Button(text, text = 'Click Me')

#    add this button to the text widget by using the "window_create" method. 
#    pass in the index at which to insert this new button, 
#    set the window property to the name of the widget object 
#        or I pass it the widget object I want to add. 
#    store that button in a variable called button, 
#    insert it here at the end of that line before the period.

text.window_create('insert', window = button)

root.mainloop()
