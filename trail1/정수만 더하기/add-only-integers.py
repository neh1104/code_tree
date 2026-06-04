a = input()

sum = 0
for i in a:
    if i.isdigit() == True:
        sum += int(i)

print(sum)