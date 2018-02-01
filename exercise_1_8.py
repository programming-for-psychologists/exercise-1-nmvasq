import time
import sys
from psychopy import visual,event,core

count = 0 
keys = event.getKeys()

win = visual.Window([400,400],color="black", units='pix')
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])

def rotate():
    for i in range(0, 24):
        square.ori += 15
        square.draw()
        win.flip()
        core.wait(.04)
        
def still():
    square.draw()
    win.flip()
    core.wait(1)

event.clearEvents(eventType = 'keyboard')

while 's' not in event.getKeys():
    rotate()
else:
    still()

win.close()
sys.exit()