import sys
sys.setrecursionlimit(10**6)

n = int(input())
ground = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * n  for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

# default 1로 설정 한다. (이것때문에 애먹음)
result = [1]

def dfs(x,y,z) :
    visited[x][y] = True
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n  and 0 <= ny < n :
            if ground[nx][ny] > z and not visited[nx][ny] :
                visited[nx][ny] = True
                dfs(nx,ny,z)

for i in range(1,101):  
    cnt = 0
    visited = [[False] * n  for _ in range(n)]  
    for j in range(n) :
        for k in range(n) :
            if ground[j][k] > i and not visited[j][k]:
                dfs(j,k,i)
                cnt += 1
                
    result.append(cnt)
    if cnt == 0 :
        break

print(max(result))