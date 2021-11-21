class Rectangle:
    height =100
    width = 100

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def is_square(self):

        if self.height==self.width:
            print(True)
        else:
            print(False)
    def area_square(self):
        S=self.height*self.height
        print(S)
