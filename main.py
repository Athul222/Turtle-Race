from turtle import Turtle, Screen
from Creating_Multiple_turtles import MakingMultiTurtle
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
colors = ["red", "blue", "violet", "orange", "green", "yellow" ]
#To change the co=ordinates of y using a list
y_position = [70, 40, 10, -20, -50, -80 ]
game_on = True

#creating a list to save the turtles
turtle_list = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y = y_position[turtle_index])
    turtle_list.append(new_turtle)
    
if user_bet:
    game_on = True
    
while game_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230: #250 width where as turtle takes 40 size so (250- (40/2))
            game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Wow You have won the bet. The {turtle.pencolor()} turtle wins")
            else:
                print(f"You lost the bet. The {turtle.pencolor()} turtle wins")
        turtle.forward(random.randint(1, 10))
    
     

screen.listen()
screen.exitonclick()
