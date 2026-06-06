a, b = map(int, input().split())

# Please write your code here.

def even(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum % 2 == 0

def sosu(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

cnt = 0 
for i in range(a, b+1):
    if even(i) and sosu(i):
        cnt += 1

print(cnt)