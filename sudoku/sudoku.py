from sudoku_utility import *
import sys
import time

solution = []		#this one will store all the solutions

def solve(grid, sol, r, c):
	global solution
	if(len(solution) > 0):
		return
	for i in range(r, 9):
		for j in range(c, 9):
			print(i, j)
			time.sleep(0.2)
			'''
			either the last cell in the grid will contain possibilites, or it will not contain any
			if list of possibilites exist, go through each of them, and if r = 9 and c = 9, then check whether you have reached a solution or not
			if it is not a list of possibilites, then simply assign the number to sol . if r = 9 and c = 9, then check whether you have reached a solution or not.
			'''
			try:
				for possibility in grid[i][j]:
					sol[i][j] = possibility
					if(r == 8 and c == 8):
						if(checkgrid(sol) == True):
							solution.insert(len(solution), sol)
						else:
							if(possibility == grid[i][j][len(grid[i][j])]):
								return
							else:
								continue
					else:
						if(j < 8):
							solve(grid, sol, i, j + 1)
						elif(i < 8):
							solve(grid, sol, i + 1, 0)
						else:
							return
			except:
				sol[i][j] = grid[i][j]
				if(r == 8 and c == 8):
					if(checkgrid(sol) == True):
						solution.insert(len(solution), sol)
					else:
						return
				else:
					if(j < 8):
						solve(grid, sol, i, j + 1)
					elif(i < 8):
						solve(grid, sol, i + 1, 0)
					else:
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
		#now use brute force through the possibilites to find the solution
		solve(grid, sol, 0, 0)
		for i in range(len(solution)):
			printgrid(solution[i])
		
	elif(mode == 2):
		grid = buildgrid("grid.txt")
		printgrid(grid)
		print(checkgrid(grid))
	else:
		print("Reading is hard, isn't it?")