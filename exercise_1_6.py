import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units='pix')
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
square.setOri(45)
square.draw()
win.flip()
core.wait(1.5)
win.close()
sys.exit()