secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.

class qlalf:
    def __init__(self, s, m, t):
        self.s = s
        self.m = m
        self.t = t
    

qlalf1 = qlalf(secret_code, meeting_point, time)
print(f'''\
secret code : {qlalf1.s}
meeting point : {qlalf1.m}
time : {qlalf1.t}''')