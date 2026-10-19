n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

s = set()
for i in arr:
    s.add(i)

print(len(s))