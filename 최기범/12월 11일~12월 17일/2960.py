'''
에라토스 테네스의 체 
1. 2부터 소수를 구하고자 하는 구간의 모든 수를 나열한다.
2. 2의 배수를 지운다
3. 남은 수중 가장 작은 수(3,5,7..)의 배수를 지운다
4. 3의 과정을 반복한다.
5. 소수만 남는다.
'''
n,k = map(int,input().split())
# 숫자 배열 생성
num = [i for i in range(2,n+1)]

# 2 추출
result = num[0]
i = 1

while True  :
    answer = result * i

    if answer in num :
        # 배수를 지운다.
        num.remove(answer)
        k -= 1
        
    if k == 0 :
        print(answer)
        break
    
    # 배수가 n 보다 클 때, 설정
    if answer > n :
        i = 0
        # 리스트의 첫번째 수 추출
        result = num[0]
        
    i += 1
    
    

    
    