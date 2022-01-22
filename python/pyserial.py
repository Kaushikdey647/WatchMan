import serial
import time

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
while True:
    str = arduino.readline().decode().strip()
    if str:
        dist = float(str)
        #if dist < 50:
        #     your code here
        