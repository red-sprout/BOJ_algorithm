# 진행중
import copy

n = int(input())
arr = list(map(int,input().split()))
minus = []
ans = 0
for i in range(n):
    if arr[i] < 0:
        minus.append(i)
if len(minus) == 0:
    print(sum(arr))
else:
    for j in minus:
        DP = copy.deepcopy(arr)
        for i in range(1,n):
            if i == j:
                DP[i] = DP[i-1]
                continue
            DP[i] = max(arr[i], arr[i] + DP[i-1])
        tmp = max(DP)
        if ans < tmp:
            ans = tmp
print(ans)