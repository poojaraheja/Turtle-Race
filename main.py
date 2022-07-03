from turtle import Turtle, Screen
import random
tinny = Turtle()
colors = ["red", "yellow", "pink", "green", "red", "brown"]
y_position = [-70, -40, -10 , 20, 50, 80]
screen = Screen()
screen.setup(width=500, height=400)
store = screen.textinput(title="what's  your bat" , prompt="which turtle win the racse ? enter the colour: ")

empty = []


for i in range(5):
    tinny = Turtle()
    tinny.shape("turtle")
    tinny.color(colors[i])
    tinny.penup()
    tinny.goto(x=-230, y=y_position[i])
    empty.append(tinny)

if store:
    is_race_on = True
while is_race_on:
    for turtle in empty:
        if turtle.xcor() > 230:
            is_race_on=False
            pooja = turtle.pencolor()
            if pooja == store:
                print(f"you {store} win!! .{pooja} colour turtle  win the game. ")
            else:
                print(f"you {store} lost. {pooja} colour turtle  win the game. ")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()
# def move_forward():
#     tinny.forward(10)
# def move_backward():
#     tinny.backward(10)
# def move_clockwise():
#     tinny.right(10)
# def move_counter_clockwise():
#     tinny.left(10)
#
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="d", fun=move_clockwise)
# screen.onkey(key="a", fun=move_counter_clockwise)