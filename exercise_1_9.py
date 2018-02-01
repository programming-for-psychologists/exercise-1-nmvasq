import time
import sys
from psychopy import visual,event,core

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
    core.wait(.01)

event.clearEvents()

while 's' not in keys:
    rotate()
    keys = event.getKeys() #note that getKeys clears the buffer every time it's called, set var to hold constant
    if 's' in keys:
        still() 
        if 'r' in event.waitKeys(keyList = ['r', 'b']): #note to self, python doesn't like it when you pass one of these commands without entering something
            keys = event.getKeys()
        else:
            break

win.close()
sys.exit()