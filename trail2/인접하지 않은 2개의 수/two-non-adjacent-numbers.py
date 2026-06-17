n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
MAX = 0
for i in range(n):
    for j in range(i+2, n):
        sum = numbers[i]+numbers[j]
        MAX = max(MAX, sum)

print(MAX)