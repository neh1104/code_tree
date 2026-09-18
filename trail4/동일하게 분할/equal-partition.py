n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

s = sum(arr)
if s%2 == 0:
    dp = set([0])
    for x in arr:
        ndp = set()
        for i in dp:
            if i+x <= s//2:
                ndp.add(i+x)
            if i-x >= -s//2:
                ndp.add(i-x)
        dp = ndp
    #print(dp)
    print('Yes' if 0 in dp else 'No')

else:
    print('No')