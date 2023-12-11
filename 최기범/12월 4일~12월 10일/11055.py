''' LIS(Longest Inrease Subsequence) 문제  
최장 증가 부분 수열을 찾아야 한다. 
점화식)  
배열 a에 대하여 모든 0 <= j < i [j < i < len(a)]에 대하여, 
a[i] > a[j] 일 때,
d[i] = max(d[i],d[j] + 1)
'''

n = int(input())
a = list(map(int,input().split()))
'''Dynamic Programming을 위한 저장 값 범위 설정(배열 크기 만큼(n))
d 에는 부분 증가 배열의 합을 저장한다
'''
d = [0] * n
# 초기값 설정 
d[0] = a[0]

for i in range(n) :
      for j in range(i) :
            '''
             a[i]가 a[j] 보다 클 때,
             d[j]가 더 큰 지 아니면,
             a[i]를 추가한 d[j] 이 더 큰 지, 판별하여 최신화
            '''
            if a[i] > a[j] :
                  d[i] = max(d[i] , d[j] + a[i])
                  
            else :
                  d[i] = max(d[i], a[i])
                  
print(max(d))      

