import sys
input = sys.stdin.readline

d = [1,2,4,7]
for i in range(int(input())):
    n = int(input())

    for j in range(len(d),n) :
        d.append((d[-3] + d[-2] + d[-1]) % 1000000009)
    print(d[n-1])