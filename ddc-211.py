# 211
import lib_sl
import random
import time

cs = [[255,255,000,000,000,255],[000,255,255,255,000,000],[000,000,000,255,255,255]]

def rc():
  return random.randint(0,5)

def rid():
    return [random.randint(0,8),random.randint(0,6)]


while 1:
# HAPPY ? SCROLL RIGHT IN LEFT OUT, WAIT
## CLEAR AND WAIT
    lib_sl.send(0,0,0,0,0)
    lib_sl.send(0,1,0,0,0)
    lib_sl.send(0,2,0,0,0)
    lib_sl.send(0,3,0,0,0)
    lib_sl.send(0,4,0,0,0)
    lib_sl.send(0,5,0,0,0)
    lib_sl.send(0,6,0,0,0)
    lib_sl.send(0,7,0,0,0)
    lib_sl.send(1,0,0,0,0)
    lib_sl.send(1,1,0,0,0)
    lib_sl.send(1,2,0,0,0)
    lib_sl.send(1,3,0,0,0)
    lib_sl.send(1,4,0,0,0)
    lib_sl.send(1,5,0,0,0)
    lib_sl.send(1,6,0,0,0)
    lib_sl.send(1,7,0,0,0)
    lib_sl.send(2,0,0,0,0)
    lib_sl.send(2,1,0,0,0)
    lib_sl.send(2,2,0,0,0)
    lib_sl.send(2,3,0,0,0)
    lib_sl.send(2,4,0,0,0)
    lib_sl.send(2,5,0,0,0)
    lib_sl.send(1,6,0,0,0)
    lib_sl.send(1,7,0,0,0)
    lib_sl.send(3,0,0,0,0)
    lib_sl.send(3,1,0,0,0)
    lib_sl.send(3,2,0,0,0)
    lib_sl.send(3,3,0,0,0)
    lib_sl.send(3,4,0,0,0)
    lib_sl.send(3,5,0,0,0)
    lib_sl.send(1,6,0,0,0)
    lib_sl.send(1,7,0,0,0)
    lib_sl.send(4,0,0,0,0)
    lib_sl.send(4,1,0,0,0)
    lib_sl.send(4,2,0,0,0)
    lib_sl.send(4,3,0,0,0)
    lib_sl.send(4,4,0,0,0)
    lib_sl.send(4,5,0,0,0)
    lib_sl.send(1,6,0,0,0)
    lib_sl.send(1,7,0,0,0)
    lib_sl.send(5,0,0,0,0)
    lib_sl.send(5,1,0,0,0)
    lib_sl.send(5,2,0,0,0)
    lib_sl.send(5,3,0,0,0)
    lib_sl.send(5,4,0,0,0)
    lib_sl.send(5,5,0,0,0)
    lib_sl.send(5,6,0,0,0)
    lib_sl.send(5,7,0,0,0)
    time.sleep(10.0)
# H1
    lib_sl.send(0,4,255,0,0)
    lib_sl.send(0,5,255,0,0)
    lib_sl.send(1,5,255,0,0)
    lib_sl.send(7,4,255,0,0)
    lib_sl.send(6,5,255,0,0)
    lib_sl.send(7,5,255,0,0)
    time.sleep(5.0)
    lib_sl.send(0,4,0,0,0)
    lib_sl.send(0,5,0,0,0)
    lib_sl.send(1,5,0,0,0)
    lib_sl.send(7,4,0,0,0)
    lib_sl.send(6,5,0,0,0)
    lib_sl.send(7,5,0,0,0)
# H12
    lib_sl.send(1,4,255,0,0)
    lib_sl.send(2,4,255,0,0)
    lib_sl.send(2,5,255,0,0)
    lib_sl.send(3,4,255,0,0)
    lib_sl.send(3,5,255,0,0)
    lib_sl.send(4,4,255,0,0)
    lib_sl.send(4,5,255,0,0)
    lib_sl.send(5,4,255,0,0)
    lib_sl.send(5,5,255,0,0)
    lib_sl.send(6,4,255,0,0)
    time.sleep(5.0)
    lib_sl.send(1,4,0,0,0)
    lib_sl.send(2,4,0,0,0)
    lib_sl.send(2,5,0,0,0)
    lib_sl.send(3,4,0,0,0)
    lib_sl.send(3,5,0,0,0)
    lib_sl.send(4,4,0,0,0)
    lib_sl.send(4,5,0,0,0)
    lib_sl.send(5,4,0,0,0)
    lib_sl.send(5,5,0,0,0)
    lib_sl.send(6,4,0,0,0)
# H
    lib_sl.send(6,2,255,0,0)
    lib_sl.send(7,2,255,0,0)
    lib_sl.send(7,3,255,0,0)
    lib_sl.send(0,2,255,0,0)
    lib_sl.send(0,3,255,0,0)
    lib_sl.send(1,2,255,0,0)
    lib_sl.send(3,4,255,0,0)
    lib_sl.send(3,5,255,0,0)
    lib_sl.send(4,4,255,0,0)
    lib_sl.send(4,5,255,0,0)
    lib_sl.send(7,4,255,0,0)
    lib_sl.send(6,5,255,0,0)
    lib_sl.send(7,5,255,0,0)
    lib_sl.send(0,4,255,0,0)
    lib_sl.send(0,5,255,0,0)
    lib_sl.send(1,5,255,0,0)
    time.sleep(5.0)
    lib_sl.send(6,2,0,0,0)
    lib_sl.send(7,2,0,0,0)
    lib_sl.send(7,3,0,0,0)
    lib_sl.send(0,2,0,0,0)
    lib_sl.send(0,3,0,0,0)
    lib_sl.send(1,2,0,0,0)
    lib_sl.send(3,4,0,0,0)
    lib_sl.send(3,5,0,0,0)
    lib_sl.send(4,4,0,0,0)
    lib_sl.send(4,5,0,0,0)
    lib_sl.send(7,4,0,0,0)
    lib_sl.send(6,5,0,0,0)
    lib_sl.send(7,5,0,0,0)
    lib_sl.send(0,4,0,0,0)
    lib_sl.send(0,5,0,0,0)
    lib_sl.send(1,5,0,0,0)
# H,[SPACE]
    lib_sl.send(1,3,255,0,0)
    lib_sl.send(2,2,255,0,0)
    lib_sl.send(2,3,255,0,0)
    lib_sl.send(3,2,255,0,0)
    lib_sl.send(3,3,255,0,0)
    lib_sl.send(4,2,255,0,0)
    lib_sl.send(4,3,255,0,0)
    lib_sl.send(5,2,255,0,0)
    lib_sl.send(5,3,255,0,0)
    lib_sl.send(6,3,255,0,0)
    lib_sl.send(1,4,255,0,0)
    lib_sl.send(2,4,255,0,0)
    lib_sl.send(2,5,255,0,0)
    lib_sl.send(3,4,255,0,0)
    lib_sl.send(3,5,255,0,0)
    lib_sl.send(4,4,255,0,0)
    lib_sl.send(4,5,255,0,0)
    lib_sl.send(5,4,255,0,0)
    lib_sl.send(5,5,255,0,0)
    lib_sl.send(6,4,255,0,0)
    time.sleep(5.0)
    lib_sl.send(1,3,0,0,0)
    lib_sl.send(2,2,0,0,0)
    lib_sl.send(2,3,0,0,0)
    lib_sl.send(3,2,0,0,0)
    lib_sl.send(3,3,0,0,0)
    lib_sl.send(4,2,0,0,0)
    lib_sl.send(4,3,0,0,0)
    lib_sl.send(5,2,0,0,0)
    lib_sl.send(5,3,0,0,0)
    lib_sl.send(6,3,0,0,0)
    lib_sl.send(1,4,0,0,0)
    lib_sl.send(2,4,0,0,0)
    lib_sl.send(2,5,0,0,0)
    lib_sl.send(3,4,0,0,0)
    lib_sl.send(3,5,0,0,0)
    lib_sl.send(4,4,0,0,0)
    lib_sl.send(4,5,0,0,0)
    lib_sl.send(5,4,0,0,0)
    lib_sl.send(5,5,0,0,0)
    lib_sl.send(6,4,0,0,0)
