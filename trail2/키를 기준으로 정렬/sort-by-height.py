n = int(input())
name = []
height = []
weight = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.

class Spec():
    def __init__(self, n, h, w):
        self.n = n
        self.h = h
        self.w = w

spec = [Spec(name[i], height[i], weight[i]) for i in range(n)]

spec.sort(key = lambda x : x.h)

for i in range(n):
    print(f"{spec[i].n} {spec[i].h} {spec[i].w}")
    