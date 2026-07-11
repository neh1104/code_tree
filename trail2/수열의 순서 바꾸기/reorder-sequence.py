n = int(input())
se = list(map(int, input().split()))

# Please write your code here.
cnt = 1
for i in range(n-1, -1, -1):
    if se[i] > se[i - 1]:
        cnt += 1
    else:
        break

print(n - cnt)