class CircleArea():
    def __init__(self,r):
        self.radius=r
    def area(self):
        print(3.14*self.radius*self.radius)
        pass
    

circle1=CircleArea(r=5)
circle1.area()

