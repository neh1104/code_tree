n, m = map(int, input().split())

# Note: Using 1-based indexing for words as per C++ code
words = [""] + [input() for _ in range(n)]
queries = [input() for _ in range(m)]

# Please write your code here.

dt1 = dict()
dt2 = dict()

for i, str in enumerate(words):
    dt1[i] = str
    dt2[str] = i

for j in queries:
    if j.isalpha():
        print(dt2[j])
    else:
        x = int(j)
        print(dt1[x])