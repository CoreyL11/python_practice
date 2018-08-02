import turtle


my_turtle = turtle.Turtle()
my_turtle.speed(0)
# def is to define a function, t_square is the name for turtle square, you have to put brackets after and a colon.

def t_square(length, angle):
        my_turtle.forward(length)
        my_turtle.left(angle)
        my_turtle.forward(length)
        my_turtle.left(angle)
        my_turtle.forward(length)
        my_turtle.left(angle)
        my_turtle.forward(length)

for i in range(36):    
    t_square(100, 90)
    my_turtle.left(100)

for i in range(72):
    my_turtle.left(95)
    t_square(100, 90)

for i in range(144):
    my_turtle.left(92.5)
    t_square(100, 90)

for i in range(288):
    my_turtle.left(91.25)
    t_square(100, 90)
