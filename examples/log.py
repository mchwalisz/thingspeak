from time import localtime, strftime
import psutil
import time

import thingspeak
channel_id = # PUT CHANNEL ID HERE
write_key  = # PUT YOUR WRITE KEY HERE

cpu_pc = psutil.cpu_percent()
mem_avail = psutil.virtual_memory().percent

channel = thingspeak.Channel(id=channel_id,write_key=write_key)

try:
    response = channel.update({1:cpu_pc, 2:mem_avail})
    print cpu_pc
    print mem_avail_mb
    print strftime("%a, %d %b %Y %H:%M:%S", localtime())
    print response
except:
    print "connection failed"