# H,[SPACE],A1
    lib_sl.send(0,0,255,0,0)
    lib_sl.send(0,1,255,0,0)
    lib_sl.send(1,0,255,0,0)
    lib_sl.send(6,0,255,0,0)
    lib_sl.send(7,0,255,0,0)
    lib_sl.send(7,1,255,0,0)
    lib_sl.send(3,2,255,0,0)
    lib_sl.send(3,3,255,0,0)
    lib_sl.send(4,2,255,0,0)
    lib_sl.send(4,3,255,0,0)
    lib_sl.send(6,2,255,0,0)
    lib_sl.send(7,2,255,0,0)
    lib_sl.send(7,3,255,0,0)
    lib_sl.send(0,2,255,0,0)
    lib_sl.send(0,3,255,0,0)
    lib_sl.send(1,2,255,0,0)
    lib_sl.send(7,4,255,0,0)
    lib_sl.send(6,5,255,0,0)
    lib_sl.send(7,5,255,0,0)
    lib_sl.send(0,4,255,0,0)
    lib_sl.send(0,5,255,0,0)
    lib_sl.send(1,5,255,0,0)
    time.sleep(5.0)
    lib_sl.send(0,0,0,0,0)
    lib_sl.send(0,1,0,0,0)
    lib_sl.send(1,0,0,0,0)
    lib_sl.send(6,0,0,0,0)
    lib_sl.send(7,0,0,0,0)
    lib_sl.send(7,1,0,0,0)
    lib_sl.send(3,2,0,0,0)
    lib_sl.send(3,3,0,0,0)
    lib_sl.send(4,2,0,0,0)
    lib_sl.send(4,3,0,0,0)
    lib_sl.send(6,2,0,0,0)
    lib_sl.send(7,2,0,0,0)
    lib_sl.send(7,3,0,0,0)
    lib_sl.send(0,2,0,0,0)
    lib_sl.send(0,3,0,0,0)
    lib_sl.send(1,2,0,0,0)
    lib_sl.send(7,4,0,0,0)
    lib_sl.send(6,5,0,0,0)
    lib_sl.send(7,5,0,0,0)
    lib_sl.send(0,4,0,0,0)
    lib_sl.send(0,5,0,0,0)
    lib_sl.send(1,5,0,0,0)
# H,[SPACE],A12
    lib_sl.send(1,1,255,0,0)
    lib_sl.send(2,0,255,0,0)
    lib_sl.send(2,1,255,0,0)
    lib_sl.send(3,0,255,0,0)
    lib_sl.send(3,1,255,0,0)
    lib_sl.send(4,0,255,0,0)
    lib_sl.send(4,1,255,0,0)
    lib_sl.send(5,0,255,0,0)
    lib_sl.send(5,1,255,0,0)
    lib_sl.send(6,1,255,0,0)
    lib_sl.send(1,3,255,0,0)
    lib_sl.send(2,2,255,0,0)
    lib_sl.send(2,3,255,0,0)
    lib_sl.send(3,2,255,0,0)
    lib_sl.send(3,3,255,0,0)
    lib_sl.send(4,2,255,0,0)
    lib_sl.send(4,3,255,0,0)
    lib_sl.send(5,2,255,0,0)
    lib_sl.send(5,3,255,0,0)
    lib_sl.send(6,3,255,0,0)
    lib_sl.send(1,4,255,0,0)
    lib_sl.send(2,4,255,0,0)
    lib_sl.send(2,5,255,0,0)
    lib_sl.send(3,4,255,0,0)
    lib_sl.send(3,5,255,0,0)
    lib_sl.send(4,4,255,0,0)
    lib_sl.send(4,5,255,0,0)
    lib_sl.send(5,4,255,0,0)
    lib_sl.send(5,5,255,0,0)
    lib_sl.send(6,4,255,0,0)
    lib_sl.send(7,4,255,0,0)
    lib_sl.send(6,5,255,0,0)
    lib_sl.send(7,5,255,0,0)
    time.sleep(5.0)
    lib_sl.send(1,1,0,0,0)
    lib_sl.send(2,0,0,0,0)
    lib_sl.send(2,1,0,0,0)
    lib_sl.send(3,0,0,0,0)
    lib_sl.send(3,1,0,0,0)
    lib_sl.send(4,0,0,0,0)
    lib_sl.send(4,1,0,0,0)
    lib_sl.send(5,0,0,0,0)
    lib_sl.send(5,1,0,0,0)
    lib_sl.send(6,1,0,0,0)
    lib_sl.send(1,3,0,0,0)
    lib_sl.send(2,2,0,0,0)
    lib_sl.send(2,3,0,0,0)
    lib_sl.send(3,2,0,0,0)
    lib_sl.send(3,3,0,0,0)
    lib_sl.send(4,2,0,0,0)
    lib_sl.send(4,3,0,0,0)
    lib_sl.send(5,2,0,0,0)
    lib_sl.send(5,3,0,0,0)
    lib_sl.send(6,3,0,0,0)
    lib_sl.send(1,4,0,0,0)
    lib_sl.send(2,4,0,0,0)
    lib_sl.send(2,5,0,0,0)
    lib_sl.send(3,4,0,0,0)
    lib_sl.send(3,5,0,0,0)
    lib_sl.send(4,4,0,0,0)
    lib_sl.send(4,5,0,0,0)
    lib_sl.send(5,4,0,0,0)
    lib_sl.send(5,5,0,0,0)
    lib_sl.send(6,4,0,0,0)
    lib_sl.send(7,4,0,0,0)
    lib_sl.send(6,5,0,0,0)
    lib_sl.send(7,5,0,0,0)
# H23,[SPACE],A
    lib_sl.send(3,0,255,0,0)
    lib_sl.send(3,1,255,0,0)
    lib_sl.send(4,0,255,0,0)
    lib_sl.send(4,1,255,0,0)
    lib_sl.send(0,0,255,0,0)
    lib_sl.send(0,1,255,0,0)
    lib_sl.send(1,0,255,0,0)
    lib_sl.send(6,0,255,0,0)
    lib_sl.send(7,0,255,0,0)
    lib_sl.send(7,1,255,0,0)
    lib_sl.send(0,2,255,0,0)
    lib_sl.send(0,3,255,0,0)
    lib_sl.send(1,2,255,0,0)
    lib_sl.send(6,2,255,0,0)
    lib_sl.send(7,2,255,0,0)
    lib_sl.send(7,3,255,0,0)
    lib_sl.send(3,4,255,0,0)
    lib_sl.send(3,5,255,0,0)
    lib_sl.send(4,4,255,0,0)
    lib_sl.send(4,5,255,0,0)
    lib_sl.send(5,4,255,0,0)
    lib_sl.send(5,5,255,0,0)
    lib_sl.send(6,4,255,0,0)
    lib_sl.send(0,4,255,0,0)
    lib_sl.send(0,5,255,0,0)
    lib_sl.send(1,5,255,0,0)
    lib_sl.send(7,4,255,0,0)
    lib_sl.send(6,5,255,0,0)
    lib_sl.send(7,5,255,0,0)
    time.sleep(5.0)
    lib_sl.send(3,0,0,0,0)
    lib_sl.send(3,1,0,0,0)
    lib_sl.send(4,0,0,0,0)
    lib_sl.send(4,1,0,0,0)
    lib_sl.send(0,0,0,0,0)
    lib_sl.send(0,1,0,0,0)
    lib_sl.send(1,0,0,0,0)
    lib_sl.send(6,0,0,0,0)
    lib_sl.send(7,0,0,0,0)
    lib_sl.send(7,1,0,0,0)
    lib_sl.send(0,2,0,0,0)
    lib_sl.send(0,3,0,0,0)
    lib_sl.send(1,2,0,0,0)
    lib_sl.send(6,2,0,0,0)
    lib_sl.send(7,2,0,0,0)
    lib_sl.send(7,3,0,0,0)
    lib_sl.send(3,4,0,0,0)
    lib_sl.send(3,5,0,0,0)
    lib_sl.send(4,4,0,0,0)
    lib_sl.send(4,5,0,0,0)
    lib_sl.send(5,4,0,0,0)
    lib_sl.send(5,5,0,0,0)
    lib_sl.send(6,4,0,0,0)
    lib_sl.send(0,4,0,0,0)
    lib_sl.send(0,5,0,0,0)
    lib_sl.send(1,5,0,0,0)
    lib_sl.send(7,4,0,0,0)
    lib_sl.send(6,5,0,0,0)
    lib_sl.send(7,5,0,0,0)
