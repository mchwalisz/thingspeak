from time import localtime, strftime

# download from http://code.google.com/p/psutil/
import psutil
import time

import thingspeak

channel_id = 0  # PUT CHANNEL ID HERE
write_key = 0  # PUT YOUR WRITE KEY HERE


def doit(channel):

    cpu_pc = psutil.cpu_percent()
    mem_avail_mb = psutil.virtual_memory().percent

    try:
        response = channel.update({1: cpu_pc, 2: mem_avail})
        print(cpu_pc)
        print(mem_avail_mb)
        print(strftime("%a, %d %b %Y %H:%M:%S", localtime()))
        print(response)
    except:
        print("connection failed")


# sleep for 16 seconds (api limit of 15 secs)
if __name__ == "__main__":
    channel = thingspeak.Channel(id=channel_id, write_key=write_key)
    while True:
        doit(channel)
        time.sleep(16)
