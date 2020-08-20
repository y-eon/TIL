import sys
#sys.stdin = open('input.txt','rt')
n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
c = a + b
for i in range(n+m):
  for j in range(i,n+m):
    if c[i] > c[j]:
      c[i],c[j] = c[j],c[i]
for i in c:
  print(i,end=' ')
