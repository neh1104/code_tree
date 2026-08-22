k, n = map(int, input().split())

# Please write your code here.

ls = []

def ls_print():
    for i in ls:
        print(i, end = ' ')

def pick(curr_num):
    
    if curr_num == n+1:
        ls_print()
        print()
        return
    
    for i in range(1, k+1):
        ls.append(i)
        pick(curr_num+1)
        ls.pop()

pick(1)