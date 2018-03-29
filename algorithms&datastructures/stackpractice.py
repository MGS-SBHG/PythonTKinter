"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?

Solution:
We had two options here—
either pop and push from the first element in our linked list, 
or pop and push from the last element. 
We already had a function, append(), that adds an element to the end.

Why didn't we just come up with a function for removing the last element 
and call it a day? 
Every operation on a linked list must start with the head. append() 
thus traverses the whole list, taking O(n). 
Any operation on the last element requires us to traverse everything, 
so even though we had to write a new method our code will run much faster 
if we push/pop from the first element in a linked list.

"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        new_element.next = self.head
        self.head = new_element
                
    def delete_first(self):
        if self.head:
            deleted_element = self.head
            temp = deleted_element.next
            self.head = temp
            return deleted_element
        else:
            return None
                 
class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)
       

    def pop(self):
        return self.ll.delete_first()
                                                  
def main():
    
    # Test cases
    # Set up some Elements
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    # Start setting up a Stack
    stack = Stack(e1)

    # Test stack functionality
    stack.push(e2)
    stack.push(e3)
    print ("stack.pop().value1 ", stack.pop().value)
    print ("stack.pop().value2 ", stack.pop().value)
    print ("stack.pop().value3 ", stack.pop().value)
    print (stack.pop())
    stack.push(e4)
    print ("stack.pop().value4 ", stack.pop().value)
    
if __name__ == "__main__": main()
