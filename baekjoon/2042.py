import sys

input = sys.stdin.readline


def tree_init(start, end, node):
    if start == end:
        tree[node] = array[start]
        return tree[node]
    mid = int((start + end) / 2)
    tree[node] = tree_init(start, mid, node * 2) + tree_init(mid + 1, end, node * 2 + 1)
    return tree[node]


def update(start, end, node, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff
    if start == end:
        return
    mid = int((start + end) / 2)
    update(start, mid, node * 2, index, diff)
    update(mid + 1, end, node * 2 + 1, index, diff)


def sum(start, end, node, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[node]
    mid = int((start + end) / 2)
    return sum(start, mid, node * 2, left, right) + sum(mid + 1, end, node * 2 + 1, left, right)


N, M, K = map(int, input().split(" "))
array = []
for i in range(N):
    array.append(int(input()))

tree = [0 for _ in range(N * 4)]
tree_init(0, N - 1, 1)

for _ in range(M + K):
    a, b, c = map(int, input().split(" "))
    if a == 1:
        update(0, N - 1, 1, b - 1, c - array[b - 1])
        array[b - 1] = c
    if a == 2:
        print(sum(0, N - 1, 1, b - 1, c - 1))

"""
5 2 2
1
2
3
4
5
1 3 6
2 2 5
1 5 2
2 3 5

1 2 2
0
1 1 1
2 1 1
1 1 2
2 1 1
"""
