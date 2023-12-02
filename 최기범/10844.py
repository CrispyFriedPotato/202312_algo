n = int(input())
d = [[0] * 10 for _ in range(n+1)]

# 초기값 설정 1일 때, 9
for i in range(1,10) :
  d[1][i] = 1

for i in range(2,n+1) :
  for j in range(10) :
    # 앞에오는 자리의 수가 0 이면 어짜피 결과에 영향을 미치지 않는다.
    if j == 0 :
      d[i][j] = d[i-1][1]
    # 9뒤에는 오직 숫자 8만 올 수 있음 
    elif j == 9 :
      d[i][j] = d[i-1][8]
    else :
      d[i][j] = d[i-1][j-1] + d[i-1][j+1]

print(sum(d[n]) % 1000000000)

