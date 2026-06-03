A = input()
B = input()

# Please write your code here.
A = list(A); B = list(B)
b = len(B)
i = 0
while True:
    if not("".join(B) in "".join(A)):
        break
    ck = True
    for j in range(b):
        if A[i+j] != B[j]:
            ck = False
            break
    i += 1
    if ck == True:
        A = A[:i-1]+A[i+b-1:]
        #print("".join(B), "".join(A))
        i = 0
    
    

print(*A, sep = '')
    