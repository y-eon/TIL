import sys
#sys.stdin = open('input.txt','rt')
ls = [i for i in range(1,21)]
for i in range(10):
  a , b = map(int,input().split())
  n = (b-a+1)//2
  for i in range(n):
    ls[a-1+i],ls[b-1-i] = ls[b-1-i],ls[a-1+i]
for i in ls:
  print(i,end = ' ')