# H3,[SPACE],A,[SPACE]
    lib_sl.send(1,1,255,0,0)
    lib_sl.send(2,0,255,0,0)
    lib_sl.send(2,1,255,0,0)
    lib_sl.send(3,0,255,0,0)
    lib_sl.send(3,1,255,0,0)
    lib_sl.send(4,0,255,0,0)
    lib_sl.send(4,1,255,0,0)
    lib_sl.send(5,0,255,0,0)
    lib_sl.send(5,1,255,0,0)
    lib_sl.send(6,1,255,0,0)
    lib_sl.send(1,3,255,0,0)
    lib_sl.send(2,2,255,0,0)
    lib_sl.send(2,3,255,0,0)
    lib_sl.send(3,2,255,0,0)
    lib_sl.send(3,3,255,0,0)
    lib_sl.send(4,2,255,0,0)
    lib_sl.send(4,3,255,0,0)
    lib_sl.send(5,2,255,0,0)
    lib_sl.send(5,3,255,0,0)
    lib_sl.send(6,3,255,0,0)
    lib_sl.send(6,2,255,0,0)
    lib_sl.send(7,2,255,0,0)
    lib_sl.send(7,3,255,0,0)
    lib_sl.send(1,4,255,0,0)
    lib_sl.send(2,4,255,0,0)
    lib_sl.send(2,5,255,0,0)
    lib_sl.send(3,4,255,0,0)
    lib_sl.send(3,5,255,0,0)
    lib_sl.send(4,4,255,0,0)
    lib_sl.send(4,5,255,0,0)
    lib_sl.send(5,4,255,0,0)
    lib_sl.send(5,5,255,0,0)
    lib_sl.send(6,4,255,0,0)
    time.sleep(5.0)
    lib_sl.send(1,1,0,0,0)
    lib_sl.send(2,0,0,0,0)
    lib_sl.send(2,1,0,0,0)
    lib_sl.send(3,0,0,0,0)
    lib_sl.send(3,1,0,0,0)
    lib_sl.send(4,0,0,0,0)
    lib_sl.send(4,1,0,0,0)
    lib_sl.send(5,0,0,0,0)
    lib_sl.send(5,1,0,0,0)
    lib_sl.send(6,1,0,0,0)
    lib_sl.send(1,3,0,0,0)
    lib_sl.send(2,2,0,0,0)
    lib_sl.send(2,3,0,0,0)
    lib_sl.send(3,2,0,0,0)
    lib_sl.send(3,3,0,0,0)
    lib_sl.send(4,2,0,0,0)
    lib_sl.send(4,3,0,0,0)
    lib_sl.send(5,2,0,0,0)
    lib_sl.send(5,3,0,0,0)
    lib_sl.send(6,3,0,0,0)
    lib_sl.send(6,2,0,0,0)
    lib_sl.send(7,2,0,0,0)
    lib_sl.send(7,3,0,0,0)
    lib_sl.send(1,4,0,0,0)
    lib_sl.send(2,4,0,0,0)
    lib_sl.send(2,5,0,0,0)
    lib_sl.send(3,4,0,0,0)
    lib_sl.send(3,5,0,0,0)
    lib_sl.send(4,4,0,0,0)
    lib_sl.send(4,5,0,0,0)
    lib_sl.send(5,4,0,0,0)
    lib_sl.send(5,5,0,0,0)
    lib_sl.send(6,4,0,0,0)
# [SPACE],A,[SPACE],P1
    lib_sl.send(0,0,255,0,0)
    lib_sl.send(0,1,255,0,0)
    lib_sl.send(1,0,255,0,0)
    lib_sl.send(6,0,255,0,0)
    lib_sl.send(7,0,255,0,0)
    lib_sl.send(7,1,255,0,0)
    lib_sl.send(3,2,255,0,0)
    lib_sl.send(3,3,255,0,0)
    lib_sl.send(4,2,255,0,0)
    lib_sl.send(4,3,255,0,0)
    lib_sl.send(5,2,255,0,0)
    lib_sl.send(5,3,255,0,0)
    lib_sl.send(6,3,255,0,0)
    lib_sl.send(0,2,255,0,0)
    lib_sl.send(0,3,255,0,0)
    lib_sl.send(1,2,255,0,0)
    lib_sl.send(6,2,255,0,0)
    lib_sl.send(7,2,255,0,0)
    lib_sl.send(7,3,255,0,0)
    lib_sl.send(0,4,255,0,0)
    lib_sl.send(0,5,255,0,0)
    lib_sl.send(1,5,255,0,0)
    lib_sl.send(7,4,255,0,0)
    lib_sl.send(6,5,255,0,0)
    lib_sl.send(7,5,255,0,0)
    time.sleep(5.0)
    lib_sl.send(0,0,0,0,0)
    lib_sl.send(0,1,0,0,0)
    lib_sl.send(1,0,0,0,0)
    lib_sl.send(6,0,0,0,0)
    lib_sl.send(7,0,0,0,0)
    lib_sl.send(7,1,0,0,0)
    lib_sl.send(3,2,0,0,0)
    lib_sl.send(3,3,0,0,0)
    lib_sl.send(4,2,0,0,0)
    lib_sl.send(4,3,0,0,0)
    lib_sl.send(5,2,0,0,0)
    lib_sl.send(5,3,0,0,0)
    lib_sl.send(6,3,0,0,0)
    lib_sl.send(0,2,0,0,0)
    lib_sl.send(0,3,0,0,0)
    lib_sl.send(1,2,0,0,0)
    lib_sl.send(6,2,0,0,0)
    lib_sl.send(7,2,0,0,0)
    lib_sl.send(7,3,0,0,0)
    lib_sl.send(0,4,0,0,0)
    lib_sl.send(0,5,0,0,0)
    lib_sl.send(1,5,0,0,0)
    lib_sl.send(7,4,0,0,0)
    lib_sl.send(6,5,0,0,0)
    lib_sl.send(7,5,0,0,0)
# A,[SPACE],P12
    lib_sl.send(1,1,255,0,0)
    lib_sl.send(2,0,255,0,0)
    lib_sl.send(2,1,255,0,0)
    lib_sl.send(3,0,255,0,0)
    lib_sl.send(3,1,255,0,0)
    lib_sl.send(4,0,255,0,0)
    lib_sl.send(4,1,255,0,0)
    lib_sl.send(5,0,255,0,0)
    lib_sl.send(5,1,255,0,0)
    lib_sl.send(6,1,255,0,0)
    lib_sl.send(6,0,255,0,0)
    lib_sl.send(7,0,255,0,0)
    lib_sl.send(7,1,255,0,0)
    lib_sl.send(1,3,255,0,0)
    lib_sl.send(2,2,255,0,0)
    lib_sl.send(2,3,255,0,0)
    lib_sl.send(3,2,255,0,0)
    lib_sl.send(3,3,255,0,0)
    lib_sl.send(4,2,255,0,0)
    lib_sl.send(4,3,255,0,0)
    lib_sl.send(5,2,255,0,0)
    lib_sl.send(5,3,255,0,0)
    lib_sl.send(6,3,255,0,0)
    lib_sl.send(1,4,255,0,0)
    lib_sl.send(2,4,255,0,0)
    lib_sl.send(2,5,255,0,0)
    lib_sl.send(3,4,255,0,0)
    lib_sl.send(3,5,255,0,0)
    lib_sl.send(4,4,255,0,0)
    lib_sl.send(4,5,255,0,0)
    lib_sl.send(5,4,255,0,0)
    lib_sl.send(5,5,255,0,0)
    lib_sl.send(6,4,255,0,0)
    lib_sl.send(7,4,255,0,0)
    lib_sl.send(6,5,255,0,0)
    lib_sl.send(7,5,255,0,0)
    time.sleep(5.0)
    lib_sl.send(1,1,0,0,0)
    lib_sl.send(2,0,0,0,0)
    lib_sl.send(2,1,0,0,0)
    lib_sl.send(3,0,0,0,0)
    lib_sl.send(3,1,0,0,0)
    lib_sl.send(4,0,0,0,0)
    lib_sl.send(4,1,0,0,0)
    lib_sl.send(5,0,0,0,0)
    lib_sl.send(5,1,0,0,0)
    lib_sl.send(6,1,0,0,0)
    lib_sl.send(6,0,0,0,0)
    lib_sl.send(7,0,0,0,0)
    lib_sl.send(7,1,0,0,0)
    lib_sl.send(1,3,0,0,0)
    lib_sl.send(2,2,0,0,0)
    lib_sl.send(2,3,0,0,0)
    lib_sl.send(3,2,0,0,0)
    lib_sl.send(3,3,0,0,0)
    lib_sl.send(4,2,0,0,0)
    lib_sl.send(4,3,0,0,0)
    lib_sl.send(5,2,0,0,0)
    lib_sl.send(5,3,0,0,0)
    lib_sl.send(6,3,0,0,0)
    lib_sl.send(1,4,0,0,0)
    lib_sl.send(2,4,0,0,0)
    lib_sl.send(2,5,0,0,0)
    lib_sl.send(3,4,0,0,0)
    lib_sl.send(3,5,0,0,0)
    lib_sl.send(4,4,0,0,0)
    lib_sl.send(4,5,0,0,0)
    lib_sl.send(5,4,0,0,0)
    lib_sl.send(5,5,0,0,0)
    lib_sl.send(6,4,0,0,0)
    lib_sl.send(7,4,0,0,0)
    lib_sl.send(6,5,0,0,0)
    lib_sl.send(7,5,0,0,0)
