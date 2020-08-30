import sys
#sys.stdin = open('input.txt','r')
n, m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
rt = n-1
lt = 0
while lt <= rt:
    mid = (rt+lt)//2
    if a[mid] == m:
        print(mid+1)
        break
    elif a[mid] > m:
        rt = mid-1
    else:
        lt = mid+1
