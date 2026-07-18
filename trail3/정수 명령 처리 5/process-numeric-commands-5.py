N = int(input())

command = []
num = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push_back" or line[0] == "get":
        num.append(int(line[1]))
    else:
        num.append(0)

# Please write your code here.
ls = []
for i in range(N):
    if command[i] == 'push_back':
        ls.append(num[i])
    elif command[i] == 'pop_back':
        ls.pop()
    elif command[i] == 'size':
        print(len(ls))
    else:
        print(ls[num[i] - 1])
