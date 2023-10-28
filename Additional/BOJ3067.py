T = int(input())
for _ in range(T):
    N = int(input())
    coins = [0]
    coins += list(map(int,input().split()))
    M = int(input())
    DP = [[0]*(M+1) for i in range(N+1)]
    DP[0][0] = 1

    for i in range(1, N+1):
        price = coins[i]
        for j in range(0, M+1):
            if price > j:
                DP[i][j] = DP[i-1][j]
            else:
                DP[i][j] = DP[i-1][j] + DP[i][j-price]

    print(DP[N][M])