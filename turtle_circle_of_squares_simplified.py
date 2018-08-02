import turtle


my_turtle = turtle.Turtle()
my_turtle.speed(0)

# def is to define a function, t_square is the name for turtle square, you have to put brackets after and a colon.

def t_square(length, angle):
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.left(angle)
        
for i in range(5000):
    t_square(100, 90)
    my_turtle.left(11)
