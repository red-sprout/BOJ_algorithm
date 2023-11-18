import sys

input = lambda : sys.stdin.readline().rstrip()
N = int(input())
score = []
for _ in range(N):
    score.append(list(map(int,input().split())))

score.sort(key=lambda x:x[2], reverse=True)
std = score[0][0]
first = [std,score[0][1]]
second = [score[1][0],score[1][1]]
idx = 2
if std == score[1][0]:
    for i in range(2, N):
        if score[i][0] != std:
            idx = i
            break
third = [score[idx][0],score[idx][1]]
print(*first)
print(*second)
print(*third)