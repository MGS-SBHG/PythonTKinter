"""Implement quick sort in Python.
Input a list.
Output a sorted list.

for each (unsorted) partition
  set first element as pivot
  storeIndex = pivotIndex + 1
  for i = pivotIndex + 1 to rightmostIndex
    if element[i] < element[pivot]
      swap(i, storeIndex); storeIndex++
  swap(pivot, storeIndex - 1)

"""
def quicksort(array):
    array_length = len(array)
    left = 0
    right = array_length - 1 
    i = left 
    j = right     
    
    pivot_index = round((i + j) / 2)
    # pivot_index = array_length - 1
    pivot = array[pivot_index]
    
    # partition 
    while (i <= j): 
        while (array[i] < pivot):
            i=i+1
        while (array[j] > pivot):
            j=j-1
        if (i <= j):
            tmp = array[i]
            array[i] = array[j]
            array[j] = tmp
            i=i+1
            j=j-1 
    print(array)
            
    #recursion 
    if (left < j):
    #   quickSort(arr, left, j);
        array_length = len(array)
        #left = 0
        #right = j 
        i = left 
        #j = right     
    
        pivot_index = round((i + j) / 2)
        # pivot_index = array_length - 1
        pivot = array[pivot_index]
    
    # partition 
        while (i <= j): 
            while (array[i] < pivot):
                i=i+1
            while (array[j] > pivot):
                j=j-1
            if (i <= j):
                tmp = array[i]
                array[i] = array[j]
                array[j] = tmp
                i=i+1
                j=j-1 
    print(array)
                
    if (i < right):
    #   quickSort(arr, i, right);      
        array_length = len(array)
        #left = i
        #right = right 
        #i = left 
        j = right     
    
        pivot_index = round((i + j) / 2)
        # pivot_index = array_length - 1
        pivot = array[pivot_index]
    
    # partition 
        while (i <= j): 
            while (array[i] < pivot):
                i=i+1
            while (array[j] > pivot):
                j=j-1
            if (i <= j):
                tmp = array[i]
                array[i] = array[j]
                array[j] = tmp
                i=i+1
                j=j-1 
    print(array)      
                                
    #return []

                 
                          
def main():

    test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    
    print (quicksort(test))        

if __name__ == "__main__": main()
