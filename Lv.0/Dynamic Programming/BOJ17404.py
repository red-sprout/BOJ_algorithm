INF = 1000001

N = int(input())
RGB = []
ans = INF
for i in range(N):
    tmp = list(map(int,input().split()))
    RGB.append(tmp)

for i in range(3):
    DP = []
    for j in range(N):
        tmp = [INF, INF, INF]
        if j == 0:
            DP.append(RGB[j])
            continue
        elif j == 1:
            tmp[i-1] = RGB[j][i-1]+RGB[j-1][i]
            tmp[i-2] = RGB[j][i-2]+RGB[j-1][i]
        else:
            for idx in range(3):
                tmp[idx] = RGB[j][idx] + min(DP[j-1][idx-1], DP[j-1][idx-2])
        DP.append(tmp)
    cand = min(DP[N-1][i-1], DP[N-1][i-2])
    if ans > cand:
        ans = cand
print(ans)