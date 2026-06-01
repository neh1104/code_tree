n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.

mx = max(nums)
for i in range(n):
    if nums.count(mx) > 1:
        nums = [x for x in nums if x != mx]
    
    if len(nums) == 0:
        mx = -1
        break
    mx = max(nums)
print(mx)