CONST = 10007

N = int(input())
DP = [[0 for i in range(10)] for j in range(N + 1)]
for i in range(1, N + 1):
    if i == 1:
        DP[i] = [1,1,1,1,1,1,1,1,1,1]
        continue
    for j in range(10):
        DP[i][j] = sum(DP[i-1][j:]) % CONST
print(sum(DP[N]) % CONST)