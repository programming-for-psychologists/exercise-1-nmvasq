import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units='pix')
red_square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
blue_square = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100])

for i in range(1, 7):
    if i%2 == 1:
        blue_square.draw()
        win.flip()
        core.wait(1)
        win.flip()
        core.wait(.05)
    else:
        red_square.draw()
        win.flip()
        core.wait(1)
        win.flip()
        core.wait(.05)

win.close()
sys.exit()