import sys
#sys.stdin = open('input.txt','rt')
N = map(int,input())
a = list(map(int,input().split()))
avg = round(sum(a)/len(a))
min = 10000000
for idx, i in enumerate(a):
  num =abs(avg-i)
  if num < min:
    min = num
    score = i
    res = idx+1
  elif num==min:
    if i > score:
      score = i
      res = idx+1
print(avg, res)