# A23,[SPACE],P
    lib_sl.send(3,0,255,0,0)
    lib_sl.send(3,1,255,0,0)
    lib_sl.send(4,0,255,0,0)
    lib_sl.send(4,1,255,0,0)
    lib_sl.send(5,0,255,0,0)
    lib_sl.send(5,1,255,0,0)
    lib_sl.send(6,1,255,0,0)
    lib_sl.send(0,0,255,0,0)
    lib_sl.send(0,1,255,0,0)
    lib_sl.send(1,0,255,0,0)
    lib_sl.send(6,0,255,0,0)
    lib_sl.send(7,0,255,0,0)
    lib_sl.send(7,1,255,0,0)
    lib_sl.send(0,2,255,0,0)
    lib_sl.send(0,3,255,0,0)
    lib_sl.send(1,2,255,0,0)
    lib_sl.send(6,2,255,0,0)
    lib_sl.send(7,2,255,0,0)
    lib_sl.send(7,3,255,0,0)
    lib_sl.send(3,4,255,0,0)
    lib_sl.send(3,5,255,0,0)
    lib_sl.send(4,4,255,0,0)
    lib_sl.send(4,5,255,0,0)
    lib_sl.send(5,4,255,0,0)
    lib_sl.send(5,5,255,0,0)
    lib_sl.send(6,4,255,0,0)
    lib_sl.send(7,4,255,0,0)
    lib_sl.send(6,5,255,0,0)
    lib_sl.send(7,5,255,0,0)
    time.sleep(5.0)
    lib_sl.send(3,0,0,0,0)
    lib_sl.send(3,1,0,0,0)
    lib_sl.send(4,0,0,0,0)
    lib_sl.send(4,1,0,0,0)
    lib_sl.send(5,0,0,0,0)
    lib_sl.send(5,1,0,0,0)
    lib_sl.send(6,1,0,0,0)
    lib_sl.send(0,0,0,0,0)
    lib_sl.send(0,1,0,0,0)
    lib_sl.send(1,0,0,0,0)
    lib_sl.send(6,0,0,0,0)
    lib_sl.send(7,0,0,0,0)
    lib_sl.send(7,1,0,0,0)
    lib_sl.send(0,2,0,0,0)
    lib_sl.send(0,3,0,0,0)
    lib_sl.send(1,2,0,0,0)
    lib_sl.send(6,2,0,0,0)
    lib_sl.send(7,2,0,0,0)
    lib_sl.send(7,3,0,0,0)
    lib_sl.send(3,4,0,0,0)
    lib_sl.send(3,5,0,0,0)
    lib_sl.send(4,4,0,0,0)
    lib_sl.send(4,5,0,0,0)
    lib_sl.send(5,4,0,0,0)
    lib_sl.send(5,5,0,0,0)
    lib_sl.send(6,4,0,0,0)
    lib_sl.send(7,4,0,0,0)
    lib_sl.send(6,5,0,0,0)
    lib_sl.send(7,5,0,0,0)
# A3,[SPACE],P,[SPACE]
    lib_sl.send(1,1,255,0,0)
    lib_sl.send(2,0,255,0,0)
    lib_sl.send(2,1,255,0,0)
    lib_sl.send(3,0,255,0,0)
    lib_sl.send(3,1,255,0,0)
    lib_sl.send(4,0,255,0,0)
    lib_sl.send(4,1,255,0,0)
    lib_sl.send(5,0,255,0,0)
    lib_sl.send(5,1,255,0,0)
    lib_sl.send(6,1,255,0,0)
    lib_sl.send(1,3,255,0,0)
    lib_sl.send(2,2,255,0,0)
    lib_sl.send(2,3,255,0,0)
    lib_sl.send(3,2,255,0,0)
    lib_sl.send(3,3,255,0,0)
    lib_sl.send(4,2,255,0,0)
    lib_sl.send(4,3,255,0,0)
    lib_sl.send(5,2,255,0,0)
    lib_sl.send(5,3,255,0,0)
    lib_sl.send(6,3,255,0,0)
    lib_sl.send(6,2,255,0,0)
    lib_sl.send(7,2,255,0,0)
    lib_sl.send(7,3,255,0,0)
    lib_sl.send(3,4,255,0,0)
    lib_sl.send(3,5,255,0,0)
    lib_sl.send(4,4,255,0,0)
    lib_sl.send(4,5,255,0,0)
    lib_sl.send(5,4,255,0,0)
    lib_sl.send(5,5,255,0,0)
    lib_sl.send(6,4,255,0,0)
    time.sleep(5.0)
    lib_sl.send(1,1,0,0,0)
    lib_sl.send(2,0,0,0,0)
    lib_sl.send(2,1,0,0,0)
    lib_sl.send(3,0,0,0,0)
    lib_sl.send(3,1,0,0,0)
    lib_sl.send(4,0,0,0,0)
    lib_sl.send(4,1,0,0,0)
    lib_sl.send(5,0,0,0,0)
    lib_sl.send(5,1,0,0,0)
    lib_sl.send(6,1,0,0,0)
    lib_sl.send(1,3,0,0,0)
    lib_sl.send(2,2,0,0,0)
    lib_sl.send(2,3,0,0,0)
    lib_sl.send(3,2,0,0,0)
    lib_sl.send(3,3,0,0,0)
    lib_sl.send(4,2,0,0,0)
    lib_sl.send(4,3,0,0,0)
    lib_sl.send(5,2,0,0,0)
    lib_sl.send(5,3,0,0,0)
    lib_sl.send(6,3,0,0,0)
    lib_sl.send(6,2,0,0,0)
    lib_sl.send(7,2,0,0,0)
    lib_sl.send(7,3,0,0,0)
    lib_sl.send(3,4,0,0,0)
    lib_sl.send(3,5,0,0,0)
    lib_sl.send(4,4,0,0,0)
    lib_sl.send(4,5,0,0,0)
    lib_sl.send(5,4,0,0,0)
    lib_sl.send(5,5,0,0,0)
    lib_sl.send(6,4,0,0,0)
