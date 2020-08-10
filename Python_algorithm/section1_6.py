import sys
#sys.stdin = open('input.txt','rt')
N = map(int,input())
x = list(map(int,input().split()))
def digit_sum(a):
  b = []
  cnt = 0
  while True:
    cnt += a % 10
    a = a // 10
    if a == 0:
      b.append(cnt)
      break
  return b[0]
num = []
for i in x:
  num.append(digit_sum(i))
c = num.index(max(num))
print(x[c])
