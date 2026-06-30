nums = list(map(int, input().split()))

# Please write your code here.

nums.sort()
a = nums[0]
b = nums[1]
if nums[2] != a+b or nums[2] == nums[3]:
    c = nums[2]
else:
    c = nums[3]

d = nums[-1] -a-b-c
print(a, b, c, d)