#[SPACE],P,[SPACE],P1
    lib_sl.send(0,0,255,0,0)
    lib_sl.send(0,1,255,0,0)
    lib_sl.send(1,0,255,0,0)
    lib_sl.send(6,0,255,0,0)
    lib_sl.send(7,0,255,0,0)
    lib_sl.send(7,1,255,0,0)
    lib_sl.send(3,2,255,0,0)
    lib_sl.send(3,3,255,0,0)
    lib_sl.send(4,2,255,0,0)
    lib_sl.send(4,3,255,0,0)
    lib_sl.send(5,2,255,0,0)
    lib_sl.send(5,3,255,0,0)
    lib_sl.send(6,3,255,0,0)
    lib_sl.send(6,2,255,0,0)
    lib_sl.send(7,2,255,0,0)
    lib_sl.send(7,3,255,0,0)
    lib_sl.send(7,4,255,0,0)
    lib_sl.send(6,5,255,0,0)
    lib_sl.send(7,5,255,0,0)
    lib_sl.send(0,4,255,0,0)
    lib_sl.send(0,5,255,0,0)
    lib_sl.send(1,5,255,0,0)
    time.sleep(5.0)
    lib_sl.send(0,0,0,0,0)
    lib_sl.send(0,1,0,0,0)
    lib_sl.send(1,0,0,0,0)
    lib_sl.send(6,0,0,0,0)
    lib_sl.send(7,0,0,0,0)
    lib_sl.send(7,1,0,0,0)
    lib_sl.send(3,2,0,0,0)
    lib_sl.send(3,3,0,0,0)
    lib_sl.send(4,2,0,0,0)
    lib_sl.send(4,3,0,0,0)
    lib_sl.send(5,2,0,0,0)
    lib_sl.send(5,3,0,0,0)
    lib_sl.send(6,3,0,0,0)
    lib_sl.send(6,2,0,0,0)
    lib_sl.send(7,2,0,0,0)
    lib_sl.send(7,3,0,0,0)
    lib_sl.send(7,4,0,0,0)
    lib_sl.send(6,5,0,0,0)
    lib_sl.send(7,5,0,0,0)
    lib_sl.send(0,4,0,0,0)
    lib_sl.send(0,5,0,0,0)
    lib_sl.send(1,5,0,0,0)
# P,[SPACE], P12
    lib_sl.send(1,1,255,0,0)
    lib_sl.send(2,0,255,0,0)
    lib_sl.send(2,1,255,0,0)
    lib_sl.send(3,0,255,0,0)
    lib_sl.send(3,1,255,0,0)
    lib_sl.send(4,0,255,0,0)
    lib_sl.send(4,1,255,0,0)
    lib_sl.send(5,0,255,0,0)
    lib_sl.send(5,1,255,0,0)
    lib_sl.send(6,1,255,0,0)
    lib_sl.send(6,0,255,0,0)
    lib_sl.send(7,0,255,0,0)
    lib_sl.send(7,1,255,0,0)
    lib_sl.send(3,2,255,0,0)
    lib_sl.send(3,3,255,0,0)
    lib_sl.send(4,2,255,0,0)
    lib_sl.send(4,3,255,0,0)
    lib_sl.send(5,2,255,0,0)
    lib_sl.send(5,3,255,0,0)
    lib_sl.send(6,3,255,0,0)
    lib_sl.send(1,4,255,0,0)
    lib_sl.send(2,4,255,0,0)
    lib_sl.send(2,5,255,0,0)
    lib_sl.send(3,4,255,0,0)
    lib_sl.send(3,5,255,0,0)
    lib_sl.send(4,4,255,0,0)
    lib_sl.send(4,5,255,0,0)
    lib_sl.send(5,4,255,0,0)
    lib_sl.send(5,5,255,0,0)
    lib_sl.send(6,4,255,0,0)
    lib_sl.send(7,4,255,0,0)
    lib_sl.send(6,5,255,0,0)
    lib_sl.send(7,5,255,0,0)
    time.sleep(5.0)
    lib_sl.send(1,1,0,0,0)
    lib_sl.send(2,0,0,0,0)
    lib_sl.send(2,1,0,0,0)
    lib_sl.send(3,0,0,0,0)
    lib_sl.send(3,1,0,0,0)
    lib_sl.send(4,0,0,0,0)
    lib_sl.send(4,1,0,0,0)
    lib_sl.send(5,0,0,0,0)
    lib_sl.send(5,1,0,0,0)
    lib_sl.send(6,1,0,0,0)
    lib_sl.send(6,0,0,0,0)
    lib_sl.send(7,0,0,0,0)
    lib_sl.send(7,1,0,0,0)
    lib_sl.send(3,2,0,0,0)
    lib_sl.send(3,3,0,0,0)
    lib_sl.send(4,2,0,0,0)
    lib_sl.send(4,3,0,0,0)
    lib_sl.send(5,2,0,0,0)
    lib_sl.send(5,3,0,0,0)
    lib_sl.send(6,3,0,0,0)
    lib_sl.send(1,4,0,0,0)
    lib_sl.send(2,4,0,0,0)
    lib_sl.send(2,5,0,0,0)
    lib_sl.send(3,4,0,0,0)
    lib_sl.send(3,5,0,0,0)
    lib_sl.send(4,4,0,0,0)
    lib_sl.send(4,5,0,0,0)
    lib_sl.send(5,4,0,0,0)
    lib_sl.send(5,5,0,0,0)
    lib_sl.send(6,4,0,0,0)
    lib_sl.send(7,4,0,0,0)
    lib_sl.send(6,5,0,0,0)
    lib_sl.send(7,5,0,0,0)
# P23,[SPACE],P
    lib_sl.send(3,0,255,0,0)
    lib_sl.send(3,1,255,0,0)
    lib_sl.send(4,0,255,0,0)
    lib_sl.send(4,1,255,0,0)
    lib_sl.send(5,0,255,0,0)
    lib_sl.send(5,1,255,0,0)
    lib_sl.send(6,1,255,0,0)
    lib_sl.send(6,0,255,0,0)
    lib_sl.send(7,0,255,0,0)
    lib_sl.send(7,1,255,0,0)
    lib_sl.send(0,2,255,0,0)
    lib_sl.send(0,3,255,0,0)
    lib_sl.send(1,2,255,0,0)
    lib_sl.send(6,2,255,0,0)
    lib_sl.send(7,2,255,0,0)
    lib_sl.send(7,3,255,0,0)
    lib_sl.send(3,4,255,0,0)
    lib_sl.send(3,5,255,0,0)
    lib_sl.send(4,4,255,0,0)
    lib_sl.send(4,5,255,0,0)
    lib_sl.send(5,4,255,0,0)
    lib_sl.send(5,5,255,0,0)
    lib_sl.send(6,4,255,0,0)
    lib_sl.send(7,4,255,0,0)
    lib_sl.send(6,5,255,0,0)
    lib_sl.send(7,5,255,0,0)
    time.sleep(5.0)
    lib_sl.send(3,0,0,0,0)
    lib_sl.send(3,1,0,0,0)
    lib_sl.send(4,0,0,0,0)
    lib_sl.send(4,1,0,0,0)
    lib_sl.send(5,0,0,0,0)
    lib_sl.send(5,1,0,0,0)
    lib_sl.send(6,1,0,0,0)
    lib_sl.send(6,0,0,0,0)
    lib_sl.send(7,0,0,0,0)
    lib_sl.send(7,1,0,0,0)
    lib_sl.send(0,2,0,0,0)
    lib_sl.send(0,3,0,0,0)
    lib_sl.send(1,2,0,0,0)
    lib_sl.send(6,2,0,0,0)
    lib_sl.send(7,2,0,0,0)
    lib_sl.send(7,3,0,0,0)
    lib_sl.send(3,4,0,0,0)
    lib_sl.send(3,5,0,0,0)
    lib_sl.send(4,4,0,0,0)
    lib_sl.send(4,5,0,0,0)
    lib_sl.send(5,4,0,0,0)
    lib_sl.send(5,5,0,0,0)
    lib_sl.send(6,4,0,0,0)
    lib_sl.send(7,4,0,0,0)
    lib_sl.send(6,5,0,0,0)
    lib_sl.send(7,5,0,0,0)
