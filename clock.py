import time #for reading the time data
am_pm=""# for am /pm string
set_alarmhour = int(input("Set hour: "))
set_alarmmin = int(input("Set minutes: "))
set_am_pm = input("am / pm: ")
alarm_loop = 5 #For lopping the alert 
if set_am_pm == "pm":
	set_alarmhour = set_alarmhour +12
while True:
    from datetime import datetime
    now = datetime.now()# reading all time data like :month, day,hour,etc
    if now.hour <12:# this Condition is for separating  am and pm
    	am_pm = "am" 
    	hour = now.hour
    else:
    	am_pm = "pm"
    	hour = now.hour - 12	#to convert international  time to local time
    print ("%s/%s/%s %s:%s:%s%s%s" % (now.day,now.month,now.year,hour,now.minute,now.second," ",am_pm)),
    time.sleep(2)
    if set_alarmhour== now.hour and set_alarmmin == now.minute:
    	while alarm_loop>0:
    		print("Wake up coders")
    		alarm_loop = alarm_loop - 1
