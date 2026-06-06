n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def abls(n, ls):
    for i in range(n):
        if ls[i] < 0:
            ls[i] *= -1

abls(n, arr)
print(*arr)