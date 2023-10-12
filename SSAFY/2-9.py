#BOJ1439
S = input()
zeros = 0
ones = 0

if S[0] =='0':
    zeros += 1
else:
    ones += 1

for i in range(1, len(S)):
    if S[i] == '0' and S[i - 1] != '0':
        zeros += 1
    elif S[i] == '1' and S[i - 1] != '1':
        ones += 1
print(min(zeros, ones))