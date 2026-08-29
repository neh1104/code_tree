n = int(input())

# Please write your code here.
mm = [-1 for _ in range(n+1)]
sum = [1 for _ in range(n+2 if n > 3 else 4)]
sum[0], sum[1], sum[2] = 1, 3, 10
def dp(curr):
    if mm[curr] != -1:
        return mm[curr]

    if curr == 1:
        mm[curr] = 2
    elif curr == 2:
        mm[curr] = 7
    elif curr == 0:
        mm[curr] = 1
    else:
        mm[curr] = (2*dp(curr-1)+3*dp(curr-2)+2*sum[curr-3])%1000000007
        sum[curr] = sum[curr-1]+mm[curr]
    
    return mm[curr]

print(dp(n))
#print(sum)