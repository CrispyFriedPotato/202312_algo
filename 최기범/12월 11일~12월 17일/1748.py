'''
1번째 시도 : Dynamic Programming 기법으로 풀려고 했으나 메모리 초과
2번째 시도 : 반복문 1번 통과(구현) 으로 풀려고 했으나 메모리 초과
3번째 시도 : 규칙 찾기 (10**(숫자의 자릿수) - 1) * (숫자의 자릿수)
'''
# n = int(input())
# d = [0] * (n+1)
# if n < 10 :
#     for i in range(1,n+1) :
#         d[i] = i
# else :
#     for i in range(1,10) :
#         d[i] = i
#     for i in range(10,n+1) :
#         d[i] = d[i-1] + (len(str(i)))
# print(d[n])

# n = int(input())
# result = 0
# for i in range(1,n+1) :
#     result += len(str(i))
# print(result)

n = input()
result = 0
for i in range(1,len(n)) :
    result += 9 * 10 **(i-1) * i 
result += (int(n) - 10 ** (len(n) - 1) + 1) * len(n)
print(result)