from pyfirmata import arduino, util
import time

nano = Arduino(
    "COM3",
    baudrate=9600
)

