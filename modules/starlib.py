# library for some operations
import copy


# Check_horizontal
# input: array with the horizontal values of the sudoku
# output 1 found repeated values
# output 0 found no repeated values
def check_horizontal(h_array):
    for i in range(len(h_array)):
        for j in range(len(h_array)):
            if (i != j):
                if h_array[i] == h_array[j]:
                    return 1
    return 0


# horizontal_info
# input: array with the horizontal values of the sudoku
# output n ocurrences of values other than '.'
def horizontal_info(h_array):
    ocurrences = 0
    for i in range(len(h_array)):
        if h_array[i] != '.':
            ocurrences += 1
    return ocurrences


# check_vertical
# input: separated values of the vertical square
# output 1 found repeated values
# output 0 found no repeated values
def check_vertical(a, b, c, d):
    v_array = [a, b, c, d]
    for i in range(len(v_array)):
        for j in range(len(v_array)):
            if (i != j):
                if v_array[i] == v_array[j]:
                    return 1
    return 0


# vertical_info
# input: separated values of the vertical square
# output n ocurrences of values other than '.'
def vertical_info(a, b, c, d):
    ocurrences = 0
    v_array = [a, b, c, d]
    for i in range(len(v_array)):
        if v_array[i] != '.':
            ocurrences += 1
    return ocurrences


# check_win
# input: matrix with the complete sudoku
# output 1 still found repeated values
# output 0 found no repeated values
def check_win(cs):
    # check verticals
    for i in range(len(cs)):
        victory = check_vertical(cs[0][i], cs[1][i], cs[2][i], cs[3][i])
        if victory == 1:
            return 1
    # check horizontals
    for i in range(len(cs)):
        victory = check_horizontal(cs[i])
    if victory == 1:
        return 1
    # best case victory
    return 0


# info_square
# get the info of a specific square in the matrix
# input: x, y position of value, matrix with whole sudoku
# number of ocurrencies vertically and horizontally (if '.' = 0)
def info_square(x, y, cs):
    # default to zero
    total_occ = 0
    # check number of information on the horizontal axis
    h_occ = horizontal_info(cs[y])
    # check number of informatio on the vertical axis
    v_occ = vertical_info(cs[0][x], cs[1][x], cs[2][x], cs[3][x])
    total_occ = h_occ + v_occ
    if cs[y][x] != '.':
        return 0
    return total_occ


# possible_value
# input: x, y position of value, matrix with whole sudoku
# possible values of the checked position
def possible_value(x, y, cs):
    values = ['1', '2', '3', '4']
    vertical = [cs[0][x], cs[1][x], cs[2][x], cs[3][x]]
    for y1 in vertical:
        if y1 in values:
            values.remove(y1)
    horizontal = cs[y]
    for x1 in horizontal:
        if x1 in values:
            values.remove(x1)
    return values


# possible_value
# input: x, y position of value, matrix with whole sudoku
# possible values of the checked position
def possible_value2(x, y, cs):
    values = ['1', '2', '3', '4']
    vertical = [cs[0][y], cs[1][y], cs[2][y], cs[3][y]]
    for y1 in vertical:
        if y1 in values:
            values.remove(y1)
    horizontal = cs[x]
    for x1 in horizontal:
        if x1 in values:
            values.remove(x1)
    return values


# check_empty
# check the number of '.' the array has
# output: number of blank spaces
def check_empty(cs):
    blank_numbers = 0
    for j in range(len(cs)):
        horizontal = cs[j]
        for x1 in horizontal:
            if x1 == '.':
                blank_numbers += 1
    return blank_numbers


# check_matrix
# input: matrix with whole sudoku
# highest value in the new matrix of weights
def check_matrix(cs):
    # create an empty matrix of the same dimensions
    temp_matrix = copy.deepcopy(cs)
    for y in range(len(cs)):
        for x in range(len(cs)):
            temp_matrix[y][x] = info_square(x, y, cs)
    return highest_value(temp_matrix)


# highest_value
# input: matrix with sudoku
# highest value of each spot in the sudoku (position and value)
def highest_value(cs):
    highest_value = 0
    x0 = 0
    y0 = 0
    for y in range(len(cs)):
        for x in range(len(cs)):
            if (highest_value < cs[y][x]):
                highest_value = cs[y][x]
                x0 = x
                y0 = y
    return highest_value, x0, y0


# create_newmat
# input: x, y position of value, matrix with whole sudoku, value
# new matrix with the new value inserted
def create_newmat(x, y, val, cs):
    newmat = copy.deepcopy(cs)
    newmat[y][x] = val
    return newmat
