'''
15666 N과 M(12)

문제 링크: https://www.acmicpc.net/problem/15666
문제 풀이 일자: 12월 19일
'''

def dfs(n, s, tlst):
    if n==M:
        ans.append(tlst)
        return

    prev = 0
    for j in range(s, N):
        if prev!=lst[j]:
            prev=lst[j]
            dfs(n+1, j, tlst+[lst[j]])

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))

ans = []
dfs(0, 0, [])

for lst in ans:
    print(*lst)