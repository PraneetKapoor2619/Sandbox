from sudoku_utility import *
import sys
import time

grid = []		#contains the given numbers and the list of possible values for each cell
iterable = []		#contains tuples which have the indices of cells which are iterable
solution = []		#this one will store all the solutions

def solve(sol, index):
	global grid, iterable, solution
	i, j = iterable[index]
	print(iterable[index], grid[i][j])
	for tmp in grid[i][j]:
		print(grid[i][j])
		sol[i][j] = tmp
		if(index == (len(iterable) - 1)):
			if(checkgrid(sol)):
				solution.insert(len(solution), sol)
			else:
				continue
		else:
			solve(sol, index + 1)
			print("I have returned son", iterable[index])
	print("On the path to return")
	return

if __name__ == "__main__":
	sys.tracebacklimit = 0
	mode = int(input("1. Solver mode\n2. Checker mode\n>> "))
	if(mode == 1):
		grid = buildgrid("puzzle.txt")
		sol = grid
		printgrid(grid)
		#fill grid with the possibilities
		for block in range(1, 10):
			grid = fillblock(grid, block)
		
		printgrid(grid)
		#form a list of tuples containing the indices of cells which are grids
		for i in range(0, 9):
			for j in range(0, 9):
				if(islist(grid[i][j]) == True):
					iterable.insert(len(iterable), (i, j))
				else:
					continue
		print("\n",iterable, "\n")
		#now use brute force through the possibilites to find the solution
		solve(sol, 0)
		for i in range(len(solution)):
			printgrid(solution[i])
		
	elif(mode == 2):
		grid = buildgrid("grid.txt")
		printgrid(grid)
		print(checkgrid(grid))
	else:
		print("Reading is hard, isn't it?")