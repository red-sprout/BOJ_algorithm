#BOJ11055
N = int(input())
arr = list(map(int,input().split()))
DP = [arr[i] for i in range(N)]
for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            DP[i] = max(arr[i] + DP[j], DP[i])
print(max(DP))