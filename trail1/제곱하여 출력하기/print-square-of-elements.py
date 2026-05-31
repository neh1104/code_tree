n = int(input())
arr = list(map(int, input().split()))

print(*[x**2 for x in arr])