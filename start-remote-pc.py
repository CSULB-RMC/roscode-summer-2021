#!/usr/bin/env python3

import os.path
import sys
import socket


default_remote_pc_ip='192.168.0.100'
default_rover_ip='192.168.0.103'


joydev=''

for x in range(6):
    jsts = '/dev/input/js' + str(x)
    if os.path.exists(jsts):
        joydev=jsts
        break

if joydev == '':
    print('###############################')
    print('WARNING: Joypad not detected.  Joy nodes will not work.')
    print('###############################')
else:
    print('Joy device is', joydev)
    joydev = '--device=' + joydev

nc_env=''
if '-no-cache' in sys.argv:
    nc_env='--no-cache'

#following was just copy-pasted from stack overflow.  I dont understand it that well
#but it seems to work from my testing...
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.connect(('<broadcast>', 0))
auto_ip = s.getsockname()[0]
print('Auto Detected Host IP:', auto_ip)
print('')
if '-auto-ip' in sys.argv:
    inp_hostip = auto_ip
else:
    inp_hostip = str(input('Enter Host Ip [' + auto_ip + ']: '))
    if inp_hostip == '':
        inp_hostip = auto_ip
    else:
        #small check just to make sure it actually is an IP
        inp_hostip = inp_hostip.strip()
        try:
            socket.inet_aton(inp_hostip)
        except socket.error:
            print('Sorry, Ip address invalid.')
            quit()

print('uid:', os.getuid())
print('gid:', os.getgid())

docparams='--network host -e ROS_MASTER_URI=http://' + inp_hostip + ':11311 -e ROS_HOSTNAME=' + inp_hostip + ' -v $PWD:/ros -w /ros'

fullbuildexec = 'docker build ' + nc_env + ' --build-arg USER_ID=' + str(os.getuid()) + ' --build-arg GROUP_ID=' + str(os.getgid()) + ' docker -t rmc:ros'
os.system(fullbuildexec)
fullrunexec = 'docker run ' + docparams + ' ' + joydev + ' --rm -it rmc:ros /bin/bash'
os.system(fullrunexec)