m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.

ls = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

cnt = 1
while True:
    if m1 == m2 and d1 == d2:
        break
    if d1 == ls[m1-1]:
        d1 = 0
        m1 += 1
    cnt += 1
    d1 += 1
    
    
    

print(cnt)