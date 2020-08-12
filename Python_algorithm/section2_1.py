import sys
#sys.stdin = open('input.txt','rt')
def same_text(x):
  ls = []
  for i in x:
    ls.append(i.upper())
  n = len(ls)
  for i in range(n):
    if ls[i] != ls[n-i-1]:
      print('NO')
      break
  else:
    print('YES')

N = int(input())
for i in range(N):
  a = input()
  print('#{}'.format(i+1),end=' ')
  same_text(a)
