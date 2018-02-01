import time
import sys
from psychopy import visual,event,core

red_op = 1 
count1 = 0
count2 = 0

win = visual.Window([400,400],color="black", units='pix')
red_square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
blu_square = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100])
red_square.pos = (30,0)
blu_square.pos = (-30,0)

def rotate():
    for i in range(0, 96):
        red_square.ori += 7.5/2
        blu_square.ori += -7.5/2
        global red_op
        global count1
        global count2
        if count1 != 99:
            red_square.setOpacity(red_op)
            blu_square.setOpacity(1-red_op)
            red_op += -.01
            count1 += 1
        else:            
            red_square.setOpacity(red_op)
            blu_square.setOpacity(1-red_op)
            red_op += .01
            count2 += 1
            if count2 == 99:
                count1 = 0
                count2 = 0
        red_square.draw()
        blu_square.draw()
        win.flip()
        core.wait(.01)       

while 'b' not in event.getKeys():
    rotate()

win.close()
sys.exit()