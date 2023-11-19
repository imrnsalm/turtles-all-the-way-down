from turtle import *

for steps in range(100):
    for c in ('blue', 'red' ,'purple', 'orange'):
        color(c)
        forward(steps)
        left(50)

mainloop()
