N = int(input())
str = input()

# Please write your code here.
ls = []
ch_ls = []

for i in range(N):
    for j in range(N-i):
        if not(str[i:i+j+1] in ls):
            ls.append(str[i:i+j+1])
        elif not(len(str[i:i+j+1]) in ch_ls):
            ch_ls.append(len(str[i:i+j+1]))


ch_ls.sort()
#print(ch_ls)
for i in range(len(ch_ls)):
    if i == len(ch_ls)-1:
        print(ch_ls[i]+1)
        break
    if ch_ls[i]+1 != ch_ls[i+1]:
        print(ch_ls[i]+1)
        break
    
        