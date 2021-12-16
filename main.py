import time #for reading the time data
import sys 
am_pm=""# for am /pm string
while True:
    from datetime import datetime
    now = datetime.now()# reading all time data like :month, day,hour,etc
    if now.hour <12:# this Condition is for separating  am and pm
    	am_pm = "am" 
    	hour = now.hour
    else:
    	am_pm = "pm"
    	hour = now.hour - 12	#to convert international  time to local time
    print ("%s/%s/%s %s:%s:%s%s%s" % (now.month,now.day,now.year,hour,now.minute,now.second," ",am_pm)),
    sys.stdout.flush()
    print("\r"),
    time.sleep(1)
