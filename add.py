#1. class defination 
class Calculator():
    #1. property/variable
    #2. constructor/esp.function
    def __init__(self,x,y):
        self.x=x
        self.y=y
    #3. function/behaviour
    def sum(self):
        print(f'The sum of {self.x} & {self.y} is {self.x+self.y}')
        pass

#2. create class external object
c1=Calculator(10,15)
c1.sum()


