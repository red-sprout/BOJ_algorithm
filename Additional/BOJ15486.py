import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

DP = [0 for _ in range(N + 1)]

for i in range(N):
    for j in range(i + arr[i][0], N + 1):
        if DP[j] < DP[i] + arr[i][1]:
            DP[j] = DP[i] + arr[i][1]
print(DP[N])