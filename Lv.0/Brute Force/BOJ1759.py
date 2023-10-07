#수정중
L, C = map(int,input().split())
arr = list(input().split())
arr.sort()

cand = []
check = ['a', 'e', 'i', 'o', 'u']
def dfs(idx):
    global cand
    n = 0
    if len(cand) == L:
        for i in check:
            if i in cand:
                n += 1
        if (n > 0) & (L - n >= 2):
            print(*cand)
        return
    for i in range(idx, C):
        idx = i
        cand.append(arr[idx])
        dfs(idx + 1)
        cand.pop()

dfs(0)