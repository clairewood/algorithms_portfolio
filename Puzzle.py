# Claire Woodford
# 3/5/2023
# CS 325 HW 8

# SOURCE:  
# The solve_puzzle function was adapted from Dijkstra's Algorithm code originally from this source:  
# https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/ 
# The above code was provided by our professor for our usage, with proper citation.
# See README for more details.

import heapq


def valid_move(puzzle, location):
    """
    Takes a 2-D array representing a puzzle and a location in that 2D array
    and returns True if the location is within the bounds of the puzzle, otherwise returns False.

    Location is given in the form of a set, i.e. location would be given as (0, 1),
    which indicates its row and column in the 2D array (puzzle[0][1]).

    The below code repurposed from the valid_neighbor function that I wrote for the MinPuzzle problem last week.
    """
    row, column = location

    if row >= 0 and column >= 0:
        if row < len(puzzle) and column < len(puzzle[0]):
            if puzzle[row][column] != '#':  # if no barrier
                return True
    return False


def retrace_steps(puzzle, source, destination, steps_from_start, path):
    """
    Retraces the path we took to reach the destination node using the  steps_from_start 2-D array.
    Returns the path it found by retracing steps.

    Lines 41-45 make use of code that was repurposed from my MinPuzzle code from last week.
    """
    x, y = destination
    a, b = source
    path.append(destination)

    possible_moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    n, m = x, y # copy destination nodes

    step_val = steps_from_start[n][m]   # We start at the destination nodes
    while n != a or m != b:  # Loop until we've retraced our way back to the source node
        for i, j in possible_moves:
            location = i + n, j + m
            if valid_move(puzzle, location):
                if steps_from_start[i + n][j + m] == step_val - 1:
                    n += i
                    m += j
                    path.append((n, m))
                    step_val = steps_from_start[n][m]
    path.reverse()  # Reverse since they were added to the path in reverse order
    return path


def solve_puzzle(Board, Source, Destination):
    """
    Takes a 2-D puzzle and attempts to find the shortest path from Source to Destination
    (each given as tuples of different indices). The Board contains some barriers (marked with '#')
    that cannot be crossed. The path can only be found by moving left, right, up, or down.

    Returns a list of tuples indicating the indices of each step in the path.
    If no path exists, returns None.
    
    The below code was adapted using code provided to us by the professor for this class. 
    The provided code was accessed at this link on 3/5/2023:
    https://github.com/DURepo/CS_325_Exercises/blob/main/Graph-calculate_distances.py
    The linked source above lists this link as its original source: 
    https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/
    """
    # Changing the name for clarity:
    puzzle = Board
    # Unpacking tuples:
    a, b = Source
    x, y = Destination

    visited = [[False for i in range(len(puzzle[0]))] for j in range(len(puzzle))]
    visited[a][b] = True # Mark source node as visited

    # We'll use the 2-D array below to track how many steps from the first node each node is.
    # Any nodes still marked "None" at the end were inaccessible.
    steps_from_start = [[None for i in range(len(puzzle[0]))] for j in range(len(puzzle))]
    steps_from_start[a][b] = 0  # 0 steps from source node to source node

    steps = 0  # Steps taken so far

    pq = []  # priority queue
    heapq.heappush(pq, (steps, (a, b)))

    while pq:
        steps, current_node = pq.pop(0)
        a, b = current_node  # Unpack tuple for coordinates

        # If we reached the target, we're done!
        if a == x and b == y:
            path = []
            # Retrace our path:
            retrace_steps(puzzle, Source, Destination, steps_from_start, path)
            return path

        # Processing current_node's possible moves from current location
        possible_moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i, j in possible_moves:
            location = a + i, b + j
            if valid_move(puzzle, location):
                if visited[a + i][b + j] is False:
                    steps_from_start[a + i][b + j] = steps + 1
                    heapq.heappush(pq, (steps + 1, location))  # queue steps so far plus location coordinates
                    visited[a + i][b + j] = True # Mark as visited

    # If we looked at every part of the puzzle that we could reach, but we didn't find a path:
    return None


# puzzle1 = [
#     ['-', '-', '-', '-', '-'],
#     ['-', '-', '#', '-', '-'],
#     ['-', '-', '-', '-', '-'],
#     ['#', '-', '#', '#', '-'],
#     ['-', '#', '-', '-', '-']
# ]

# print(solve_puzzle(puzzle1, (0, 2), (2, 2)))
# print(solve_puzzle(puzzle1, (0, 0), (4, 0)))

