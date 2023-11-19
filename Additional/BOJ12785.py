import sys
CONST = 1000007

input = lambda: sys.stdin.readline().rstrip()
w, h = map(int, input().split())
x, y = map(int, input().split())

dp1 = [[1 for j in range(x)] for i in range(y)]
dp2 = [[1 for j in range(w-x+1)] for i in range(h-y+1)]

for i in range(y):
    for j in range(x):
        if (i*j == 0): continue
        dp1[i][j] = (dp1[i-1][j] + dp1[i][j-1]) % CONST

for i in range(h-y+1):
    for j in range(w-x+1):
        if (i*j == 0): continue
        dp2[i][j] = (dp2[i-1][j] + dp2[i][j-1]) % CONST

print((dp1[y-1][x-1] * dp2[h-y][w-x]) % CONST)