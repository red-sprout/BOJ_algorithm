# 1,1,2,1,2,3,1,2,3,4,1,2,3,4,5...
# N 이 주어졌을 때 수열의 N번째 수
num = 1
N = int(input())
while True:
    if num >= N:
        break
    N -= num
    num += 1
print(N)