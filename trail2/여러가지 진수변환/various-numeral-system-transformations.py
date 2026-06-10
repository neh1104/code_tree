N, B = map(int, input().split())

# Please write your code here.
ls = []
while N >= B:
    ls.append(N%B)
    N //= B
ls.append(N%B)
print(*ls[::-1], sep = '')