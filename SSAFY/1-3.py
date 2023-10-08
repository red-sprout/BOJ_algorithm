#BOJ1339
N = int(input())
arr = [['0' for i in range(8)] for j in range(N)]
for i in range(N):
    word = input()
    l = len(word)
    for j in range(7, -1, -1):
        if j <= 7 - l:
            break
        arr[i][j] = word[l + j - 8]

memo = [0 for i in range(26)]
for i in range(N):
    for j in range(7, -1, -1):
        if arr[i][j] == '0':
            break
        memo[ord(arr[i][j]) - ord('A')] += 10 ** (7 - j)

memo.sort(reverse = True)

num = 9
for i in range(26):
    if memo[i] == 0:
        break
    memo[i] = memo[i] * num
    num -= 1

print(sum(memo))