# 보류
N, M = map(int,input().split())
arr = [[0 for j in range(M + 2)] for i in range(N + 2) ]
for i in range(1, N + 1):
    a = list(map(int, input().split()))
    for j in range(1, M + 1):
        arr[i][j] = a[j - 1]

value = []
compare = []
tmp = 0
print(arr)
for i in range(1, N + 1):
    tmp_i = i
    for j in range(1, M + 1):
        tmp_j = j
        tmp = arr[tmp_i][tmp_j]
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    nextone = [arr[tmp_i + 1][tmp_j], arr[tmp_i - 1][tmp_j], arr[tmp_i][tmp_j + 1], arr[tmp_i][tmp_j - 1]]
