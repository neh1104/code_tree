n = int(input())

# Please write your code here.
for i in range(1, 2*n):
    for _ in range(abs(n-i)):
        print(' ', end = '')
    for _ in range(2*n-1 - 2*abs(n-i)):
        print('*', end = '')
    print()
# 1  1
# 2  3
# 3  5
# 4  3
# 5  1