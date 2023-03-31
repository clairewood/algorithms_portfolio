# algorithms_portfolio
Portfolio project for my Intro to Algorithms class. 

PROMPT: <br>

You are given a 2-D puzzle of size MxN, that has N rows and M column (M and N can be different). Each cell in the puzzle is either empty or has a barrier. An empty cell is marked by ‘-’ (hyphen) and the one with a barrier is marked by ‘#’. You are given two coordinates from the puzzle (a,b) and (x,y). You are currently located at (a,b) and want to reach (x,y). You can move only in the following directions. <br>
L: move to left cell from the current cell<br>
R: move to right cell from the current cell<br>
U: move to upper cell from the current cell<br>
D: move to the lower cell from the current cell <br>

You can move to only an empty cell and cannot move to a cell with a barrier in it. Your goal is to reach the destination cells covering the minimum number of cells as you travel from the starting cell.

SOURCE: <br>

The code in my solve_puzzle function was adapted using code provided to us by the professor for this class. 
The provided code was accessed at this link on 3/5/2023:
https://github.com/DURepo/CS_325_Exercises/blob/main/Graph-calculate_distances.py
The above source lists this link as its original source: 
https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/


EXAMPLE INPUT: <br>

puzzle1 = [ <br>
    ['-', '-', '-', '-', '-'], <br>
    ['-', '-', '#', '-', '-'], <br>
    ['-', '-', '-', '-', '-'], <br>
    ['#', '-', '#', '#', '-'], <br>
    ['-', '#', '-', '-', '-'] <br>
] <br>

print(solve_puzzle(puzzle1, (0, 2), (2, 2))) <br>
print(solve_puzzle(puzzle1, (0, 0), (4, 0))) <br>
