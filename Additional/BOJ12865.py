# 평범한 배낭
# N: 물품 수, K: 버틸 수 있는 무게, W: 각 물건의 무게, V: 해당 물건의 가치
# 진행중
N, K = map(int,input().split())
DP = [0 for _ in range(K + 1)]
for _ in range(N):
    W, V = map(int,input().split())
    for i in range(K, W - 1, -1):
        DP[i] = max(DP[i], DP[i - W] + V)

print(max(DP))