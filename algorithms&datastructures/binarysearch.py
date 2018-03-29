"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""
from math import floor

def binary_search(input_array, value):   
    # Given an array input_array of n elements 
    # with values or records input_array[0] ... input_array[n−1]   
    # Set l to 0 and h to n − 1.
    l = 0    
    h = len(input_array) - 1              
     
    while(l <= h):
        # Set m (the position of the middle element) to the floor of (l + h) / 2.
        m = floor((l + h) / 2)
        print("m", m)
        # If input_array[m] = value, search is done; return m.
        if (input_array[m] == value):
            return m
                
        # If Am < T, set L to m + 1 and go to step 2.   
        elif (input_array[m] < value): 
            l = m + 1      
            print("a[m] < target: l, m: ", l, m)
                                                                    
        # If Am > T, set h to m − 1 and go to step 2.
        else:           
            h = m - 1          
            print("input_array[m] > value: l, m", l, m)        
    return -1
                                                              
def main():    
    test_list = [1,3,9,11,15,19,29]
    test_val1 = 25
    test_val2 = 15
    print ("result for test_val1: ", binary_search(test_list, test_val1))
    print ("test_val2: ", binary_search(test_list, test_val2))

if __name__ == "__main__": main()
