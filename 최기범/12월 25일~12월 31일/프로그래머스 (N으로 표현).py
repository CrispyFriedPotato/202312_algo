def find_all_mixture(n,k) :
    if n == None :
        return [k,-k]
    return [n-k,n+k,n//k,n*k]

def solution(n,number) :
    if n == number :
        return 1
    
    d = []
    d.append([None])
    d.append([n,-n])
    
    for i in range(1,8) :
        temp = []
        for element in d[i] :
            temp.extend(find_all_mixture(element,n))
            
        multipler = 11
        for k in range(i) :
            for element in d[i-1-k] :
                temp.extend(find_all_mixture(element,n*multipler))
            multipler += 10 ** (k + 2)
            
        if number in temp :
            return i + 1
        d.append(temp)
        
    return -1