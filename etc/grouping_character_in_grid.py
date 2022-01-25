def solution(grid):
    answer = recursive(grid, 0, 0)
    return answer


def recursive(grid, start_i, start_j):
    if is_done(grid):
        if check(grid):
            return 1
        else:
            return 0
    result = 0
    for i in range(len(grid)):
        if i < start_i:
            continue
        for j in range(len(grid[i])):
            if i == start_i and j < start_j:
                continue
            if grid[i][j] == "?":
                grid[i] = grid[i][:j] + "a" + grid[i][j + 1:]
                result += recursive(grid, i, j)
                grid[i] = grid[i][:j] + "b" + grid[i][j + 1:]
                result += recursive(grid, i, j)
                grid[i] = grid[i][:j] + "c" + grid[i][j + 1:]
                result += recursive(grid, i, j)
                grid[i] = grid[i][:j] + "?" + grid[i][j + 1:]
    return result


def is_done(grid):
    for item in grid:
        if "?" in item:
            return False
    return True


def check(grid):
    for c in ["a", "b", "c"]:
        table = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        i, j = find_c(grid, c)
        if i == -1 and j == -1:
            continue
        table[i][j] = 1
        fill_value(grid, table, i, j, c)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == c and table[i][j] == 0:
                    return False
    return True


def find_c(grid, c):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == c:
                return i, j
    return -1, -1


def fill_value(grid, table, i, j, c):
    if i > 0 and grid[i - 1][j] == c and table[i - 1][j] == 0:
        table[i - 1][j] = 1
        fill_value(grid, table, i - 1, j, c)
    if i < len(grid) - 1 and grid[i + 1][j] == c and table[i + 1][j] == 0:
        table[i + 1][j] = 1
        fill_value(grid, table, i + 1, j, c)
    if j > 0 and grid[i][j - 1] == c and table[i][j - 1] == 0:
        table[i][j - 1] = 1
        fill_value(grid, table, i, j - 1, c)
    if j < len(grid[i]) - 1 and grid[i][j + 1] == c and table[i][j + 1] == 0:
        table[i][j + 1] = 1
        fill_value(grid, table, i, j + 1, c)


print(solution(["??b", "abc", "cc?"]))
print(solution(["abcabcab", "????????"]))
print(solution(["aa?"]))
