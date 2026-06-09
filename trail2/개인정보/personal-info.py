N = 5
name = []
height = []
weight = []

for _ in range(N):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

# Please write your code here.

class People():
    def __init__(self, n, h, w):
        self.name, self.height, self.weight = n, h, w

people = [People(name[i], height[i], weight[i]) for i in range(N)]

people.sort(key = lambda x : x.name)
print('name')
for i in range(N):
    print(people[i].name, people[i].height, round(people[i].weight, 1))

print()
people.sort(key = lambda x : -x.height)
print('height')
for i in range(N):
    print(people[i].name, people[i].height, round(people[i].weight, 1))
