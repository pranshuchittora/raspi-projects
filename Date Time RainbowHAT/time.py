import datetime
import time
import threading
import rainbowhat as rh

def formatter(flag):
    if(flag<=9):
        return str('0'+str(flag))
    else:
        return flag

    
def displayLong(name):
    name = name +'    '
    for i in range(len(name)-3):
        a=name[i]
        b=name[i+1]
        c=name[i+2]
        d=name[i+3]
        rh.display.print_str(str(a+b+c+d))
        rh.display.show()

        time.sleep(0.4)
        if(i==len(name)-4):
            i=0
        else:
            i=i+1
def displaySingle(name):
    for i in range(10):
        rh.display.print_str(str(name))
        rh.display.show()
        time.sleep(0.8)
        rh.display.print_str('    ')
        rh.display.show()
        time.sleep(0.4)

    
        
def funct():
    while True:
        now =datetime.datetime.now()
        minutes=formatter(now.minute)
        hours=formatter(now.hour)
        date = formatter(now.day)
        month=formatter(now.month)
        year = now.year
        
        dateStr=str(date)+'-'+str(month)+'-'+str(year)
        timeStr=str(hours)+str(minutes)
        displayLong(dateStr)
        displaySingle(timeStr)
        rh.display.show()
        

funct()

    
    
    
    




