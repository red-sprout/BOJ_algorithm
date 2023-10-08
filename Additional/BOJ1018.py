# 체스판 다시 칠하기
# N행 M열
N, M = map(int,input().split())

arr = []
for i in range(N):
    arr.append(input())

caseB, caseW = 2500, 2500
for row in range(N - 7):
    for col in range(M - 7):
        tmpB, tmpW = 0, 0
        for i in range(8):
            for j in range(8):
                check = (i + j) % 2
                if check == 0:
                    if arr[i + row][j + col] == 'W':
                        tmpB += 1
                    else:
                        tmpW += 1
                else:
                    if arr[i + row][j + col] == 'B':
                        tmpB += 1
                    else:
                        tmpW += 1
        caseB, caseW = min(tmpB, caseB), min(tmpW, caseW)
print(min(caseB, caseW))