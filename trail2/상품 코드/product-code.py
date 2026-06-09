product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.

class Tkdvna():
    def __init__(self, name = 'codetree', code = 50):
        self.name = name
        self.code = code
    
    def Print(self):
        print(f'product {self.code} is {self.name}')

tkdvna = Tkdvna()
tkdvna.Print()
tkdvna.name = product_name; tkdvna.code = product_code
tkdvna.Print()