# R: 행 수, S: 열 수
# X: 유성의 일부, #: 땅의 일부, .: 공기
# 유성이 땅에 떨어졌을 때, 유성과 땅은 원래 모습 유지
import sys

R, S = map(int,sys.stdin.readline().rstrip().split())
pic, ans = [], [] # 사진
met, land = [-1]*S, [R]*S # 유성의 최하단 좌표, 땅의 최상단 좌표
for i in range(R):
    tmp = list(sys.stdin.readline().rstrip())
    for j in range(S):
        c = tmp[j]
        if c == 'X':
            met[j] = i
        elif c == '#':
            land[j] = min(land[j], i)
    pic.append(tmp)

ans = [['.' for j in range(S)] for i in range(R)]
h = R
for j in range(S):
    if met[j] == -1:
        continue
    tmp = land[j] - met[j] - 1
    h = min(h, tmp)

for i in range(R):
    for j in range(S):
        if pic[i][j] == 'X':
            ans[i+h][j] = pic[i][j]
        elif pic[i][j] == '#':
            ans[i][j] = pic[i][j]

for row in ans:
    print(''.join(row))