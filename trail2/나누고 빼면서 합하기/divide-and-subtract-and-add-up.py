n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.

def f(M):
    if M % 2 == 0:
        M //= 2
    else:
        M -= 1
    return M

sum = 0
while m > 0:
    #print(m)
    sum += A[m-1]
    m = f(m)
    

print(sum)