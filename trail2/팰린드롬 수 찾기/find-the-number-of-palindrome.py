X, Y = map(int, input().split())

# Please write your code here.

def pelindrome(n):
    n = str(n)
    half = len(n)//2
    if len(n) % 2 == 0:
        #print(n[half:], n[half-1::-1], 2)
        return n[half:] == n[half-1::-1]
    else:
        #print(n[half+1:], n[half-1::-1], 1)
        return n[half+1:] == n[half-1::-1]

cnt = 0
for i in range(X, Y+1):
    if pelindrome(i):
        cnt += 1

print(cnt)