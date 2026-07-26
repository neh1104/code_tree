a = input()
ls = []; ch = True
for i in a:
    if i == '(':
        ls.append('(')
    else:
        if len(ls) > 0:
            ls.pop()
        else:
            ch = False

if ch == False or len(ls) > 0:
    print('No')
else:
    print('Yes')