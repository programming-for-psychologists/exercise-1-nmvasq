import time
import sys
from psychopy import visual,event,core


dicti = {'right': 10, 'left': -10}

win = visual.Window([400,400],color="black", units='pix')
square = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100])

def transform(size):
    square.size += [size,0]
    square.draw()
    win.flip()
    core.wait(.01)
    
square.draw()
win.flip()
core.wait(.01)
        
while 'b' not in event.getKeys():
    transform(dicti[event.waitKeys(keyList = ['left', 'right'])[0]])
    

win.close()
sys.exit()