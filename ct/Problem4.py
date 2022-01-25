def bitwiseRecurrence(a, b, c, n):
    # Write your code here
    if n < 3:
        if n == 0:
            return a
        elif n == 1:
            return b
        elif n == 2:
            return c
    cache = {}
    cycle_list = []
    for i in range(3, n + 1):
        cache_key_1 = (c, b, a)
        cache_key_2 = (b, c, a)
        if len(cycle_list) != 0 and cache_key_1 == cycle_list[0]:
            answer_key = cycle_list[(n - i) % len(cycle_list)]
            return cache[answer_key]
        if cache_key_1 in cache:
            fi = cache[cache_key_1]
            cycle_list.append(cache_key_1)
        elif cache_key_2 in cache:
            fi = cache[cache_key_2]
        else:
            fi = (c | b) ^ a
            cycle_list = []

        cache[cache_key_1] = fi
        cache[cache_key_2] = fi
        a = b
        b = c
        c = fi
    return c


print(bitwiseRecurrence(4, 1, 10, 50))
print(bitwiseRecurrence(3, 2, 5, 0))
