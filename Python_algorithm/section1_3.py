import sys
#sys.stdin = open('input.txt','rt')
N, K = map(int, input().split())
a = list(map(int,input().split()))
num = []
for i in range(len(a)):
  for j in range(i+1, len(a)):
    for z in range(j+1,len(a)):
      num.append(a[i]+a[j]+a[z])
num = list(set(num))
num.sort(reverse=True)
print(num[K-1])
