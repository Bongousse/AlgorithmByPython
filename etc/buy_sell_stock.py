def solution(prices):
    answer = 0
    is_buy = False
    buy_price = 0
    long_count = 0
    short_count = 0
    for i in range(1, len(prices)):
        if not is_buy and prices[i] > prices[i-1]:
            short_count = 0
            long_count += 1
            if long_count == 3:
                is_buy = True
                buy_price = prices[i]
        elif is_buy and prices[i] < prices[i-1]:
            long_count = 0
            short_count += 1
            if short_count == 3:
                is_buy = False
                answer += prices[i] - buy_price
        else:
            long_count = 0
            short_count = 0
    if is_buy:
        answer += prices[-1] - buy_price
    return answer


print(solution([5, 3, 4, 6, 7, 9, 19, 18, 17, 16, 12, 14, 15, 20, 13]))
print(solution([1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 10, 1]))
print(solution([5, 6, 7, 8]))