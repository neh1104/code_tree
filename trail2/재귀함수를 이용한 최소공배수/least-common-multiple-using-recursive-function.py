n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def insu(n):
    i = 2; ls = []
    while True:
        if n % i == 0:
            ls.append(i)
            n = n // i
        else:
            i += 1
        if n == 1:
            ls.append(1)
            break
    return ls

def cha(a, b):
    for i in b:
        if i in a:
            a.remove(i)
    return a

def wornl(n):
    if n == 1:
        return arr[0]

    ls = cha(insu(wornl(n-1)), insu(arr[n-1]))+insu(arr[n-1])
    prod = 1 
    for i in ls:
        prod *= i
    return prod

print(wornl(n))

#print(insu(5), insu(10), insu(2), insu(6))
#print(cha(insu(5), insu(10)), cha(insu(10), insu(2)))
#prod = 1
#for i in cha([1, 2, 2, 3], (1, 3, 7))+[1, 3, 7]:
#   prod *= i

#print(prod)
