import time
import sys
from psychopy import visual,event,core

count = 0 

win = visual.Window([400,400],color="black", units='pix')
red_square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
blu_square = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100])
red_square.pos = (30,0)
blu_square.pos = (-30,0)

def rotate():
    for i in range(0, 96):
        red_square.ori += 7.5/2
        blu_square.ori += -7.5/2
        red_square.draw()
        blu_square.draw()
        win.flip()
        core.wait(.01)

while 'b' not in event.getKeys():
    rotate()

win.close()
sys.exit()