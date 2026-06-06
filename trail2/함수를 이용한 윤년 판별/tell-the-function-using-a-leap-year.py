y = int(input())

# Please write your code here.

def isY(n):
    if (n % 100 == 0 and n % 400 != 0) or n % 4 != 0:
        return 'false'
    return 'true'

print(isY(y))