n,m = map(int,input().split())
arr =  list(map(int,input().split()))
# 투 포인터 사용
left,right = 0,1
cnt = 0
# right 포인터가 n , left 포인터가 right 포인터가 될 때까지
while right <= n and left <= right :

  sum_val = sum(arr[left : right])

  if sum_val == m :
    cnt += 1
    right += 1
  
  # 값이 m 보다 작으면 right 포인터 이동 
  elif sum_val < m :
    right += 1
  
  # 값이 m 보다 크면 left 포인터 이동 
  else :
    left += 1

print(cnt)