import copy


def fill_virus(array):
    queue = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 2:
                queue.append((i, j))

    while len(queue) != 0:
        x, y = queue.pop()
        array[x][y] = 2
        if x + 1 < len(array) and array[x + 1][y] == 0:
            queue.append((x + 1, y))
        if y + 1 < len(array[x]) and array[x][y + 1] == 0:
            queue.append((x, y + 1))
        if x - 1 >= 0 and array[x - 1][y] == 0:
            queue.append((x - 1, y))
        if y - 1 >= 0 and array[x][y - 1] == 0:
            queue.append((x, y - 1))


def count_safety(array):
    count = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 0:
                count += 1
    return count


def next_safety_position(array, x, y):
    for i in range(x, len(array)):
        if i == x:
            start_j = y + 1
        else:
            start_j = 0
        for j in range(start_j, len(array[i])):
            if array[i][j] == 0:
                return i, j
    return -1, -1


if __name__ == '__main__':
    line = input()
    n, m = map(int, line.split(" "))
    array = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        line = input()
        array[i] = list(map(int, line.split(" ")))

    answer = 0
    first_x, first_y = 0, -1
    while True:
        first_x, first_y = next_safety_position(array, first_x, first_y)
        if (first_x, first_y) == (-1, -1):
            break
        second_x, second_y = first_x, first_y
        while True:
            second_x, second_y = next_safety_position(array, second_x, second_y)
            if (second_x, second_y) == (-1, -1):
                break
            third_x, third_y = second_x, second_y
            while True:
                third_x, third_y = next_safety_position(array, third_x, third_y)
                if (third_x, third_y) == (-1, -1):
                    break
                copy_array = copy.deepcopy(array)
                copy_array[first_x][first_y] = 1
                copy_array[second_x][second_y] = 1
                copy_array[third_x][third_y] = 1
                fill_virus(copy_array)
                count = count_safety(copy_array)
                answer = max(answer, count)
    print(answer)

