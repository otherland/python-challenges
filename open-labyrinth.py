
def checkio(grid, start=(1,1), end=(10,10)):
	compass = {
		(0,1):'E',
		(1,0):'S',
		(0,-1):'W',
		(-1,0):'N',
	}
	dead_ends = list()
	visited = list()
	def move(current_position=start, previous_direction=(0,0), stack=list()):
		dirs = [i for i in ((0,1), (1,0), (0,-1), (-1,0)) if i != (-previous_direction[0],-previous_direction[1])]
		print('previous direction:', previous_direction)
		x, y = current_position
		openn = False
		for coords in dirs:
			print('stack:', stack)
			x1, y1 = coords
			cell = (x + x1, y + y1)
			print('dead ends:', dead_ends)
			if cell in dead_ends:
				continue
			print('cell:', cell)
			current = grid[x + x1][y + y1] == 0
			if current:
				openn = True
				print('open', cell)
				visited.append(cell)
				stack.append((compass[coords]))
				if cell == end:
					print('found')
					return stack, True
				stack, found = move(current_position=cell, previous_direction=coords, stack=stack)
				if found:
					return stack, found
			else:
				openn = False
				print('Closed', cell)
		if not openn and stack:
			print 'stepping backwards'
			dead_ends.append(current_position)
			stack.pop()
		print 'returning'
		return stack, False

	stack, found = move()

	print 'visited', visited
	result =  "".join(stack)
	print result
	return result



def check_route(func, labyrinth):
	MOVE = {"S": (1, 0), "N": (-1, 0), "W": (0, -1), "E": (0, 1)}
	#copy maze
	route = func([row[:] for row in labyrinth])
	print route
	pos = (1, 1)
	goal = (10, 10)
	for i, d in enumerate(route):
		move = MOVE.get(d, None)
		if not move:
			print("Wrong symbol in route")
			return False
		pos = pos[0] + move[0], pos[1] + move[1]
		print pos, labyrinth[pos[0]][pos[1]]
		if pos == goal:
			return True
		if labyrinth[pos[0]][pos[1]] == 1:
			print("Player in the pit")
			return False
	print("Player did not reach exit")
	return False


assert check_route(checkio, [
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
	[1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
	[1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
	[1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
	[1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
	[1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
	[1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "First maze"
# assert check_route(checkio, [
# 	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# 	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
# 	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
# 	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
# 	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
# 	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
# 	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
# 	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
# 	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
# 	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
# 	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
# 	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "Empty maze"
# assert check_route(checkio, [
# 	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# 	[1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
# 	[1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
# 	[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
# 	[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
# 	[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
# 	[1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
# 	[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
# 	[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
# 	[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
# 	[1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
# 	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "Up and down maze"
# assert check_route(checkio, [
# 	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# 	[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
# 	[1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
# 	[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
# 	[1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
# 	[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
# 	[1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
# 	[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
# 	[1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
# 	[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
# 	[1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
# 	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "Dotted maze"
# assert check_route(checkio, [
# 	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# 	[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
# 	[1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
# 	[1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
# 	[1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
# 	[1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
# 	[1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
# 	[1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
# 	[1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
# 	[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
# 	[1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
# 	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "Need left maze"
# assert check_route(checkio, [
# 	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# 	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
# 	[1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
# 	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
# 	[1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
# 	[1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
# 	[1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
# 	[1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
# 	[1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
# 	[1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
# 	[1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
# 	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "The big dead end."
print("The local tests are done.")