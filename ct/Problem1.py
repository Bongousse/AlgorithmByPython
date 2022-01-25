def getMaximumMex(arr, x):
    # Write your code here
    d = {}
    for item in arr:
        d[item % x] = d.get(item % x, 0) + 1

    answer = 0
    while True:
        if answer not in d:
            if answer - x in d and d[answer - x] > 1:
                d[answer] = d[answer - x] - 1
                d[answer - x] = 1
            else:
                break
        answer += 1
    return answer


if __name__ == '__main__':
    arr = [0, 1, 2, 2, 0, 0, 10, 3]
    x = 3
    print(getMaximumMex(arr, x))
