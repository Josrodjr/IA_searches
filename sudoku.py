# python sudoku.py start=.4.13.4.1..4.21.
# python sudoku.py start=.42...4.2...4...

import sys

import modules.starlib as slib

# get the first arg and parse out the start

parsed_string = ''
# generate the matrix where we will store the starting state
init_matrix = []
completion = False

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

# start the loop of the program
possible_routes = []
# start with one route
possible_routes.append(init_matrix)

# borrar esto
# tx = [['.', '4', '2', '.'], ['1', '.', '4', '.'], ['2', '.', '.', '.'], ['4', '.', '.', '.']]
# ty = [['3', '4', '2', '1'], ['1', '2', '4', '3'], ['2', '3', '1', '4'], ['4', '1', '3', '2']]

# possible_routes.append(ty)

while (completion is not True):
    if (possible_routes == []):
        print("SIN SOLUCION")
        break
    for i in range(len(possible_routes)):
        if (slib.check_win(possible_routes[i]) != 0 | slib.check_empty(possible_routes[i]) != 0):
            # print(possible_routes[i])
            # get the position that holds most probability of solving problem
            # ----check matrix---- highest value, x, y
            xpos = slib.check_matrix(possible_routes[i])[1]
            ypos = slib.check_matrix(possible_routes[i])[2]

            # with position get the possible values of the spot
            # ----possible value.....
            possible_values = slib.possible_value(xpos, ypos, possible_routes[i])

            # for each value create a new matrix with the newval in position
            # ----create newmat----
            for posval in possible_values:
                tempmat = slib.create_newmat(xpos, ypos, posval, possible_routes[i])
            # insert the new matrix in array of possibel values
                possible_routes.append(tempmat)

            # remove the old matrix with the old frontier
            possible_routes.pop(i)

        if (slib.check_win(possible_routes[i]) == 0 and slib.check_empty(possible_routes[i]) == 0):
            print("Path Complete")
            print(possible_routes[i])
            # print(range(len(possible_routes)))
            # for i in range(len(possible_routes)):
            #     print(possible_routes[i])
            completion = True
