# library for some operations


def check_horizontal(h_array):
    for i in range(len(h_array)):
        for j in range(len(h_array)):
            if (i != j):
                if h_array[i] == h_array[j]:
                    return 1
    return 0


def check_vertical(a, b, c, d):
    v_array = [a, b, c, d]
    for i in range(len(v_array)):
        for j in range(len(v_array)):
            if (i != j):
                if v_array[i] == v_array[j]:
                    return 1
    return 0


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

# tests for the methods
# print(check_horizontal([5, 2, 5, 4]))
# print(check_vertical(1, 2, 3, 4))
