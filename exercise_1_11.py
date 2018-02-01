import time
import sys
from psychopy import visual,event,core

width = 100
dicti = {'right': width/10, 'left': -width/10}

win = visual.Window([400,400],color="black", units='pix')
square = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100])

def transform(size):    
    global width 
    width += size
    square.size += [size,0]
    square.draw()
    win.flip()
    core.wait(.01)
    
square.draw()
win.flip()
core.wait(.01)
        
while 'b' not in event.getKeys():
    dicti = {'right': width/10, 'left': -width/10}
    transform(dicti[event.waitKeys(keyList = ['left', 'right'])[0]])
    

win.close()
sys.exit()