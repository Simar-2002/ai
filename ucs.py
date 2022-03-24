graph = [[0, 1, 5, 15, 0], [1, 0, 0, 0, 10], [
    5, 0, 0, 0, 5], [15, 0, 0, 0, 5], [0, 10, 5, 5, 0]]

s = 0
a = 1
b = 2
c = 3
g = 4

open = [s]
closed = []
parent = {
    s: -1
}
cost = {
    s: 0
}


def sort_according_to_cost(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-i-1):
            if(cost[arr[j]] > cost[arr[j+1]]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


def generate_successors(element, op, cl):
    connected = []
    new_cost = {}

    for i in range(0, len(graph)):
        if(graph[element][i] != 0):
            connected.append(i)
            new_cost[i] = cost[element] + graph[element][i]

    for x in connected:
        if x in op:
            if cost[x] > new_cost[x]:
                parent[x] = element
                cost[x] = new_cost[x]
        elif x in cl:
            if cost[x] > new_cost[x]:
                parent[x] = element
                cost[x] = new_cost[x]
        else:
            op.append(x)
            parent[x] = element
            cost[x] = new_cost[x]


while(len(open)):
    sort_according_to_cost(open)
    x = open[0]
    open.pop(0)
    generate_successors(x, open, closed)
    closed.append(x)

state = [g]
i = 0
while(parent[state[i]] != s):
    state.append(parent[state[i]])
    i += 1
state.append(s)
state.reverse()
print('Path', end=": ")
for i in state:
    if i == 0:
        print('S', end=" -> ")
    elif i == 1:
        print('A', end=" -> ")
    elif i == 2:
        print('B', end=" -> ")
    elif i == 3:
        print('C', end=" -> ")
    else:
        print('G')

print("Cost:", cost[g])
