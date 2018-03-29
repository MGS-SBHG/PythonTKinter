
#  Element class
#  element - a single unit in a linked list
#  use __init__ to initialize a new Element. 
#  "value" variable: number, string, character, etc 
#  "next" variable that points to the next element in the linked list. 
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

# a LinkedList class:
# a LinkedList has a head Element - the first element in the list. 
# If we establish a new LinkedList without a head, it will default to None. 
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

# method will add a new Element to the end of our LinkedList.
    def append(self, new_element):
        current = self.head
        # If the LinkedList already has a head, 
        if self.head:
            # iterate through the next reference in every Element 
            # until you reach the end of the list.
            while current.next:
                current = current.next
            # Set next for the end of the list to be the new_element.     
            current.next = new_element
        else:
            # if there is no head already, just assign new_element to it and do nothing else.
            self.head = new_element


    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".        
        Return "None" if position is not in the list."""
                
        key_pos = 1        
        current = self.head
        previous = None 
              
        while current != None:                                                   
            if key_pos == position:                       
                return current
            previous = current
            current = current.next            
            key_pos+=1                        
                    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
                
        key_pos = 1        
        current = self.head
        previous = None 
              
        while current != None:                                                   
            if key_pos == position:
                # Update link of the "previous" node to point to the new node.
                previous.next = new_element
                # Update link of the new node, to point to the "next" node.
                new_element.next = current              
                return current
            previous = current
            current = current.next            
            key_pos+=1    
            
                                                        
    def delete(self, value):
        """Delete the first node with a given value."""                           
        current = self.head
        key_value = value         
        previous = None 
        
        if ((key_value == current.value) & (previous == None)):
            self.head = current.next                        
            return self.head  
        else:       
            while current != None:                                                   
                if key_value == value:   
                    previous = current  
                    current = current.next 
                    # Update next link of the previous node to point to the next node following removed node.
                    previous.next = current.next
                    return current        
                      
                          
def main():

# Test cases
# Set up some Elements

    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

# Start setting up a LinkedList
    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)

# Test get_position
# Should print 3
#    print (ll.head.next.next.value)
# Should also print 3    
#    print ('Test get_position in main: ', ll.get_position(3).value)

# Test insert
    ll.insert(e4,3)
# Should print 4 now
    print ('Test insert in main: ', ll.get_position(3).value)

    i = 1
    while i < 4:
        print('position:', i, 'value', ll.get_position(i).value )
        i=i+1
    
# Test delete
    ll.delete(1)
    
# Should print 2 now
    print ('Test delete in main: ', ll.get_position(1).value)
# Should print 4 now
    print ('Test delete in main: ', ll.get_position(2).value)
# Should print 3 now
    print ('Test delete in main: ', ll.get_position(3).value)

if __name__ == "__main__": main()
