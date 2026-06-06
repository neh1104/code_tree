a, b = map(int, input().split())

# Please write your code here.
def f_3(n):
    return n % 3 == 0

def f_369(n):
    return set('369') & set(str(n))

sum = 0
for i in range(a,b+1):
    if f_369(i) or f_3(i):
        sum += 1
print(sum)