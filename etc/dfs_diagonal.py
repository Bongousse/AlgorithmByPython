def solution(grid):
    global grid_copy, paths, path, g, s, count
    n = len(grid) + 1
    g = [False for _ in range(n)]
    s = [False for _ in range(n)]
    grid_copy = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            path = []
            traverse(grid, i, j)
            paths.append(path)
    recursive(grid, 0)
    return count


paths = []
path = []
g = []
s = []
grid_copy = []
count = 0


def traverse(grid, i, j):
    global path
    path.append((i, j))
    if i == len(grid):
        return
    if j < len(grid):
        if (i + 1, j + 1) not in path and grid[i][j] == "0":
            traverse(grid, i + 1, j + 1)
    if j > 0:
        if (i + 1, j - 1) not in path and grid[i][j - 1] == "1":
            traverse(grid, i + 1, j - 1)
    if i < len(grid):
        if j < len(grid):
            if (i - 1, j + 1) not in path and grid[i-1][j] == "1":
                traverse(grid, i-1,j+1)

dup_p = set()

def recursive(grid, i):
    global g, s, count
    if i == len(grid) + 1:
        p = ""
        for ii in range(len(grid_copy)):
            p += str(grid_copy[ii].index(True))
        dup_p.add(p)
        count += 1
        return
    for j in range(len(grid) + 1):
        if not s[j]:
            found = True
            for sub_path in paths:
                if (i, j) in sub_path:
                    for sub_sub_path in sub_path:
                        if grid_copy[sub_sub_path[0]][sub_sub_path[1]]:
                            found = False
                            break
            if found:
                s[j] = True
                grid_copy[i][j] = True
                recursive(grid, i + 1)
                s[j] = False
                grid_copy[i][j] = False


def search_path(i, j):
    for sub_path in paths:
        if (i, j) in sub_path:
            return sub_path
    return None


grid = ["0010", "0121", "1101", "2000"]
print(solution(grid))

# grid = ["10", "01"]
# print(solution(grid))
