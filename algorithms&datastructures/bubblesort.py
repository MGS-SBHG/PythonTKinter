
def bubbleSort(input_array):
    print("input_array", input_array)
    n = (len(input_array)-1)
    print("n", n)
         
    i = 1    
    # repeat
    while(n!=0):
        newn = 0        
        while(i <= n):  
            if (input_array[i-1] > input_array[i]):
                # swap(input_array[i-1], input_array[i])
                print("input_array[i-1] before ", input_array[i-1])
                print("input_array[i] before ", input_array[i])
                 
                temp = input_array[i-1]
                print("temp", temp)
                
                input_array[i-1] = input_array[i]
                print("input_array[i-1] after ", input_array[i-1])
                
                input_array[i] = temp
                print("input_array[i] after ", input_array[i])                            
                newn = i   
            else: i=1+1                     
        n = newn    
        return            
                          
def main():
    
    a = [21,4,1,3,9,20,25,6,21,14]
    
    bubbleSort(a) 
    
    print(a)
    

if __name__ == "__main__": main()
