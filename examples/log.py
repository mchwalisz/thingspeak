from time import localtime, strftime
# download from http://code.google.com/p/psutil/
import psutil
import time

import thingspeak

cpu_pc = psutil.cpu_percent()
mem_avail_mb = psutil.avail_phymem()/1000000
channel = thingspeak.channel('YOURKEYHERE')

try:
    response = channel.update([cpu_pc, mem_avail_mb])
    print cpu_pc
    print mem_avail_mb
    print strftime("%a, %d %b %Y %H:%M:%S", localtime())
    print response.status, response.reason
    data = response.read()
except:
    print "connection failed"
