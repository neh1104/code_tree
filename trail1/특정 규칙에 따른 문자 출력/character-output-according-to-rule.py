n = int(input())

for i in range(1, 2*n):
    cnt_s = 0
    if i < n:
        cnt_s = n - i
    cnt_a = n-abs(n-i)
    print('  '*cnt_s, '@ '*cnt_a, sep = '')
    