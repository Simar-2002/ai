#Simardeep Singh_102003559
initial_state = [[2, -1, 3], [1, 8, 4], [7, 6, 5]]
goal_state = [[1, 2, 3], [8, -1, 4], [7, 6, 5]]

p = 3  # parameter for minkowski distance
eucleadian = 0
manhattan = 0
minkowski = 0

for i in range(0, 3):
    for j in range(0, 3):
        for k in range(0, 3):
            for l in range(0, 3):
                if(initial_state[i][j] != -1 and initial_state[i][j] == goal_state[k][l]):
                    manhattan += abs(k-i) + abs(l-j)
                    eucleadian += ((k-i)**2 + (l-j)**2)**(1/2)
                    minkowski += (abs(k-i)**p + abs(l-j)**p)**(1/p)
print(f"eucleadian distance: {eucleadian}")
print(f"manhattan distance: {manhattan}")
print(f"minkowski distance: {minkowski}")

