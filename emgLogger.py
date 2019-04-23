from machine import ADC
import machine
import utime

# The inputs
adc = ADC(0) # Opens the Analog pin to read
stopButton = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP) #Pin D1

# LEDs
led1 = machine.Pin(4, machine.Pin.OUT) #Pin D2
led2 = machine.Pin(0, machine.Pin.OUT) #Pin D3
led3 = machine.Pin(2, machine.Pin.OUT) #Pin D4
led4 = machine.Pin(14, machine.Pin.OUT) #Pin D5

#Thresholds
led1_thresh = 256
led2_thresh = 512
led3_thresh = 768
led4_thresh = 1024

def updateLed(volt):
    if volt >= led1_thresh:
        led1.value(1)
    else:
        led1.value(0)

    if volt >= led2_thresh:
        led2.value(1)
    else:
        led2.value(0)

    if volt >= led3_thresh:
        led3.value(1)
    else:
        led3.value(0)

    if volt >= led4_thresh:
        led4.value(1)
    else:
        led4.value(0)

def emgLog(filename, sampleRate):
    print("Recording Starting...")
    thetime = 0

    with open(filename, "w") as file:
        while stopButton.value() != 0:
            rawIn = adc.read()
        
            #Convert the Raw 1024 value to 0 > 3.3 Volts
            volt = rawIn * (3.3/1024)

            file.write('{:d}, {:5.3f}\n'.format(thetime, volt))
            print(volt)
            updateLed(rawIn)

            thetime += 1
            utime.sleep(sampleRate) 

    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(0)
    print("Recording Stopped...")