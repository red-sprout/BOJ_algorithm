# Longest Common Subsequence
import sys
A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()
lA, lB = len(A), len(B)
DP = [[0 for j in range(lB+1)] for i in range(lA+1)]

for i in range(1,lA+1):
    for j in range(1,lB+1):
        if A[i-1] == B[j-1]:
            DP[i][j] = DP[i-1][j-1]+1
        else:
            DP[i][j] = max(DP[i-1][j],DP[i][j-1])


print(DP[lA][lB])