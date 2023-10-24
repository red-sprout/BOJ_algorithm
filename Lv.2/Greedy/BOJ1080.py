import sys

N, M = map(int,input().split())
A, comp = [], [[True for j in range(M)] for i in range(N)]
for i in range(N):
    A.append(input())
for i in range(N):
    tmp = input()
    for j in range(M):
        if tmp[j] != A[i][j]:
            comp[i][j] = False

ans = 0
for i in range(N - 2):
    for j in range(M - 2):
        if comp[i][j]:
            continue
        for row in range(3):
            for col in range(3):
                comp[i + row][j + col] = not comp[i + row][j + col]
        ans += 1

for i in range(N):
    for j in range(M):
        if not comp[i][j]:
            print(-1)
            sys.exit(0)

print(ans)