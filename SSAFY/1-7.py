#BOJ1663
DP = [[0,0,0],[1,0,0]]
for i in range(2, 101):
    tmp = []
    tmp.append(DP[i - 1][2])
    tmp.append(DP[i - 1][0])
    tmp.append(DP[i - 1][0] + DP[i - 1][1])
    DP.append(tmp)

ans = ''
cand = ["","X","YZ","ZX"]
def divide(n, k):
    global ans
    if n <= 3:
        ans = cand[n][k - 1]
        return
    else:
        l = sum(DP[n - 3])
        if k <= l:
            divide(n - 3, k)
        else:
            divide(n - 2, k - l)

problem = int(input())
if problem == 1:
    n = int(input())
    print(sum(DP[n]))
elif problem == 2:
    n = int(input())
    k = int(input())
    divide(n, k)
    print(ans)
else:
    n = int(input())
    k = input()
    if k == 'X':
        print(DP[n][0])
    elif k == 'Y':
        print(DP[n][1])
    else:
        print(DP[n][2])