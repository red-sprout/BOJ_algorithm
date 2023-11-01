'''
왼쪽 끝에서 오른쪽 끝으로 이동하는데 최소 점프 수, 불가능하면 -1

예제 입력
10
1 2 0 1 3 2 1 5 4 2

예제 출력
5
'''
INF = 1001

N = int(input())
A = list(map(int, input().split()))
DP = [INF] * N

for i in range(N):
    if i == 0:
        DP[i] = 0
        continue
    for j in range(i):
        if i <= j + A[j]:
            DP[i] = min(DP[i], DP[j] + 1)

ans = DP[N-1]
if ans == INF:
    print(-1)
else:
    print(ans)