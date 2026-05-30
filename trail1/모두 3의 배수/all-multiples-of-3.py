arr = [int(input()) for _ in range(5)]

ch = True
for i in arr:
    if i % 3 != 0:
        ch = False

print(1 if ch == True else 0)