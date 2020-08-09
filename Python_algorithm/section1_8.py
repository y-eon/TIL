def reverse(x):
  cnt = 0
  num = 0
  for i in range(6):
    b = x // 10**(5-i)
    if b != 0:
      x = x - b*(10**(5-i))
      num += b*(10**cnt)
      cnt += 1
  return num

def isPrime(x):
  cnt = 0
  for i in range(1,x+1):
    num = x % i
    if num == 0:
      cnt += 1
    if cnt > 2:
      break
  if cnt == 2:
    return x

N = map(int,input())
a = list(map(int,input().split()))
ls = []
for x in a:
 a = isPrime(reverse(x))
 if a != None:
  print(a,sep='\t')
