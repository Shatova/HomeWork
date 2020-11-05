class Balance:
    def __init__(self):
        self.right = 0
        self.left = 0


    def  add_right(self):
        self.right = int(input())


    def add_left(self):
        self.left = int(input())


    def result(self):
        if self.right == self.left:
            print('=')
        if self.right > self.left:
            print('R')
        if self.right < self.left:
            print('L')
