#Simardeep Singh_102003559
from cmath import exp
import copy
from itertools import chain

simardeep_state = [[2, -1, 3], [1, 8, 4], [7, 6, 5]]
goal_state = [[1, 2, 3], [8, -1, 4], [7, 6, 5]]

queue = [simardeep_state]
visited = []
parent = {}


def calculate_heuristic(s):
    count = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if(s[i][j] != goal_state[i][j] and s[i][j] != -1):
                count += 1
    return count


def print_state(s):
    L = list(s)
    for i in range(0, 3):
        print(L[i], end=" ")
    print()
    for i in range(3, 6):
        print(L[i], end=" ")
    print()
    for i in range(6, 9):
        print(L[i], end=" ")
    print("\n")


def print_final():
    state = tuple(list(chain.from_iterable(goal_state)))
    list1 = [state]
    while(state != tuple(list(chain.from_iterable(simardeep_state)))):
        list1.append(parent[state])
        state = parent[state]
    list1.reverse()
    for x in list1:
        print_state(x)


def find_blank(s):
    for i in range(0, 3):
        for j in range(0, 3):
            if(s[i][j] == -1):
                return i, j


def swap(a, x1, y1, x2, y2):
    temp = a[x1][y1]
    a[x1][y1] = a[x2][y2]
    a[x2][y2] = temp


def move_right(s, i, j):
    current_state = copy.deepcopy(s)
    if(j != 2):
        swap(current_state, i, j, i, j+1)
    return current_state


def move_left(s, i, j):
    current_state = copy.deepcopy(s)
    if(j != 0):
        swap(current_state, i, j, i, j-1)
    return current_state


def move_up(s, i, j):
    current_state = copy.deepcopy(s)
    if(i != 0):
        swap(current_state, i, j, i-1, j)
    return current_state


def move_down(s, i, j):
    current_state = copy.deepcopy(s)
    if(i != 2):
        swap(current_state, i, j, i+1, j)
    return current_state


def check_visted(st, vt):
    for i in range(0, len(vt)):
        if(st == vt[i]):
            return 1
    return 0


def generate_states(init, parent_heuristic_value):
    i, j = find_blank(init)

    if(j != 2):
        s = move_right(init, i, j)
        val = calculate_heuristic(s)
        if(check_visted(s, visited) == 0 and val < parent_heuristic_value):
            parent[tuple(list(chain.from_iterable(s)))] = tuple(
                list(chain.from_iterable(init)))
            parent_heuristic_value = val
            return s, parent_heuristic_value

    if(j != 0):
        s = move_left(init, i, j)
        val = calculate_heuristic(s)
        if(check_visted(s, visited) == 0 and val < parent_heuristic_value):
            parent[tuple(list(chain.from_iterable(s)))] = tuple(
                list(chain.from_iterable(init)))
            parent_heuristic_value = val
            return s, parent_heuristic_value

    if(i != 0):
        s = move_up(init, i, j)
        val = calculate_heuristic(s)
        if(check_visted(s, visited) == 0 and val < parent_heuristic_value):
            parent[tuple(list(chain.from_iterable(s)))] = tuple(
                list(chain.from_iterable(init)))
            parent_heuristic_value = val
            return s, parent_heuristic_value

    if(i != 2):
        s = move_down(init, i, j)
        val = calculate_heuristic(s)
        if(check_visted(s, visited) == 0 and val < parent_heuristic_value):
            parent[tuple(list(chain.from_iterable(s)))] = tuple(
                list(chain.from_iterable(init)))
            parent_heuristic_value = val
            return s, parent_heuristic_value

flag = 0
parent_heuristic_value = calculate_heuristic(simardeep_state)
while(len(queue) > 0):
    if(queue[0] == goal_state):
        flag = 1
        break
    visited.append(queue[0])
    explore = queue[0]
    queue.pop(0)
    s, parent_heuristic_value = generate_states(
        explore, parent_heuristic_value)
    queue.append(s)

if(flag == 0):
    print("Hill Climbing algorithm has failed for this problem")
else:
    print_final()