# P3,[SPACE],P,[SPACE]
    lib_sl.send(3,0,255,0,0)
    lib_sl.send(3,1,255,0,0)
    lib_sl.send(4,0,255,0,0)
    lib_sl.send(4,1,255,0,0)
    lib_sl.send(5,0,255,0,0)
    lib_sl.send(5,1,255,0,0)
    lib_sl.send(6,1,255,0,0)
    lib_sl.send(1,3,255,0,0)
    lib_sl.send(2,2,255,0,0)
    lib_sl.send(2,3,255,0,0)
    lib_sl.send(3,2,255,0,0)
    lib_sl.send(3,3,255,0,0)
    lib_sl.send(4,2,255,0,0)
    lib_sl.send(4,3,255,0,0)
    lib_sl.send(5,2,255,0,0)
    lib_sl.send(5,3,255,0,0)
    lib_sl.send(6,3,255,0,0)
    lib_sl.send(6,2,255,0,0)
    lib_sl.send(7,2,255,0,0)
    lib_sl.send(7,3,255,0,0)
    lib_sl.send(3,4,255,0,0)
    lib_sl.send(3,5,255,0,0)
    lib_sl.send(4,4,255,0,0)
    lib_sl.send(4,5,255,0,0)
    lib_sl.send(5,4,255,0,0)
    lib_sl.send(5,5,255,0,0)
    lib_sl.send(6,4,255,0,0)
    time.sleep(5.0)
    lib_sl.send(3,0,0,0,0)
    lib_sl.send(3,1,0,0,0)
    lib_sl.send(4,0,0,0,0)
    lib_sl.send(4,1,0,0,0)
    lib_sl.send(5,0,0,0,0)
    lib_sl.send(5,1,0,0,0)
    lib_sl.send(6,1,0,0,0)
    lib_sl.send(1,3,0,0,0)
    lib_sl.send(2,2,0,0,0)
    lib_sl.send(2,3,0,0,0)
    lib_sl.send(3,2,0,0,0)
    lib_sl.send(3,3,0,0,0)
    lib_sl.send(4,2,0,0,0)
    lib_sl.send(4,3,0,0,0)
    lib_sl.send(5,2,0,0,0)
    lib_sl.send(5,3,0,0,0)
    lib_sl.send(6,3,0,0,0)
    lib_sl.send(6,2,0,0,0)
    lib_sl.send(7,2,0,0,0)
    lib_sl.send(7,3,0,0,0)
    lib_sl.send(3,4,0,0,0)
    lib_sl.send(3,5,0,0,0)
    lib_sl.send(4,4,0,0,0)
    lib_sl.send(4,5,0,0,0)
    lib_sl.send(5,4,0,0,0)
    lib_sl.send(5,5,0,0,0)
    lib_sl.send(6,4,0,0,0)
# SPACE,P,SPACE,Y1
    lib_sl.send(0,0,255,0,0)
    lib_sl.send(0,1,255,0,0)
    lib_sl.send(1,0,255,0,0)
    lib_sl.send(6,0,255,0,0)
    lib_sl.send(7,0,255,0,0)
    lib_sl.send(7,1,255,0,0)
    lib_sl.send(3,2,255,0,0)
    lib_sl.send(3,3,255,0,0)
    lib_sl.send(4,2,255,0,0)
    lib_sl.send(4,3,255,0,0)
    lib_sl.send(5,2,255,0,0)
    lib_sl.send(5,3,255,0,0)
    lib_sl.send(6,3,255,0,0)
    lib_sl.send(6,2,255,0,0)
    lib_sl.send(7,2,255,0,0)
    lib_sl.send(7,3,255,0,0)
    lib_sl.send(7,4,255,0,0)
    lib_sl.send(6,5,255,0,0)
    lib_sl.send(7,5,255,0,0)
    time.sleep(5.0)
    lib_sl.send(0,0,0,0,0)
    lib_sl.send(0,1,0,0,0)
    lib_sl.send(1,0,0,0,0)
    lib_sl.send(6,0,0,0,0)
    lib_sl.send(7,0,0,0,0)
    lib_sl.send(7,1,0,0,0)
    lib_sl.send(3,2,0,0,0)
    lib_sl.send(3,3,0,0,0)
    lib_sl.send(4,2,0,0,0)
    lib_sl.send(4,3,0,0,0)
    lib_sl.send(5,2,0,0,0)
    lib_sl.send(5,3,0,0,0)
    lib_sl.send(6,3,0,0,0)
    lib_sl.send(6,2,0,0,0)
    lib_sl.send(7,2,0,0,0)
    lib_sl.send(7,3,0,0,0)
    lib_sl.send(7,4,0,0,0)
    lib_sl.send(6,5,0,0,0)
    lib_sl.send(7,5,0,0,0)
# P,SPACE,Y12
    lib_sl.send(1,1,255,0,0)
    lib_sl.send(2,0,255,0,0)
    lib_sl.send(2,1,255,0,0)
    lib_sl.send(3,0,255,0,0)
    lib_sl.send(3,1,255,0,0)
    lib_sl.send(4,0,255,0,0)
    lib_sl.send(4,1,255,0,0)
    lib_sl.send(5,0,255,0,0)
    lib_sl.send(5,1,255,0,0)
    lib_sl.send(6,1,255,0,0)
    lib_sl.send(6,0,255,0,0)
    lib_sl.send(7,0,255,0,0)
    lib_sl.send(7,1,255,0,0)
    lib_sl.send(3,2,255,0,0)
    lib_sl.send(3,3,255,0,0)
    lib_sl.send(4,2,255,0,0)
    lib_sl.send(4,3,255,0,0)
    lib_sl.send(5,2,255,0,0)
    lib_sl.send(5,3,255,0,0)
    lib_sl.send(6,3,255,0,0)
    lib_sl.send(5,4,255,0,0)
    lib_sl.send(5,5,255,0,0)
    lib_sl.send(6,4,255,0,0)
    lib_sl.send(0,4,255,0,0)
    lib_sl.send(0,5,255,0,0)
    lib_sl.send(1,5,255,0,0)
    time.sleep(5.0)
    lib_sl.send(1,1,0,0,0)
    lib_sl.send(2,0,0,0,0)
    lib_sl.send(2,1,0,0,0)
    lib_sl.send(3,0,0,0,0)
    lib_sl.send(3,1,0,0,0)
    lib_sl.send(4,0,0,0,0)
    lib_sl.send(4,1,0,0,0)
    lib_sl.send(5,0,0,0,0)
    lib_sl.send(5,1,0,0,0)
    lib_sl.send(6,1,0,0,0)
    lib_sl.send(6,0,0,0,0)
    lib_sl.send(7,0,0,0,0)
    lib_sl.send(7,1,0,0,0)
    lib_sl.send(3,2,0,0,0)
    lib_sl.send(3,3,0,0,0)
    lib_sl.send(4,2,0,0,0)
    lib_sl.send(4,3,0,0,0)
    lib_sl.send(5,2,0,0,0)
    lib_sl.send(5,3,0,0,0)
    lib_sl.send(6,3,0,0,0)
    lib_sl.send(5,4,0,0,0)
    lib_sl.send(5,5,0,0,0)
    lib_sl.send(6,4,0,0,0)
    lib_sl.send(0,4,0,0,0)
    lib_sl.send(0,5,0,0,0)
    lib_sl.send(1,5,0,0,0)
# P23,SPACE, Y
    lib_sl.send(3,0,255,0,0)
    lib_sl.send(3,1,255,0,0)
    lib_sl.send(4,0,255,0,0)
    lib_sl.send(4,1,255,0,0)
    lib_sl.send(5,0,255,0,0)
    lib_sl.send(5,1,255,0,0)
    lib_sl.send(6,1,255,0,0)
    lib_sl.send(6,0,255,0,0)
    lib_sl.send(7,0,255,0,0)
    lib_sl.send(7,1,255,0,0)
    lib_sl.send(6,2,255,0,0)
    lib_sl.send(7,2,255,0,0)
    lib_sl.send(7,3,255,0,0)
    lib_sl.send(3,4,255,0,0)
    lib_sl.send(3,5,255,0,0)
    lib_sl.send(4,4,255,0,0)
    lib_sl.send(4,5,255,0,0)
    lib_sl.send(1,4,255,0,0)
    lib_sl.send(2,4,255,0,0)
    lib_sl.send(2,5,255,0,0)
    lib_sl.send(7,4,255,0,0)
    lib_sl.send(6,5,255,0,0)
    lib_sl.send(7,5,255,0,0)
    time.sleep(5.0)
    lib_sl.send(3,0,0,0,0)
    lib_sl.send(3,1,0,0,0)
    lib_sl.send(4,0,0,0,0)
    lib_sl.send(4,1,0,0,0)
    lib_sl.send(5,0,0,0,0)
    lib_sl.send(5,1,0,0,0)
    lib_sl.send(6,1,0,0,0)
    lib_sl.send(6,0,0,0,0)
    lib_sl.send(7,0,0,0,0)
    lib_sl.send(7,1,0,0,0)
    lib_sl.send(6,2,0,0,0)
    lib_sl.send(7,2,0,0,0)
    lib_sl.send(7,3,0,0,0)
    lib_sl.send(3,4,0,0,0)
    lib_sl.send(3,5,0,0,0)
    lib_sl.send(4,4,0,0,0)
    lib_sl.send(4,5,0,0,0)
    lib_sl.send(1,4,0,0,0)
    lib_sl.send(2,4,0,0,0)
    lib_sl.send(2,5,0,0,0)
    lib_sl.send(7,4,0,0,0)
    lib_sl.send(6,5,0,0,0)
    lib_sl.send(7,5,0,0,0)
