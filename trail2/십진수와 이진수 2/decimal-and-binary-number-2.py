N = input()

# Please write your code here.
sum = 0
for i in N:
    sum = sum * 2 + int(i)

sum *= 17

ls = []
while sum >= 2:
    ls.append(sum%2)
    sum //= 2
ls.append(sum%2)

print(*ls[::-1], sep = '')