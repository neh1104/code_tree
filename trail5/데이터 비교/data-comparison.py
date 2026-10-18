n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

# Please write your code here.

s1 = set(arr1)

for i in arr2:
    print(1 if i in s1 else 0, end = ' ')