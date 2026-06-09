unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.

class Gowo():
    def __init__(self, uc, wc, s):
        self.uc = uc
        self.wc = wc
        self.s = s

    def Print(self):
        print(f'''\
code : {self.uc}
color : {self.wc}
second : {self.s}''')

gowo = Gowo(unlock_code, wire_color, seconds)

gowo.Print()