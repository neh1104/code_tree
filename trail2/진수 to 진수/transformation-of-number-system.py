a, b = map(int, input().split())
n = input()

# Please write your code here.
x = 0
for i in n:
    x = x * a + int(i)

ls = []
while x >= b:
    ls.append(x%b)
    x //= b
ls.append(x%b)

print(*ls[::-1], sep = '')