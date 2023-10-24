N = int(input())
I = input()
G = input()
TF = [I[i] == G[i] for i in range(N)]

ans = 0
for i in range(N):
    if i == 0:
        if TF[i] and TF[i + 1]:
            continue
        TF[i] = not TF[i]
        TF[i + 1] = not TF[i + 1]
    elif i == N-1:
        if TF[i - 1] and TF[i]:
            continue
        TF[i] = not TF[i]
        TF[i - 1] = not TF[i - 1]
    else:
        if TF[i - 1] and TF[i]:
            continue
        TF[i] = not TF[i]
        TF[i + 1] = not TF[i + 1]
        TF[i - 1] = not TF[i - 1]
    print(TF)