import sys

input = sys.stdin.readline

MAX = sys.maxsize
MIN = -sys.maxsize


def init_min_tree(start, end, node):
    if start == end:
        min_tree[node] = array[start]
        return min_tree[node]
    mid = int((start + end) / 2)
    min_tree[node] = min(init_min_tree(start, mid, node * 2), init_min_tree(mid + 1, end, node * 2 + 1))
    return min_tree[node]


def find_min(start, end, node, left, right):
    if left > end or right < start:
        return MAX
    if left <= start and right >= end:
        return min_tree[node]
    mid = int((start + end) / 2)
    return min(find_min(start, mid, node * 2, left, right), find_min(mid + 1, end, node * 2 + 1, left, right))


N, M = map(int, input().split(" "))
array = []
for _ in range(N):
    array.append(int(input()))

min_tree = [0 for _ in range(N * 4)]
init_min_tree(0, N - 1, 1)

for _ in range(M):
    left, right = map(int, input().split(" "))
    print(find_min(0, N - 1, 1, left - 1, right - 1))

"""
10 4
75
30
100
38
50
51
52
20
81
5
1 10
3 5
6 9
8 10
"""
