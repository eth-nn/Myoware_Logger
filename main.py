from emgLogger import emgLog
import machine
import utime
import os

status = machine.Pin(16, machine.Pin.OUT) #Pin D0
status.value(1)

def start():
    rate = 0.1
    while True:
        filename = input("New Filename: ")
        
        print("Current Sample Rate: ", rate)
        if (input("Change Sample Rate? [y/n]") == 'y'):
            rate = input("Enter Rate in Seconds")
        status.value(1)
        emgLog(filename, float(rate))
        status.value(0)

def rmFi(thename): 
    if(input("Remove: ", thename,"?") == 'y'):
        os.remove(thename)
    print("Removed: ",thename,"\n", os.listdir)


utime.sleep(1)
print("EMG Logger ready to start...")
status.value(0)