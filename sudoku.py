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

# list for all the possible routes
p_rts = []
# start with one route
p_rts.append(init_matrix)

while (completion is not True):
    if (p_rts == []):
        print("SIN SOLUCION")
        break
    for i in range(len(p_rts)):
        print("----------------------------")
        for j in range(0, 4):
            print(p_rts[i][j])
        print("----------------------------")
        if (slib.check_win(p_rts[i]) != 0 | slib.check_empty(p_rts[i]) != 0):

            # get the position that holds most probability of solving problem
            # ----check matrix---- highest value, x, y
            xpos = slib.check_matrix(p_rts[i])[1]
            ypos = slib.check_matrix(p_rts[i])[2]

            # with position get the possible values of the spot
            # ----possible value.....
            possible_values = slib.possible_value(xpos, ypos, p_rts[i])

            # for each value create a new matrix with the newval in position
            # ----create newmat----
            for posval in possible_values:
                tempmat = slib.create_newmat(xpos, ypos, posval, p_rts[i])

            # insert the new matrix in array of possibel values
                p_rts.append(tempmat)

            # remove the old matrix with the old frontier
            p_rts.pop(i)

        if (slib.check_win(p_rts[i]) == 0 and slib.check_empty(p_rts[i]) == 0):
            print("Path Complete")
            for j in range(0, 4):
                print(p_rts[i][j])
            completion = True
