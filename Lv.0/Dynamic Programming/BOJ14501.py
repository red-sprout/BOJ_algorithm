#진행중
N = int(input())
TP = []
for _ in range(N):
    tmp = list(map(int,input().split()))
    TP.append(tmp)

price = 0
def dfs(idx):
    global price
    tmp = 0
    for i in range(idx, N):
        idx = i + TP[i][0]
        if idx > N:
            continue
        tmp = max(tmp, TP[i][0])
    return price

print(dfs(0))