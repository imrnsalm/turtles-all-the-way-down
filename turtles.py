from turtle import *
from random import randrange

# tmnt = ['blue', 'red', 'purple', 'orange']

# for steps in range(100):
#     for t in tmnt:
#         color(t)
#         forward(steps)
#         left(50)

# t1 = Turtle()
# t2 = Turtle()
# t1.color(tmnt[0])
# t2.color(tmnt[1])
# w = 79
# x = 1
# y = 2
# while x <= w:
# 	z = x + y
# 	x = y
# 	y = z

# 	t1.fd(x)
# 	t2.fd(y)

# 	t1.lt(x)
# 	t2.lt(x/2)

# 	t1.bk(y)
# 	t2.bk(x)

# 	t1.rt(y)
# 	t2.rt(y/2)

# '''
#  Plot a tinkerbell map.
# '''

# def chua_circuit():
#     mainloop()

# chua_circuit()

Screen().bgcolor("black")

world_turtle = Turtle()

world_turtle.begin_fill()

world_turtle.color("light yellow")

world_turtle.pensize(10)

world_turtle.left(45)
world_turtle.forward(105)

for i in range(3):
    world_turtle.left(90)
    world_turtle.forward(105)

world_turtle.end_fill()

mainloop()
