import lib_sl
import random
import time

c =	[ [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
          [2,2,2,1,2,1,2,2,1,2,2,2,0,2,2,2,2,2,2,2,2,2,2,2],
          [2,2,2,1,2,2,2,1,2,1,2,2,0,2,2,2,2,2,2,2,2,2,2,2],
          [2,2,1,1,2,1,2,1,1,1,2,2,0,0,2,2,2,0,0,2,2,0,0,2],
          [2,1,2,1,2,1,2,1,2,2,2,2,0,2,0,2,0,2,0,2,0,2,0,2],
          [2,1,1,1,2,1,2,1,1,1,2,2,0,0,0,2,0,0,0,2,0,2,2,2]
	]

idx = 0
cx = 0
while 1:

    for x in range(0,8):
	cx = x + idx;
	if (cx > 23):
	    cx = cx - 24
	    
	for y in range(0,6):	    
	    col = c[y][cx]
	    
	    if (col == 0):
		lib_sl.send(x,y,255,0,0)

	    if (col == 1):
		lib_sl.send(x,y,255,255,255)

	    if (col == 2):
		lib_sl.send(x,y,0,0,0)
    
    time.sleep(0.05)
    
    idx = idx + 1
    if (idx > 23):
	idx = 0