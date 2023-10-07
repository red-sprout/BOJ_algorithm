# 진행중
# A~B 최장거리
# 지점 개수, 간선의 시작점, 간선의 도착적, 간선의 거리, 출발지A, 도착지B
import copy
n = int(input())
arr = []
while True:
    tmp = list(map(int, input().split()))
    if len(tmp) == 3:
        arr.append(tmp)
    else:
        break
A, B = map(int, input().split())

graph = [[0 for i in range(n + 1)] for j in range(n + 1)]
for i in arr:
    graph[i[0]][i[1]] = i[2]
    graph[i[1]][i[0]] = i[2]

scan = copy.deepcopy(graph)