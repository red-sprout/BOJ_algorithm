import sys
input = lambda: sys.stdin.readline().rstrip()

'''
펠린드롬? -  앞으로 읽으나 뒤로 읽으나 같은 것

S = 1, E = 3인 경우 1, 2, 1은 팰린드롬이다.
S = 2, E = 5인 경우 2, 1, 3, 1은 팰린드롬이 아니다.
S = 3, E = 3인 경우 1은 팰린드롬이다.
S = 5, E = 7인 경우 1, 2, 1은 팰린드롬이다.

예제 입력 1
7
1 2 1 3 1 2 1
4
1 3
2 5
3 3
5 7

예제 출력 1
1
0
1
1
'''
N = int(input())
A = [0] + list(map(int, input().split()))
M = int(input())
cand = [[0 for j in range(N+1)] for i in range(N+1)]
for l in range(1, N + 1):
    for i in range(1, N - l + 2):
        if l == 1:
            cand[i][i] = 1
            continue
        elif l == 2:
            if A[i] == A[i+1]:
                cand[i][i+1] = 1
            continue
        if cand[i+1][i+l-2]:
            if A[i] == A[i+l-1]:
                cand[i][i+l-1] = 1

for _ in range(M):
    S, E = map(int, input().split())
    print(cand[S][E])