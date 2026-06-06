A = input()

# Please write your code here.

def palin(A):
    if A == A[::-1]:
        return 'Yes'
    return "No"

print(palin(A))