def solution(cards):
    trade = [True for _ in range(len(cards))]
    for i, card in enumerate(cards):
        if not trade[i]:
            continue
        min_index = card.index(min(card))

        for j, other_card in enumerate(cards[i + 1:], i + 1):
            if not trade[j]:
                continue
            other_min_index = other_card.index(min(other_card))
            if min_index == other_min_index:
                continue
            if card[other_min_index] > card[min_index] + 1 and other_card[min_index] > other_card[other_min_index] + 1:
                trade[i] = trade[j] = False
                card[min_index] += 1
                card[other_min_index] -= 1
                other_card[other_min_index] += 1
                other_card[min_index] -= 1
                break
    answer = 0
    for card in cards:
        answer += min(card)
    return answer


cards = [[10, 5, 15], [5, 15, 10], [10, 11, 9]]
cards = [[10, 5, 15], [8, 9, 13], [10, 10, 10]]
cards = [[8, 11, 11], [6, 15, 9], [14, 2, 14], [8, 20, 2]]
cards = [[8, 11, 11], [10, 7, 13], [15, 10, 5], [7, 17, 6]]
cards = [[0, 0, 30], [30, 0, 0]]
print(solution(cards))
