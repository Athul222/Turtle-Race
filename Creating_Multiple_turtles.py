from turtle import Turtle
import random

class MakingMultiTurtle:
    def __init__(self):
        self.temp = ''
    
    def t_movement(self):
        while self.name.xcor(250) != True:
            self.name.forward(random.randint(1,10))
    
            
    def turtle(self, name):
        name = Turtle()
        name.shape("turtle")
        name.penup()
        self.temp = name
        return self.temp
    
    
            