#python sudoku.py start=.4.13.4.1..4.21.

import sys

#get the first arg and parse out the start

parsed_string = ''
#generate the matrix where we will store the starting state
init_matrix = []

if str(sys.argv[1]):
  full_string = str(sys.argv[1])
  parsed_string = full_string.replace('start=','')

#parse the empty values located inside the sudoku
temporal_arr = []
for i in range(len(parsed_string)):
  j = i+1
  temporal_arr.append(parsed_string[i])
  if (j % 4 == 0):
    init_matrix.append(temporal_arr)
    temporal_arr = []

print(init_matrix[0])