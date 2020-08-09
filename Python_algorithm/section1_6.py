import sys
sys.stdin = open('input.txt','rt')
N = map(int,input())
x = list(map(int,input().split()))
def digit_sum(x):
b = []
for a in x:
  cnt = 0
  while True:
    cnt += a % 10
    a = a // 10
    if a == 0:
      b.append(cnt)
      break
 return num[b.index(max(b))]
digit_sum(x)
