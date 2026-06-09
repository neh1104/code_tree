n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.

nums.sort()

s = 0
for i in range(2*n):
    if nums[i] + nums[2*n-i-1] > s:
        s = nums[i] + nums[2*n-i-1]

print(s)