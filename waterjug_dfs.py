from collections import defaultdict
jug1, jug2, aim = 4, 3, 2
visited = defaultdict(lambda: False)
def waterJugSolver(amt1, amt2):
	if (amt1 == aim and amt2 == 0):
		print(f" {amt1}    {amt2}")
		return True
	if visited[(amt1, amt2)] == False:
		print(f" {amt1}    {amt2}")
		visited[(amt1, amt2)] = True
		return (waterJugSolver(0, amt2) or
				waterJugSolver(amt1, 0) or
				waterJugSolver(jug1, amt2) or
				waterJugSolver(amt1, jug2) or
				waterJugSolver(amt1 + min(amt2, (jug1-amt1)),
				amt2 - min(amt2, (jug1-amt1))) or
				waterJugSolver(amt1 - min(amt1, (jug2-amt2)),
				amt2 + min(amt1, (jug2-amt2))))
	else:
		return False
print("Jug1 : 4l \nJug2 : 3l\n")
print("Steps followed to get 2l in Jug1: \n")
print("Jug1 Jug2")
waterJugSolver(0, 0)

