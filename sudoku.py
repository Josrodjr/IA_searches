#python sudoku.py start=.4.13.4.1..4.21.

import sys

#get the first arg and parse out the start

parsed_string = ''

if str(sys.argv[1]):
  full_string = str(sys.argv[1])
  parsed_string = full_string.replace('start=','')

#parse the empty values located inside the sudoku

for i in range(len(parsed_string)):
  #hear