def solution(prices, d, k):
    prices.sort()
    print(prices)
    if prices[-1] - prices[0] <= d:
        return int(sum(prices) / len(prices))
    if len(prices) >= 4 and prices[-2] - prices[1] <= d:
        return int(sum(prices[1:-1]) / len(prices[1:-1]))

    index = 0
    while index + k < len(prices):
        if prices[index + k - 1] - prices[index] <= d:
            return int(sum(prices[index:index + k]) / len(prices[index:index + k]))
        index += 1
    if len(prices) % 2 == 0:
        return prices[int(len(prices) / 2) - 1]
    return prices[int(len(prices) / 2)]


prices = [4, 5, 6, 7, 8]
d = 4
k = 3
print(solution(prices, d, k))

prices = [4, 5, 6, 7, 8]
d = 2
k = 1
print(solution(prices, d, k))

prices = [4, 5, 6, 7, 8]
d = 1
k = 2
print(solution(prices, d, k))

prices = [8, 4, 5, 7, 6]
d = 1
k = 3
print(solution(prices, d, k))

prices = [1, 8, 1, 8, 1, 8]
d = 6
k = 4
print(solution(prices, d, k))
