'''
14284 백준 간선 이어가기

문제 링크: https://www.acmicpc.net/problem/14284
문제 풀이 일자: 12월 22일
'''

import heapq

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

s, t = map(int, input().split())

inf = int(21e8)
result = [inf]*(n+1)

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    result[start] = 0

    while heap:
        sk, k = heapq.heappop(heap)
        if sk>result[k]:
            continue
        for i in arr[k]:
            cost = sk + i[1]
            if cost<result[i[0]]:
                result[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))

dijkstra(s)
print(result[t])