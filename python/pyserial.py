import serial
import time

arduino = serial.Serial(port='COM12', baudrate=9600, timeout=.1)
while True:
    str = arduino.readline().decode('utf-8').strip() # format the input data
    if str:
        try:
            dist = float(str)
           # print("Object Dist: ",dist)
        except:
            print("error",str)
        finally:
            #print("eos") 
            continue