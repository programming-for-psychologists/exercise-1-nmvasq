import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units='pix')
red_square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
red_square.draw()
win.flip()
core.wait(1) #pause for 1000 ms (one second)
win.flip()
core.wait(1)

for i in range(1, 4):
    red_square.draw()
    win.flip()
    core.wait(.03)
    win.flip()
    core.wait(.05)

win.close()
sys.exit()