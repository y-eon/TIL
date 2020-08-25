import sys
#sys.stdin = open('input.txt','rt')
n = int(input())
a = []
a.append([0]*(n+2))
for i in range(n):
    ls = list(map(int,input().split()))
    ls.insert(0,0)
    ls.append(0)
    a.append(ls)
a.append([0]*(n+2))

cnt = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if a[i][j] > max([a[i-1][j],a[i][j-1],a[i+1][j],a[i][j+1]]):
            cnt += 1
print(cnt)
