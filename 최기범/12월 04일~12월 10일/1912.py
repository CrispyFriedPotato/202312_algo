n = int(input())
arr = list(map(int,input().split()))
d = arr

# 처음 내가 짠 알고리즘
# for i in range(1,n) :
#     for j in range(i) : 
#         d[i] = max(d[i-1] + arr[i], sum(arr[j : i+1]))

# 알고리즘 개선 (반복문 1번)
for i in range(1,n) :
    # 이전 까지의 데이터 합이 , i 번째 데이터의 합보다 큰 경우 i 번째 숫자를 최대값으로 설정
    d[i] = max(d[i] , d[i] + d[i-1])

print(max(d))
        
    