# P3,SPACE,Y,SPACE
    lib_sl.send(3,0,255,0,0)
    lib_sl.send(3,1,255,0,0)
    lib_sl.send(4,0,255,0,0)
    lib_sl.send(4,1,255,0,0)
    lib_sl.send(5,0,255,0,0)
    lib_sl.send(5,1,255,0,0)
    lib_sl.send(6,1,255,0,0)
    lib_sl.send(5,2,255,0,0)
    lib_sl.send(5,3,255,0,0)
    lib_sl.send(6,3,255,0,0)
    lib_sl.send(0,2,255,0,0)
    lib_sl.send(0,3,255,0,0)
    lib_sl.send(1,2,255,0,0)
    lib_sl.send(5,4,255,0,0)
    lib_sl.send(5,5,255,0,0)
    lib_sl.send(6,4,255,0,0)
    time.sleep(5.0)
    lib_sl.send(3,0,0,0,0)
    lib_sl.send(3,1,0,0,0)
    lib_sl.send(4,0,0,0,0)
    lib_sl.send(4,1,0,0,0)
    lib_sl.send(5,0,0,0,0)
    lib_sl.send(5,1,0,0,0)
    lib_sl.send(6,1,0,0,0)
    lib_sl.send(5,2,0,0,0)
    lib_sl.send(5,3,0,0,0)
    lib_sl.send(6,3,0,0,0)
    lib_sl.send(0,2,0,0,0)
    lib_sl.send(0,3,0,0,0)
    lib_sl.send(1,2,0,0,0)
    lib_sl.send(5,4,0,0,0)
    lib_sl.send(5,5,0,0,0)
    lib_sl.send(6,4,0,0,0)
# SPACE,Y,SPACE,?1
    lib_sl.send(6,0,255,0,0)
    lib_sl.send(7,0,255,0,0)
    lib_sl.send(7,1,255,0,0)
    lib_sl.send(1,3,255,0,0)
    lib_sl.send(2,2,255,0,0)
    lib_sl.send(2,3,255,0,0)
    lib_sl.send(3,2,255,0,0)
    lib_sl.send(3,3,255,0,0)
    lib_sl.send(4,2,255,0,0)
    lib_sl.send(4,3,255,0,0)
    lib_sl.send(6,2,255,0,0)
    lib_sl.send(7,2,255,0,0)
    lib_sl.send(7,3,255,0,0)
    lib_sl.send(7,4,0,255,0)
    lib_sl.send(6,5,0,255,0)
    lib_sl.send(7,5,0,255,0)
    time.sleep(5.0)
    lib_sl.send(6,0,0,0,0)
    lib_sl.send(7,0,0,0,0)
    lib_sl.send(7,1,0,0,0)
    lib_sl.send(1,3,0,0,0)
    lib_sl.send(2,2,0,0,0)
    lib_sl.send(2,3,0,0,0)
    lib_sl.send(3,2,0,0,0)
    lib_sl.send(3,3,0,0,0)
    lib_sl.send(4,2,0,0,0)
    lib_sl.send(4,3,0,0,0)
    lib_sl.send(6,2,0,0,0)
    lib_sl.send(7,2,0,0,0)
    lib_sl.send(7,3,0,0,0)
    lib_sl.send(7,4,0,0,0)
    lib_sl.send(6,5,0,0,0)
    lib_sl.send(7,5,0,0,0)
# Y,SPACE,?12
    lib_sl.send(5,0,255,0,0)
    lib_sl.send(5,1,255,0,0)
    lib_sl.send(6,1,255,0,0)
    lib_sl.send(0,0,255,0,0)
    lib_sl.send(0,1,255,0,0)
    lib_sl.send(1,0,255,0,0)
    lib_sl.send(5,2,255,0,0)
    lib_sl.send(5,3,255,0,0)
    lib_sl.send(6,3,255,0,0)
    lib_sl.send(5,4,0,255,0)
    lib_sl.send(5,5,0,255,0)
    lib_sl.send(6,4,0,255,0)
    lib_sl.send(0,4,0,255,0)
    lib_sl.send(0,5,0,255,0)
    lib_sl.send(1,5,0,255,0)
    lib_sl.send(7,4,0,255,0)
    lib_sl.send(6,5,0,255,0)
    lib_sl.send(7,5,0,255,0)
    time.sleep(5.0)
    lib_sl.send(5,0,0,0,0)
    lib_sl.send(5,1,0,0,0)
    lib_sl.send(6,1,0,0,0)
    lib_sl.send(0,0,0,0,0)
    lib_sl.send(0,1,0,0,0)
    lib_sl.send(1,0,0,0,0)
    lib_sl.send(5,2,0,0,0)
    lib_sl.send(5,3,0,0,0)
    lib_sl.send(6,3,0,0,0)
    lib_sl.send(5,4,0,0,0)
    lib_sl.send(5,5,0,0,0)
    lib_sl.send(6,4,0,0,0)
    lib_sl.send(0,4,0,0,0)
    lib_sl.send(0,5,0,0,0)
    lib_sl.send(1,5,0,0,0)
    lib_sl.send(7,4,0,0,0)
    lib_sl.send(6,5,0,0,0)
    lib_sl.send(7,5,0,0,0)
# Y23,SPACE,?
    lib_sl.send(1,1,255,0,0)
    lib_sl.send(2,0,255,0,0)
    lib_sl.send(2,1,255,0,0)
    lib_sl.send(3,0,255,0,0)
    lib_sl.send(3,1,255,0,0)
    lib_sl.send(4,0,255,0,0)
    lib_sl.send(4,1,255,0,0)
    lib_sl.send(6,0,255,0,0)
    lib_sl.send(7,0,255,0,0)
    lib_sl.send(7,1,255,0,0)
    lib_sl.send(6,2,0,255,0)
    lib_sl.send(7,2,0,255,0)
    lib_sl.send(7,3,0,255,0)
    lib_sl.send(1,4,0,255,0)
    lib_sl.send(2,4,0,255,0)
    lib_sl.send(2,5,0,255,0)
    lib_sl.send(3,4,0,255,0)
    lib_sl.send(3,5,0,255,0)
    lib_sl.send(4,4,0,255,0)
    lib_sl.send(4,5,0,255,0)
    lib_sl.send(5,4,0,255,0)
    lib_sl.send(5,5,0,255,0)
    lib_sl.send(6,4,0,255,0)
    lib_sl.send(7,4,0,255,0)
    lib_sl.send(6,5,0,255,0)
    lib_sl.send(7,5,0,255,0)
    time.sleep(5.0)
    lib_sl.send(1,1,0,0,0)
    lib_sl.send(2,0,0,0,0)
    lib_sl.send(2,1,0,0,0)
    lib_sl.send(3,0,0,0,0)
    lib_sl.send(3,1,0,0,0)
    lib_sl.send(4,0,0,0,0)
    lib_sl.send(4,1,0,0,0)
    lib_sl.send(6,0,0,0,0)
    lib_sl.send(7,0,0,0,0)
    lib_sl.send(7,1,0,0,0)
    lib_sl.send(6,2,0,0,0)
    lib_sl.send(7,2,0,0,0)
    lib_sl.send(7,3,0,0,0)
    lib_sl.send(1,4,0,0,0)
    lib_sl.send(2,4,0,0,0)
    lib_sl.send(2,5,0,0,0)
    lib_sl.send(3,4,0,0,0)
    lib_sl.send(3,5,0,0,0)
    lib_sl.send(4,4,0,0,0)
    lib_sl.send(4,5,0,0,0)
    lib_sl.send(5,4,0,0,0)
    lib_sl.send(5,5,0,0,0)
    lib_sl.send(6,4,0,0,0)
    lib_sl.send(7,4,0,0,0)
    lib_sl.send(6,5,0,0,0)
    lib_sl.send(7,5,0,0,0)
