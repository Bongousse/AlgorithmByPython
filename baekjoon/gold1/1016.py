import math

min, max = map(int, input().split(" "))

i = 2
answer = max - min + 1
table = [0] * answer
while i * i <= max:
    s_num = math.ceil(min / (i*i))
    while s_num * (i * i) <= max:
        if not table[s_num * (i * i) - min]:
            table[s_num * (i * i) - min] = True
            answer -= 1
        s_num += 1
    i += 1
print(answer)
