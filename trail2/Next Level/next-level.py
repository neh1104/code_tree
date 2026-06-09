user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.

class Id():
    def __init__(self, id = 'codetree', lv = 10):
        self.id = id
        self.lv = lv

    def Print(self):
        print(f'user {self.id} lv {self.lv}')

id = Id()
id.Print()
id.id = user2_id
id.lv = user2_level
id.Print()