n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.

ls = []
l_ls = -1; cnt = 0
for i in arr:
    if l_ls == -1:
        cnt = 1
        l_ls = i
    else:
        if i != l_ls:
            ls.append(cnt)
            cnt = 1
            l_ls = i
        else:
            cnt += 1
ls.append(cnt)
print(max(ls))