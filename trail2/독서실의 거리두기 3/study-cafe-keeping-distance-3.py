N = int(input())
seats = input()

# Please write your code here.

ch = 0
last = 0
ls = []
for i in range(1, N):
    if seats[i] == '1':
        ln = i - last
        ls.append(ln)
        last = i

ls.sort(reverse = True)
ls[0] //= 2
#print(ls)
print(min(ls))