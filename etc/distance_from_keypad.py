def solution(s, keypad):
    keypad_map = {}
    ki = 0
    for i in range(3):
        for j in range(3):
            keypad_map[keypad[ki]] = (i, j)
            ki += 1

    answer = 0
    x, y = keypad_map[s[0]]
    for c in s[1:]:
        next_x, next_y = keypad_map[c]
        answer += max(abs(next_x-x), abs(next_y-y))
        x = next_x
        y = next_y
    return answer


"""
523817
371648295

3999
735194826

13722327
481729356
"""