import sys
#sys.stdin = open('input.txt','rt')
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
    
tot = 0
half = int((n-1)/2)
for i in range(n):
    if i < half:
        tot += sum(a[i][half-i:n-half+i])
    if i == half:
        tot += sum(a[i])
    if i > half:
        tot += sum(a[i][i-half:half-i])
print(tot)





    

