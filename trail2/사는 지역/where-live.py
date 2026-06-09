n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Please write your code here.

class Wkfy():
    def __init__(self, name, add, reg):
        self.name = name
        self.add = add
        self.reg = reg

wkfy = [Wkfy(name[i], street_address[i], region[i]) for i in range(n)]
Name = 'aaaaaaa'; Id = 0
for i in range(n):
    if wkfy[i].name > Name:
        Name = wkfy[i].name
        id = i

print(f'''\
name {wkfy[id].name}
addr {wkfy[id].add}
city {wkfy[id].reg}''')