expression = input()

# Please write your code here.
n = len(expression)//2+1
import sys
MAX = -sys.maxsize

mapping = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0}
a = ord('a')

def wornl(curr):
    global MAX
    global mapping
    if curr == a+6:
        MAX = max(MAX, calc())
        return

    for i in range(1, 5):
        mapping[chr(curr)] = i
        wornl(curr+1)

    
def calc():
    s = mapping[expression[0]]
    for i in range(1, n):
        if expression[i*2-1] == '+':
            s += mapping[expression[i*2]]
        elif expression[i*2-1] == '-':
            s -= mapping[expression[i*2]]
        else:
            s *= mapping[expression[i*2]]
    return s

wornl(a)
print(MAX)