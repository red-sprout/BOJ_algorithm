#BOJ1041 주사위
N = int(input())
dice = list(map(int,input().split()))
one = min(dice)
two = 300
three = 300
for i in range(6):
    for j in range(6):
        if i + j == 5:
            continue
        elif i == j:
            continue
        tmp_two = dice[i] + dice[j]
        if tmp_two < two:
            two = tmp_two
        for k in range(6):
            if i + k == 5 or j + k == 5:
                continue
            elif i == k or j == k:
                continue
            tmp_three = dice[i] + dice[j] + dice[k]
            if tmp_three < three:
                three = tmp_three

if N == 1:
    print(sum(dice) - max(dice))
else:
    print(one * 5 * (N - 2) ** 2 + (two * 8 + one * 4) * (N - 2) + three * 4 + two * 4)