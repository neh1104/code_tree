n = int(input())

for i in range(1, 2*n):
    cnt = n - abs(i-n)
    print('*' * cnt, end = '')
    print('\n')

# *    1
# **   2
# ***  3
# **   4
# *    5