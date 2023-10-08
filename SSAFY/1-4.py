# 닫힌 삼각형 공간
# 지점: 4, 간선: 6 -> 닫힌 삼각형 공간 3개
nodes, lines = map(int,input().split())

if nodes >= 3 and lines >= 3:
    makeTwoTriangles = min(nodes - 3, (lines - 3) // 3)
    makeOneTriangle = min(nodes - 3 - makeTwoTriangles, (lines - 3 - 3 * makeTwoTriangles) // 2)
    ans = 1 + 2 * makeTwoTriangles + makeOneTriangle
else:
    ans = 0

print(ans)