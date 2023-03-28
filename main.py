from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(2)
    tim.speed(10)


def move_backward():
    tim.backward(1)
    tim.speed(10)


def move_left():
    tim.left(10)


def move_right():
    tim.right(10)


def start_over():
    tim.reset()
    print('I love python!!!')


screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=move_left)
screen.onkey(key='d', fun=move_right)
screen.onkey(key='space', fun=start_over)
screen.exitonclick()
