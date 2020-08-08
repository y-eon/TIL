import sys
sys.stdin = open('input.txt','rt')
N = map(int,input())
num = list(map(int,input().split()))
b = []
for a in num:
  cnt = 0
  while True:
    cnt += a % 10
    a = a // 10
    if a == 0:
      b.append(cnt)
      break
print(num[b.index(max(b))])
