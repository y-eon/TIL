import sys
#sys.stdin = open('input.txt','r')
k,n = map(int, input().split())
a = [int(input()) for _ in range(k)]

def Count(num):
    cnt = 0
    for i in a:
        cnt += (i // num)
    return cnt
res = 0
left = 1
right = max(a)
while left <= right:
    mid = (left+right)//2
    if Count(mid)>= n:
        result = mid
        left = mid+1
    else:
        right = mid-1
print(result)
        
