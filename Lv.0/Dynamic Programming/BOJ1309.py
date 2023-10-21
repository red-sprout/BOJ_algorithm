CONST = 9901

N = int(input())
DP = [[0,0,0] for i in range(N+1)]
for i in range(1, N + 1):
    if i == 1:
        DP[i] = [1,1,1]
        continue
    DP[i][0] = (DP[i-1][0] + DP[i-1][1] + DP[i-1][2]) % CONST
    DP[i][1] = (DP[i-1][0] + DP[i-1][2]) % CONST
    DP[i][2] = (DP[i-1][0] + DP[i-1][1]) % CONST
print(sum(DP[N]) % CONST)