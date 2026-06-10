m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.

day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def f(m, d):
    cnt = 0; dd = 1; mm = 1
    while True:
        if d == dd and m == mm:
            break
        if dd == month[mm-1]:
            dd = 0
            mm += 1
        dd += 1
        cnt += 1
    
    return cnt

#print(f(m1, d1))
#print(f(m2, d2))
cha = f(m2, d2) - f(m1, d1); d_day = day.index(A)
cha = cha - d_day

print(cha// 7 + 1)