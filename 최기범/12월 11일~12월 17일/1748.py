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