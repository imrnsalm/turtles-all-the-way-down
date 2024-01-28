from turtle import *
from random import randrange

tmnt = ['blue', 'red', 'purple', 'orange']

# for steps in range(100):
#     for t in tmnt:
#         color(t)
#         forward(steps)
#         left(50)

w = 79
x = 1
y = 2
while x <= w:
	t = tmnt[randrange(len(tmnt))]
	color(t)
	z = x + y
	x = y
	y = z
	forward(x)
	left(x)
	back(y)
	right(y)

mainloop()
