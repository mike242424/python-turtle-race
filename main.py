import turtle as t
import random

screen = t.Screen()
start_message = t.Turtle()
is_playing = False
finish_line = 330
winning_turtle = t.Turtle()
winning_turtle.hideturtle()

user_prediction = screen.textinput('Turtle Race', 'Who will win? (Blue/Red/Green/Orange/Purple/Pink/Black)').lower()
colors = ['red', 'green', 'blue', 'orange', 'purple', 'pink', 'black']
turtles = []


def create_turtles():
    for turtle_index in range(0, 7):
        turtle = t.Turtle('turtle')
        turtles.append(turtle)
        turtle.penup()
        turtle.color(colors[turtle_index])
        turtle.goto(x=-350, y=-200 + turtle_index * 50)


def display_start_message():
    start_message.hideturtle()
    start_message.penup()
    start_message.goto(0, 250)
    start_message.write("Press SPACE to start the game", align="center", font=("Arial", 18, "bold"))


def start_game():
    global winning_turtle
    global is_playing
    is_playing = True
    start_message.clear()

    while is_playing:
        for turtle in turtles:
            turtle.forward(random.randint(0, 10))
            if turtle.xcor() > finish_line:
                is_playing = False
                winning_turtle = turtle
                find_winner()
                return


def find_winner():
    if user_prediction.lower() == winning_turtle.pencolor().lower():
        print(f'You won! The {winning_turtle.pencolor()} turtle is the winner!')
    else:
        print(f'You lost! The {winning_turtle.pencolor()} turtle is the winner.')


create_turtles()
display_start_message()

screen.listen()
screen.onkey(fun=start_game, key='space')
screen.exitonclick()
