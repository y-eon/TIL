import sys
sys.stdin = open('input.txt','rt')
N = map(int,input())
v1 = list(map(int,input().split()))
v2 = list(map(int,input().split()))
v3 = list(map(int,input().split()))

price_ls = []
def price(a):
  if len(set(a)) == 1:
    price = 10000 + a[0]*1000
  elif len(set(a)) == 2:
    for x in set(a):
      a.remove(x)
    price = 1000 +a[0]*100 
  else:
    price = max(a) * 100
  return price

print(max([price(v1), price(v2), price(v3)]))
