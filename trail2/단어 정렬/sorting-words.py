n = int(input())
word = [input() for _ in range(n)]

# Please write your code here.

word.sort()

print(*word, sep = '\n')