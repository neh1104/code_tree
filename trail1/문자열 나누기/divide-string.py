n = int(input())

x = input().split()

new_x = "".join(x)

cnt = 0 
for i in new_x:
    if cnt == 5:
        print()
        cnt = 0
    print(i,end = '')
    cnt+=1