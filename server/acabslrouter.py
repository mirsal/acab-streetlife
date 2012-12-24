import socket
import thread
import time
import Queue
import sys
import select

"""
Accepts traditional single wall streams and
splits them onto different acabsl.

The streams are splitted onto different slave
acabslservers.

The different streams can have different priorities and
timeouts. After a stream has a timeout, the next stream
with lower priority will be activated.
"""

#walls = [[host, port, startx, starty, sizex, sizey, socket],
walls = [{'host': 'localhost', 'port': 5001, 'simhost': 'localhost', 'simport': 4001, 'startx': 0, 'starty': 0, 'sizex': 8, 'sizey': 6},
         {'host': 'localhost', 'port': 5002, 'simhost': 'localhost', 'simport': 4002, 'startx': 8, 'starty': 0, 'sizex': 8, 'sizey': 6}]

#inputs = [[port, priority, timeout, socket],
inputs = [{'port': 5007, 'priority': 0, 'timeout': 1},
          {'port': 5008, 'priority': 1, 'timeout': 1}]

input_sockets = []
for i in inputs:
    i['socket'] = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    i['socket'].bind(('localhost',i['port']))
    input_sockets.append(i['socket'])

for w in walls:
    w['socket'] = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    w['simsocket'] = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#q = Queue.Queue(100)
selected_input = inputs[0]


def is_timed_out(i):
    return time.time() - i['timestamp'] > i['timeout']

def send_to_wall(data, wall):
    wall['socket'].sendto(data, (wall['host'], wall['port']))
    wall['socket'].sendto(data, (wall['simhost'], wall['simport']))

def find_wall(x,y):
    # hack for congress
    if x < 8:
        return walls[0]
    return walls[1]

def translate_for_wall(x,y,wall):
    nx = x - wall['startx']
    ny = y - wall['starty']
    return nx,ny

# find better name
tainted = {}

def forward(data, source):
    #print data, 'from', source
    try:
        if source not in tainted:
            tainted['source'] = []

        x = ord(data[0])
        y = ord(data[1])
        cmd = data[2]
        print x,y,cmd

        if cmd != 'U':
            wall = find_wall(x, y)
            x,y = translate_for_wall(x,y,wall)
            data = '%c%c%s'%(chr(x), chr(y), data[2:])
            print '->', x, y, wall['simport']
            send_to_wall(data, wall)
            if wall not in tainted['source']:
                tainted['source'].append(wall)
        else:
            for wall in tainted['source']:
                send_to_wall(data, wall)
            tainted['source'] = []
    except Exception as e:
        print "Unexpected error:", e


while True:
    readable = select.select(input_sockets, [], [])[0]
    for s in readable:
        i = [i for i in inputs if i['socket'] == s][0]
        i['last_frame'], i['last_addr'] = s.recvfrom(1024)
        i['timestamp'] = time.time()
        
        if i['priority'] >= selected_input['priority']:
            selected_input = i;
        elif is_timed_out(selected_input):
            selected_input = inputs[0]
            maxprio = 0
            for i in inputs:
                if i['priority'] >= maxprio and not is_timed_out(i):
                    selected_input = i
        else:
            continue

        forward(selected_input['last_frame'], str(selected_input['last_addr']))