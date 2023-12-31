n = int(input())
d = [0] * (n+1)
result = ["" for _ in range(n+1)]
result[1] = "1"

for i in range(2,n+1) :
    d[i] = d[i-1] + 1
    prev = i - 1
    
    if i % 3 == 0 and d[i//3] + 1 < d[i] :
        d[i] = d[i // 3] + 1
        prev = i // 3
        
    if i % 2 == 0 and d[i//2] + 1 < d[i] :
        d[i] = d[i // 2]  + 1
        prev = i // 3
        
    result[i] = str(i) + " " + result[prev]
    
print(d[n])
print(result[n])

