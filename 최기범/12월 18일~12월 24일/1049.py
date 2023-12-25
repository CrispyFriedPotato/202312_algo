import math

n,m = map(int,input().split())

# 6개 패키지 기타 줄 가격 리스트와 낱개 기타 줄 가격 리스트 선언
guitar_string_package = []
guitar_string_each = []

for _ in range(m) :
    a,b = map(int,input().split())
    guitar_string_package.append(a)
    guitar_string_each.append(b)

# 낮은 가격 순으로 정렬
guitar_string_package.sort()
guitar_string_each.sort()

result = 0

# 기타줄 6개 패키지가 기타줄 낱개 패키지 보다 싼 경우
if guitar_string_package[0] < guitar_string_each[0] * 6 :
    #최대한 싼 기타줄 패키지를 산 후 나머지 줄을 낱개 줄 중 싼 기타 줄로 산다
    result = guitar_string_package[0] * (n // 6) + guitar_string_each[0] * (n % 6)
    # 기타줄 6개 패키지 1개가 가장 싼 낱개 줄의 합들보다 적은 경우 그냥 패키지로 다 산다.
    if guitar_string_package[0] < guitar_string_each[0] * (n % 6) :
        result = guitar_string_package[0] * (math.ceil(n/6))
# 패키지가 더 비싼 경우 낱개로만 산다.
else :
    result = guitar_string_each[0] * n

print(result)

