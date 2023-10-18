n, k = map(int,input().split())
child = list(map(int,input().split()))
DP = [0] * n

for i in range(1, n):
    DP[i] = child[i] - child[i-1]

DP.sort()
print(sum(DP[:n - k + 1]))