# 8진수를 2진수로 변환
def makeBin(num):
    ans = ''
    for i in range(4):
        tmp = 8 // (2 ** i)
        if num >= tmp:
            ans += '1'
            num -= tmp
        else:
            ans += '0'
    return ans[1:]

n = input()
ans = ''
for i in n:
    ans += makeBin(int(i))

idx = 0
for i in ans:
    if i == '0':
        idx += 1
    else:
        break

print(ans[idx:])