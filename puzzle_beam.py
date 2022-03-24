

import copy



def Print(A):  

    for x in range(3):

        for y in range(3):

            print(A[x][y],end=" ")

        print()

    print()



def Swap(a,b): 

    return b,a



def FindEmptyTile(I):

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

   

def Check(X,Visited):  

    flag=0

    for Temp in Visited:

        if X==Temp[0]:

            flag=1

    return flag



def Heuristic(S,F):

    count=0

    for x in range(3):

        for y in range(3):

            if S[x][y]==F[x][y] and S[x][y]!=0:

                count+=1

    return count





def PrintPath(Visited):     

    Visited.reverse()

    Path=[F]

    Temp=Visited[0][0]

    for X in Visited:

        if(X[0]==Temp):

            Path.append(X[1])

            Temp=X[1]

        if(Temp==I):

            break

    Path.reverse()

    for X in Path:

        print(f"No of Matched Tiles:\t{Heuristic(X,F)}")

        Print(X)



def Solve(I,F,bwidth): 

    flag=0

    P = [[0,0,0], [0,0,0], [0,0,0]]

    Visited=[]    

    Queue=[(I,P,Heuristic(I,F))]      

    count=1

    while(len(Queue)!=0):

        S=Queue[len(Queue)-1]    

        Queue.pop()

        Visited.append(S)

        if(S[0]==F):  

            flag=1

            break

        x,y=FindEmptyTile(S[0])   

        X=Up(S[0],x,y)            

        if(Check(X,Visited)==0):    

            Queue.append((X,S[0],Heuristic(X,F)))

            count+=1

        X=Down(S[0],x,y)            

        if(Check(X,Visited)==0):

            Queue.append((X,S[0],Heuristic(X,F)))

            count+=1

        X=Left(S[0],x,y)      

        if(Check(X,Visited)==0):

            Queue.append((X,S[0],Heuristic(X,F)))

            count+=1

        X=Right(S[0],x,y)       

        if(Check(X,Visited)==0):

            Queue.append((X,S[0],Heuristic(X,F)))

            count+=1

        Queue.sort(key = lambda x: x[2]) 

        if(len(Queue)>bwidth):

            for b in range(bwidth,len(Queue)):

                Queue.pop(0)

    if(flag==0):

        print("Solution not Found with Beam Search for Beta =",bwidth)

        print()

    else:

        print("Solution Found with Beam Search Algorithm with Beta =",bwidth,end="\n")

    print("Following States are Visited During Beam Search\n")

    PrintPath(Visited)

    print("Total States Visisted:",count)



I=[[5,6,7],[4,0,8],[3,1,2]]    

F=[[4,5,7],[0,6,8],[3,1,2]] 

B_Width=2

Solve(I,F,B_Width)