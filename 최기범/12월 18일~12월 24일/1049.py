import math
n,m = map(int,input().split())

guitar_string_package = []
guitar_string = []

for _ in range(m) :
    a,b = map(int,input().split())
    guitar_string_package.append(a)
    guitar_string.append(b)
    
guitar_string_package.sort()
guitar_string.sort()

result = 0

while n > 0 :
    
    if guitar_string[0] * n > guitar_string_package[0] * (math.ceil(n/6)) :
        result += guitar_string_package[0] * (math.ceil(n/6))
        break
        
    if n >= 6 :
        result += guitar_string_package[0]
        n -= 6
    else :
        result += guitar_string[0]
        n -= 1
            
print(result)