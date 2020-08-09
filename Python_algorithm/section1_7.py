import sys
sys.stdin = open('input.txt','rt')
N = map(int,input())
a = []
for i in range(1, N+1):
  cnt = 0
  for j in range(1,i+1):
    if i%j == 0:
     cnt += 1
    if cnt > 2:
      break
  if cnt == 2:
    a.append(i)
print(len(a))