# Y3,SPACE,?,SPACE
    lib_sl.send(5,0,255,0,0)
    lib_sl.send(5,1,255,0,0)
    lib_sl.send(6,1,255,0,0)
    lib_sl.send(5,2,0,255,0)
    lib_sl.send(5,3,0,255,0)
    lib_sl.send(6,3,0,255,0)
    lib_sl.send(0,2,0,255,0)
    lib_sl.send(0,3,0,255,0)
    lib_sl.send(1,2,0,255,0)
    lib_sl.send(6,2,0,255,0)
    lib_sl.send(7,2,0,255,0)
    lib_sl.send(7,3,0,255,0)
    lib_sl.send(3,4,0,255,0)
    lib_sl.send(3,5,0,255,0)
    lib_sl.send(4,4,0,255,0)
    lib_sl.send(4,5,0,255,0)
    lib_sl.send(5,4,0,255,0)
    lib_sl.send(5,5,0,255,0)
    lib_sl.send(6,4,0,255,0)
    time.sleep(5.0)
    lib_sl.send(5,0,0,0,0)
    lib_sl.send(5,1,0,0,0)
    lib_sl.send(6,1,0,0,0)
    lib_sl.send(5,2,0,0,0)
    lib_sl.send(5,3,0,0,0)
    lib_sl.send(6,3,0,0,0)
    lib_sl.send(0,2,0,0,0)
    lib_sl.send(0,3,0,0,0)
    lib_sl.send(1,2,0,0,0)
    lib_sl.send(6,2,0,0,0)
    lib_sl.send(7,2,0,0,0)
    lib_sl.send(7,3,0,0,0)
    lib_sl.send(3,4,0,0,0)
    lib_sl.send(3,5,0,0,0)
    lib_sl.send(4,4,0,0,0)
    lib_sl.send(4,5,0,0,0)
    lib_sl.send(5,4,0,0,0)
    lib_sl.send(5,5,0,0,0)
    lib_sl.send(6,4,0,0,0)
# SPACE,?,SPACE,SPACE
    lib_sl.send(6,0,0,255,0)
    lib_sl.send(7,0,0,255,0)
    lib_sl.send(7,1,0,255,0)
    lib_sl.send(1,3,0,255,0)
    lib_sl.send(2,2,0,255,0)
    lib_sl.send(2,3,0,255,0)
    lib_sl.send(3,2,0,255,0)
    lib_sl.send(3,3,0,255,0)
    lib_sl.send(4,2,0,255,0)
    lib_sl.send(4,3,0,255,0)
    lib_sl.send(5,2,0,255,0)
    lib_sl.send(5,3,0,255,0)
    lib_sl.send(6,3,0,255,0)
    lib_sl.send(6,2,0,255,0)
    lib_sl.send(7,2,0,255,0)
    lib_sl.send(7,3,0,255,0)
    time.sleep(5.0)
    lib_sl.send(6,0,0,0,0)
    lib_sl.send(7,0,0,0,0)
    lib_sl.send(7,1,0,0,0)
    lib_sl.send(1,3,0,0,0)
    lib_sl.send(2,2,0,0,0)
    lib_sl.send(2,3,0,0,0)
    lib_sl.send(3,2,0,0,0)
    lib_sl.send(3,3,0,0,0)
    lib_sl.send(4,2,0,0,0)
    lib_sl.send(4,3,0,0,0)
    lib_sl.send(5,2,0,0,0)
    lib_sl.send(5,3,0,0,0)
    lib_sl.send(6,3,0,0,0)
    lib_sl.send(6,2,0,0,0)
    lib_sl.send(7,2,0,0,0)
    lib_sl.send(7,3,0,0,0)
# ?,SPACE ETC
    lib_sl.send(5,0,0,255,0)
    lib_sl.send(5,1,0,255,0)
    lib_sl.send(6,1,0,255,0)
    lib_sl.send(0,0,0,255,0)
    lib_sl.send(0,1,0,255,0)
    lib_sl.send(1,0,0,255,0)
    lib_sl.send(6,0,0,255,0)
    lib_sl.send(7,0,0,255,0)
    lib_sl.send(7,1,0,255,0)
    lib_sl.send(3,2,0,255,0)
    lib_sl.send(3,3,0,255,0)
    lib_sl.send(4,2,0,255,0)
    lib_sl.send(4,3,0,255,0)
    lib_sl.send(5,2,0,255,0)
    lib_sl.send(5,3,0,255,0)
    lib_sl.send(6,3,0,255,0)
    time.sleep(5.0)
    lib_sl.send(5,0,0,0,0)
    lib_sl.send(5,1,0,0,0)
    lib_sl.send(6,1,0,0,0)
    lib_sl.send(0,0,0,0,0)
    lib_sl.send(0,1,0,0,0)
    lib_sl.send(1,0,0,0,0)
    lib_sl.send(6,0,0,0,0)
    lib_sl.send(7,0,0,0,0)
    lib_sl.send(7,1,0,0,0)
    lib_sl.send(3,2,0,0,0)
    lib_sl.send(3,3,0,0,0)
    lib_sl.send(4,2,0,0,0)
    lib_sl.send(4,3,0,0,0)
    lib_sl.send(5,2,0,0,0)
    lib_sl.send(5,3,0,0,0)
    lib_sl.send(6,3,0,0,0)
# ?23,SPACE ETC
    lib_sl.send(1,1,0,255,0)
    lib_sl.send(2,0,0,255,0)
    lib_sl.send(2,1,0,255,0)
    lib_sl.send(3,0,0,255,0)
    lib_sl.send(3,1,0,255,0)
    lib_sl.send(4,0,0,255,0)
    lib_sl.send(4,1,0,255,0)
    lib_sl.send(5,0,0,255,0)
    lib_sl.send(5,1,0,255,0)
    lib_sl.send(6,1,0,255,0)
    lib_sl.send(6,0,0,255,0)
    lib_sl.send(7,0,0,255,0)
    lib_sl.send(7,1,0,255,0)
    time.sleep(5.0)
    lib_sl.send(1,1,0,0,0)
    lib_sl.send(2,0,0,0,0)
    lib_sl.send(2,1,0,0,0)
    lib_sl.send(3,0,0,0,0)
    lib_sl.send(3,1,0,0,0)
    lib_sl.send(4,0,0,0,0)
    lib_sl.send(4,1,0,0,0)
    lib_sl.send(5,0,0,0,0)
    lib_sl.send(5,1,0,0,0)
    lib_sl.send(6,1,0,0,0)
    lib_sl.send(6,0,0,0,0)
    lib_sl.send(7,0,0,0,0)
    lib_sl.send(7,1,0,0,0)
# ?3,SPACE ETC
    lib_sl.send(3,0,0,255,0)
    lib_sl.send(3,1,0,255,0)
    lib_sl.send(4,0,0,255,0)
    lib_sl.send(4,1,0,255,0)
    lib_sl.send(5,0,0,255,0)
    lib_sl.send(5,1,0,255,0)
    lib_sl.send(6,1,0,255,0)
    time.sleep(5.0)
    lib_sl.send(3,0,0,0,0)
    lib_sl.send(3,1,0,0,0)
    lib_sl.send(4,0,0,0,0)
    lib_sl.send(4,1,0,0,0)
    lib_sl.send(5,0,0,0,0)
    lib_sl.send(5,1,0,0,0)
    lib_sl.send(6,1,0,0,0)
# SPACE ETC
    time.sleep(20.0)
