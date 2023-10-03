N = int(input())
A = list(map(int,input().split()))
DP = [1] * N

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            DP[i] = max(DP[i], DP[j] + 1)

l = max(DP)
print(l)

ans = []
for i in range(N-1, -1, -1):
    if DP[i] == l:
        ans.append(A[i])
        l -= 1

ans.reverse()
print(*ans)