# 평범한 배낭
# N: 물품 수, K: 버틸 수 있는 무게, W: 각 물건의 무게, V: 해당 물건의 가치
# 진행중
N, K = map(int,input().split())
cand = []
for i in range(N):
    cand.append(list(map(int,input().split())))