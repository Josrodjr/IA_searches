#library for some operations

def check_horizontal(h_array):
  for i in range(len(h_array)):
    for j in range(len(h_array)):
      if (i != j):
        if h_array[i] == h_array[j]:
          return 1
  return 0

def check_vertical(a,b,c,d):
  v_array = [a,b,c,d]
  for i in range(len(v_array)):
    for j in range(len(v_array)):
      if (i != j):
        if v_array[i] == v_array[j]:
          return 1
  return 0

def check_win(current_state):
  #check verticals
  for i in range(len(current_state)):
    victory = check_vertical(current_state[0][i], current_state[1][i], current_state[2][i], current_state[3][i])
    if victory == 1:
      return 1
  #check horizontals
  for i in range(len(current_state)):
    victory = check_horizontal(current_state[i])
    if victory == 1:
      return 1
  #best case victory
  return 0

#tests for the methods
# print(check_horizontal([5,2,1,4]))
# print(check_vertical(1,4,3,4))