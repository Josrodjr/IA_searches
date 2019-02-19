# python sudoku.py start=.4.13.4.1..4.21.
# python sudoku.py start=.42...4.2...4...

import sys

import modules.starlib as slib

# get the first arg and parse out the start

parsed_string = ''
# generate the matrix where we will store the starting state
init_matrix = []

if str(sys.argv[1]):
    full_string = str(sys.argv[1])
    parsed_string = full_string.replace('start=', '')

# parse the empty values located inside the sudoku
temporal_arr = []
for i in range(len(parsed_string)):
    j = i+1
    temporal_arr.append(parsed_string[i])
    if (j % 4 == 0):
        init_matrix.append(temporal_arr)
        temporal_arr = []

print(init_matrix)
print(init_matrix[0][1] + " " + init_matrix[1][1] + " " + init_matrix[2][1])

# start the loop of the program
possible_routes = []
# start with one route
possible_routes.append(init_matrix)

# borrar esto
tx = [['.', '4', '2', '.'], ['1', '.', '4', '.'], ['2', '.', '.', '.'], ['4', '.', '.', '.']]
ty = [['3', '4', '2', '1'], ['1', '2', '4', '3'], ['2', '3', '1', '4'], ['4', '1', '3', '2']]

while (slib.check_win(ty) != 0 & slib.check_empty(ty) != 0):
    print("victory")