import sys
#sys.stdin = open('input.txt','rt')
a = input()
num = ''
for x in a:
  if x in ['0','1','2','3','4','5','6','7','8','9']:
    num += x
num = int(num)
print(num)
cnt = 0
for i in range(1,num+1):
  if num % i == 0:
    cnt += 1
print(cnt)
