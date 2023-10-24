import sys

N = int(input())
if N % 2:
    print(0)
    sys.exit(0)

DP = [0] * (N + 1)
DP[2] = 3
for i in range(4, N + 1):
    if i % 2:
        continue
    DP[i] = DP[i-2] + 2 * sum(DP) + 2

print(DP[N])