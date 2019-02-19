

def add_number(x, y, n, s):
    s[y][x] = n
    return 0

array = [['.', '4', '2', '.'], ['.', '.', '4', '.'], ['2', '.', '.', '.'], ['4', '.', '.', '.']]
print(array)
print(add_number(0, 1, '1', array))
print(array)