str = input()

# Please write your code here.

dt = dict()

for i in str:
    dt[i] = dt.get(i, 0) + 1

for i in dt:
    if dt[i] == 1:
        print(i)
        break
else:
    print('None')