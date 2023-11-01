'''
첫 번째로 공격받는 SCV는 체력 9를 잃는다.
두 번째로 공격받는 SCV는 체력 3을 잃는다.
세 번째로 공격받는 SCV는 체력 1을 잃는다.
'''
# 진행중
MAX_HP = 61
N = int(input())
SCV = [0] * (3 - N) + list(map(int, input().split()))

DP = [[[-1 for i in range(MAX_HP)] for j in range(MAX_HP)] for k in range(MAX_HP)]
cand = [(1,3,9), (1,9,3), (3,1,9), (3,9,1), (9,1,3), (9,3,1)]
for ele in cand:
    c1, c2, c3 = ele
for i in range(c1 + 1):
    for j in range(c2 + 1):
        for k in range(c3 + 1):
            DP[i][j][k] = 1


'''
입력 1
3
12 10 4
출력 1
2

입력 2
3
54 18 6
출력 2
6

입력 3
1
60
출력 3
7

입력 4
3
1 1 1
출력 4
1

입력 5
2
60 40
출력 5
9
'''