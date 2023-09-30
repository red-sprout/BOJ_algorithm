N = int(input())
arr = [[0, 0, 0]]
for _ in range(N):
    arr.append(list(map(int, input().split())))

DP = [[0, 0, 0], [arr[1][0], arr[1][1], arr[1][2]]]
for i in range(2, N + 1):
    DP.append([min(DP[i - 1][1] + arr[i][0], DP[i - 1][2] + arr[i][0]), min(DP[i - 1][0] + arr[i][1], DP[i - 1][2] + arr[i][1]), min(DP[i - 1][0] + arr[i][2], DP[i - 1][1] + arr[i][2])])
print(min(DP[N]))