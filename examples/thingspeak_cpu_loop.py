from time import localtime, strftime
# download from http://code.google.com/p/psutil/
import psutil
import time

import thingspeak

def doit(channel):
    cpu_pc = psutil.cpu_percent()
    mem_avail_mb = psutil.avail_phymem()/1000000

    try:
        response = channel.update([cpu_pc, mem_avail_mb])
        print cpu_pc
        print mem_avail_mb
        print strftime("%a, %d %b %Y %H:%M:%S", localtime())
        print response.status, response.reason
        data = response.read()
    except:
        print "connection failed"

#sleep for 16 seconds (api limit of 15 secs)
if __name__ == "__main__":
    channel = thingspeak.channel('YOURKEYHERE')
    while True:
        doit(channel)
        time.sleep(16)
