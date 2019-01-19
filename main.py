import time
from turtle import *

hours = 2
minutes = 59
seconds = 50

t1 = Turtle()

while True:
    t1.clear()
    t1.hideturtle()
    t1.write(str(hours).zfill(2) + ':' + str(minutes).zfill(2) + ':' + str(seconds).zfill(2), font=('aerial', 25, 'normal'))
    seconds = seconds + 1
    time.sleep(1)
    if(seconds == 60):
        seconds = 0
        minutes = minutes + 1
    if(minutes == 60):
        minutes = 0
        hours = hours + 1
    if(hours == 24):
        hours = 0

