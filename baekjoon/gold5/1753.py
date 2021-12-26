import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split(" "))
start_vertex = int(input())
edge_map = dict()
for _ in range(E):
    u, v, w = map(int, input().split(" "))
    if u not in edge_map:
        edge_map[u] = {}
    edge_map[u][v] = min(edge_map[u].get(v, 10), w)

heap = []
distance = [10 for _ in range(V+1)]
for v, w in edge_map[start_vertex].items():
    heapq.heappush(heap, (w, v))
    distance[v] = w

while len(heap) != 0:
    edge_to_min, min_vertex = heapq.heappop(heap)
    if min_vertex not in edge_map or edge_to_min > distance[min_vertex]:
        continue
    for v, w in edge_map[min_vertex].items():
        if v not in edge_map[start_vertex] or edge_to_min + w < edge_map[start_vertex][v]:
            edge_map[start_vertex][v] = edge_to_min + w
            distance[v] = edge_to_min + w
            heapq.heappush(heap, (edge_to_min + w, v))

for v in range(1, V + 1):
    if start_vertex == v:
        print(0)
    else:
        if v not in edge_map[start_vertex]:
            print("INF")
        else:
            print(edge_map[start_vertex][v])
