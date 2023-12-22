# https://youknow301.tistory.com/65 (풀이 참고)
import sys
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
work = [list(map(int,input().split())) for _ in range(2)]
result = 0

def solution(n,m,prev) :
  global result 
  if n == 0 :
    if m <= 0 :
      result += 1
    return 
  for i in range(2) :
    for j in range(3) :
      next_sum = sum
      if j == prev :
        solution(n-1,m-work[i][j]/2,j)
      else :
        solution(n-1,m-work[i][j],j)
      
solution(n,m,-1)
print(result)
