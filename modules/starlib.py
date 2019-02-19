# library for some operations


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


# get the info of a specific square in the matrix
def info_square(x, y, cs):
    # default to zero
    total_occ = 0
    # check number of information on the horizontal axis
    h_occ = horizontal_info(cs[y])
    # check number of informatio on the vertical axis
    v_occ = vertical_info(cs[0][x], cs[1][x], cs[2][x], cs[3][x])
    total_occ = h_occ + v_occ
    return total_occ


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


# check the number of '.' the array has
def check_empty(cs):
    blank_numbers = 0
    # for i in range(len(cs)):
    #     vertical = [cs[0][i], cs[1][i], cs[2][i], cs[3][i]]
    #     for y1 in vertical:
    #         if y1 == '.':
    #             blank_numbers += 1
    for j in range(len(cs)):
        horizontal = cs[j]
        for x1 in horizontal:
            if x1 == '.':
                blank_numbers += 1
    return blank_numbers

# tests for the methods
# print(check_horizontal([5, 2, 5, 4]))
# print(check_vertical(1, 2, 3, 4))
# print(horizontal_info(['.', '1', '2', '.']))
# print(info_square(0, 1, [['.', '4', '2', '.'], ['.', '.', '4', '.'], ['2', '.', '.', '.'], ['4', '.', '.', '.']]))
print(check_win([['.', '4', '2', '.'], ['.', '.', '4', '.'], ['2', '.', '.', '.'], ['4', '.', '.', '.']]))

# print(possible_value(0, 0, [['.', '4', '2', '.'], ['.', '.', '4', '.'], ['2', '.', '.', '.'], ['4', '.', '.', '.']]))
# array = [['.', '4', '2', '.'], ['.', '.', '4', '.'], ['2', '.', '.', '.'], ['4', '.', '.', '.']]
# print(check_empty(array))