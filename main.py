import turtle as t
import random

screen = t.Screen()
finish_line = 335
winning_turtle = t.Turtle()
start_message = t.Turtle()
winning_turtle.hideturtle()
is_playing = True
user_prediction = screen.textinput('Turtle Race', 'Who will win? (Blue/Red/Green/Orange/Purple/Pink/Black)').lower()


def display_start_message():
    start_message.hideturtle()
    start_message.penup()
    start_message.goto(0, 250)
    start_message.write("Press SPACE to start the game", align="center", font=("Arial", 18, "bold"))

def start_game():
    global winning_turtle
    global is_playing
    start_message.clear()
    while is_playing:
        turtle_1.forward(random.randint(1, 30))
        if turtle_1.xcor() > finish_line:
            is_playing = False
            winning_turtle = turtle_1
            find_winner()
            return
        turtle_2.forward(random.randint(1, 30))
        if turtle_2.xcor() > finish_line:
            is_playing = False
            winning_turtle = turtle_2
            find_winner()
            return
        turtle_3.forward(random.randint(1, 30))
        if turtle_3.xcor() > finish_line:
            is_playing = False
            winning_turtle = turtle_3
            find_winner()
            return
        turtle_4.forward(random.randint(1, 30))
        if turtle_4.xcor() > finish_line:
            is_playing = False
            winning_turtle = turtle_4
            find_winner()
            return
        turtle_5.forward(random.randint(1, 30))
        if turtle_5.xcor() > finish_line:
            is_playing = False
            winning_turtle = turtle_5
            find_winner()
            return
        turtle_6.forward(random.randint(1, 30))
        if turtle_6.xcor() > finish_line:
            is_playing = False
            winning_turtle = turtle_6
            find_winner()
            return
        turtle_7.forward(random.randint(1, 30))
        if turtle_7.xcor() > finish_line:
            is_playing = False
            winning_turtle = turtle_7
            find_winner()
            return


def find_winner():
    if user_prediction.lower() == winning_turtle.pencolor().lower():
        print(f'You won! The {winning_turtle.pencolor()} turtle is the winner!')
    else:
        print(f'You lost! The {winning_turtle.pencolor()} turtle is the winner.')


display_start_message()


turtle_1 = t.Turtle()
turtle_1.color('blue')
turtle_1.shape('turtle')
turtle_1.penup()
turtle_1.setheading(-15)
turtle_1.backward(310)
turtle_1.setheading(0)

turtle_2 = t.Turtle()
turtle_2.color('red')
turtle_2.shape('turtle')
turtle_2.penup()
turtle_2.setheading(-10)
turtle_2.backward(305)
turtle_2.setheading(0)

turtle_3 = t.Turtle()
turtle_3.color('green')
turtle_3.shape('turtle')
turtle_3.penup()
turtle_3.setheading(-5)
turtle_3.backward(300)
turtle_3.setheading(0)

turtle_4 = t.Turtle()
turtle_4.color('orange')
turtle_4.shape('turtle')
turtle_4.penup()
turtle_4.setheading(5)
turtle_4.backward(300)
turtle_4.setheading(0)

turtle_5 = t.Turtle()
turtle_5.color('purple')
turtle_5.shape('turtle')
turtle_5.penup()
turtle_5.setheading(10)
turtle_5.backward(305)
turtle_5.setheading(0)

turtle_6 = t.Turtle()
turtle_6.color('pink')
turtle_6.shape('turtle')
turtle_6.penup()
turtle_6.setheading(15)
turtle_6.backward(310)
turtle_6.setheading(0)

turtle_7 = t.Turtle()
turtle_7.color('black')
turtle_7.shape('turtle')
turtle_7.penup()
turtle_7.backward(300)

screen.listen()
screen.onkey(fun=start_game, key='space')
screen.exitonclick()
