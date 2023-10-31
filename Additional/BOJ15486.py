import sys

N = int(sys.stdin.readline().rstrip())
arr = [[] for _ in range(N)]
for i in range(N):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    arr[i] = tmp

DP = [0 for _ in range(N + 1)]

for i in range(N):
    for j in range(i + arr[i][0], N + 1):
        if DP[j] < DP[i] + arr[i][1]:
            DP[j] = DP[i] + arr[i][1]
print(DP)