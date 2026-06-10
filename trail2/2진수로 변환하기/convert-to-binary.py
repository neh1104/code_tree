n = int(input())

# Please write your code here.
ls = []
while n >= 2:
    ls.append(n%2)
    n //= 2

ls.append(n%2)

print(*ls[::-1], sep = '')