n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

# Please write your code here.

s = set(a)

for i in b:
    print(1 if i in s else 0)