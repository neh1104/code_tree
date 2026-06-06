A = input()

# Please write your code here.

def alpha_2(arr):
    ls = []
    for i in arr:
        if not(i in ls):
            ls.append(i)
    return 'Yes' if len(ls) >= 2 else 'No'

print(alpha_2(A))