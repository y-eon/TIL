import sys
#sys.stdin = open('input.txt','rt')
a = []
m = int(input())
for i in range(m):
  a.append(list(map(int,input().split())))
max = -10000
#가로
for i in range(m):
  if sum(a[i]) > max:
    max = sum(a[i])
#세로
for i in range(m):
  tot = 0
  for j in range(m):
    tot += a[j][i]
  if tot > max:
    max = tot
len_ = int((m+1)/2)
tot1 = 0
tot2 = 0
for i in range(m):
  tot1 += a[i][4-i]
  tot2 += a[i][i]
  if tot1 > max:
    max = tot1
  if tot2 > max:
    max = tot2
print(max)






    
