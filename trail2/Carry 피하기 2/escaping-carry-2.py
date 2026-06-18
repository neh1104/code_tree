n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.

carry = -1
MAX = -1
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            x = str(arr[i])[::-1]
            y = str(arr[j])[::-1]
            z = str(arr[k])[::-1]
            x = x +'00000'
            y = y+'00000'
            z = z+'00000'
            for n1, n2, n3 in zip(x, y, z):
                if int(n1) + int(n2) + int(n3) < 10:
                    carry = int(arr[i]) + int(arr[j]) + int(arr[k])
                    #print('I did!', carry)
                else:
                    #print('I loose..')
                    carry = -1
                    break
            MAX = max(carry, MAX)
            #print('This is MAX', MAX)

print(MAX)