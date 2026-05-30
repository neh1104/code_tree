n = int(input())

cmt = 0
for i in range(n):
    if i %2 ==0:
        for j in range(n):
            cmt+=1
            print(cmt, end = ' ')
    else:
        for j in range(n):
            cmt+=2
            print(cmt, end=' ')
  
    print()