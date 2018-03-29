from collections import deque

def islandCounter(M):
    if (M == None or M == [[]] ):
        return 0
 
    islands = 0

    # nbr of rows; columns
    c = len(M[0])
    r = len(M)

    for i in range(0, r):
        for j in range(0, c):
            if (M[i][j] == 1 ):
                islands += 1    
        #helper method for Breath-First Search
                findPartsofIsland(M, i, j, r, c)
    return islands

def findPartsofIsland(M, i, j, r, c):
    # initialize queue; get first element     
    q = deque()
    q.append([i,j])

    while (len(q) != 0):
        i=q.pop()
        x = i[0]
        y = 1[0]  
        if (M[x][y] == 1 ):
            M[x][y] = 2
    # check if 2 elements are next to each other, 
    # if they are, add it to the queue    
    appendif(q,r,c,x+1,y+1)    
    appendif(q,r,c,x,y+1)    
    appendif(q,r,c,x-1,y)
    appendif(q,r,c,x,y-1)
        

def appendif(q,r,c,x,y)):
    if (x>0 and x < c and y >=0 and g < r):
        q.append(x,y)

                          
def main():
        
# Test cases
# None

# Empty []

# [1,0,1]  

# [0,1,1]


if __name__ == "__main__": main()
