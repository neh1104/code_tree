start, end = map(int, input().split())

# Please write your code here.

cnt = 0
for i in range(start, end+1):
    l_sum = 0
    for j in range(1, i+1):
        if i % j == 0:
            l_sum += 1
        if l_sum > 3:
            break
    if l_sum == 3:
        cnt += 1
print(cnt)