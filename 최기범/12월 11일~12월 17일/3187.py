import sys
sys.setrecursionlimit(10**6)
r,c = map(int,input().split())
ground = [list(input().rstrip()) for _ in range(r)]

dx = [0,-1,0,1]
dy = [-1,0,1,0]

visited = [[False] * c for _ in range(r)]

sheep = 0
wolf = 0

def dfs(x,y) :
    global sheep, wolf
    visited[x][y] = True
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c :
            if not visited[nx][ny] :
                if ground[nx][ny] == 'v' :
                    wolf += 1
                    ground[nx][ny] = '.'
                    
                if ground[nx][ny] == 'k' :
                    sheep += 1
                    ground[nx][ny] = '.'
                    
                if ground[nx][ny] == '.' :
                    visited[nx][ny] = True
                    dfs(nx,ny)
        
tot_wolf = 0
tot_sheep = 0 

for i in range(r) :
    for j in range(c) :
        if not visited[i][j] :
            if ground[i][j] == 'v' :
                wolf += 1
                ground[i][j] = '.'
            if ground[i][j] == 'k' :
                sheep += 1
                ground[i][j] = '.'
            if ground[i][j] == '.' :
                dfs(i,j)
                if sheep <= wolf :
                    tot_wolf += wolf
                else :
                    tot_sheep += sheep
                    
                sheep,wolf = 0,0
            
print(tot_sheep,tot_wolf)
        
