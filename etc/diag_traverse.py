import os


def diag_traverse(matrix):
    i = j = 0
    result = []
    upward = True
    while True:
        result.append(matrix[i][j])
        if i == len(matrix) - 1 and j == len(matrix[0]) - 1:
            break

        if upward:
            if i == 0 and j != len(matrix[0]) - 1:
                j += 1
                upward = False
            elif j == len(matrix[0]) - 1:
                i += 1
                upward = False
            else:
                i -= 1
                j += 1
        else:
            if j == 0 and i != len(matrix) - 1:
                i += 1
                upward = True
            elif i == len(matrix) - 1:
                j += 1
                upward = True
            else:
                i += 1
                j -= 1
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], "w")

    matrix_rows = int(input().strip())
    matrix_columns = int(input().strip())

    matrix = []
    for _ in range(matrix_rows):
        matrix.append(list(map(int, input().rstrip().split())))

    result = diag_traverse(matrix)
    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()

"""
3 
3
1 2 3
4 5 6
7 8 9
"""
