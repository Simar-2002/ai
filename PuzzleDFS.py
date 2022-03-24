from collections import defaultdict
from itertools import chain
import copy

def Print(A):
    for x in range(3):
        for y in range(3):
            print(A[x][y],end=" ")
        print()
    print()

def Swap(a,b):
    return b,a

def FindZero(I):
    for x in range(3):
        for y in range(3):
            if I[x][y]==0:
                return x,y

def Up(I,x,y):
    temp=copy.deepcopy(I)
    if x!=0:
        temp[x][y],temp[x-1][y]=Swap(temp[x][y],temp[x-1][y])
    return temp
            
def Down(I,x,y):
    temp=copy.deepcopy(I)
    if x!=2:
        temp[x][y],temp[x+1][y]=Swap(temp[x][y],temp[x+1][y]) 
    return temp

def Left(I,x,y):  
    temp=copy.deepcopy(I)
    if y!=0:  
        temp[x][y],temp[x][y-1]=Swap(temp[x][y],temp[x][y-1])    
    return temp

def Right(I,x,y):
    temp=copy.deepcopy(I)
    if y!=2:
        temp[x][y],temp[x][y+1]=Swap(temp[x][y],temp[x][y+1])     
    return temp

def Puzzle(I,F):
    if F==I:
        Print(I)
        return True

    if(I in Visited):
        return False
        
    Visited.append(I)
    Print(I)
    x,y=FindZero(I)
    return Puzzle(Up(I,x,y),F) or Puzzle(Down(I,x,y),F) or Puzzle(Left(I,x,y),F) or Puzzle(Right(I,x,y),F)

Visited=[]
I = [[2, 0, 3], [1, 8, 4], [7, 6, 5]]
F = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
Puzzle(I,F)
