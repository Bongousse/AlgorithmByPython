def solution(cards):
    if len(cards) == 1:
        return 1
    cards_sum = [0 for _ in range(len(cards))]
    for i in range(0, len(cards), 2):
        if i - 2 < 0:
            cards_sum[i] = cards[i]
        else:
            cards_sum[i] = cards_sum[i - 2] + cards[i]
    for i in range(1, len(cards), 2):
        if i - 2 < 0:
            cards_sum[i] = cards[i]
        else:
            cards_sum[i] = cards_sum[i - 2] + cards[i]

    cards_reversed_sum = [0 for _ in range(len(cards))]
    for i in range(len(cards) - 1, -1, -2):
        if i + 2 >= len(cards):
            cards_reversed_sum[i] = cards[i]
        else:
            cards_reversed_sum[i] = cards_reversed_sum[i + 2] + cards[i]
    for i in range(len(cards) - 2, -1, -2):
        if i + 2 >= len(cards):
            cards_reversed_sum[i] = cards[i]
        else:
            cards_reversed_sum[i] = cards_reversed_sum[i + 2] + cards[i]

    for i in range(len(cards)):
        if i - 2 >= 0:
            previous_a = cards_sum[i - 2]
        else:
            previous_a = 0
        if i + 1 < len(cards):
            next_a = cards_reversed_sum[i + 1]
        else:
            next_a = 0
        a_sum = previous_a + next_a

        if i - 1 >= 0:
            previous_b = cards_sum[i - 1]
        else:
            previous_b = 0
        if i + 2 < len(cards):
            next_b = cards_reversed_sum[i + 2]
        else:
            next_b = 0
        b_sum = previous_b + next_b
        if a_sum == b_sum:
            return i + 1
    return -1


if __name__ == '__main__':
    # fptr = open(os.environ["OUTPUT_PATH"], "w")
    fptr = open("output.txt", "w")
    cards_count = int(input().strip())
    cards = []
    for _ in range(cards_count):
        cards_item = float(input().strip())
        cards.append(cards_item)

    result = solution(cards)
    fptr.write(str(result) + "\n")
    fptr.close()

"""
4
2
5
3
1

6
2
5
2
7
8
4

"""
