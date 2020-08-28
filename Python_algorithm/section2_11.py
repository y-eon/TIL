import sys
#sys.stdin = open('input.txt','rt')
n = 7
a = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(3):
        if a[i][j] == a[i][j+4] and a[i][j+1] == a[i][j+3]:
            cnt += 1
        if a[j][i] == a[j+4][i] and a[j+1][i] == a[j+3][i]:
            cnt += 1
print(cnt)
