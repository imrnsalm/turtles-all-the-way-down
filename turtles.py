from turtle import *

for steps in range(100):
    for tmnt in ('blue', 'red' ,'purple', 'orange'):
        color(tmnt)
        forward(steps)
        left(50)

mainloop()
