n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

s = sum(arr)
if s%2 == 0:
    dp = set([0])
    ch = 0
    for x in arr:
        ndp = set()
        for i in dp:
            if i+x <= s//2:
                ndp.add(i+x)
            if i-x >= -s//2:
                ndp.add(i-x)
        dp = ndp
        if s//2 in dp:
            ch = 1 
            break
    print('Yes' if ch else 'No')
    #print(dp)
    

else:
    print('No')