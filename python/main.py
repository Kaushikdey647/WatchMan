from pyfirmata import Arduino, util
import time

#Definining the device with port and baud rate
uno = Arduino(
    "COM3",
    baudrate=9600
)
"""
*Using Iterators with pyFirmata*

itx = util.Iterator(uno) -> board name in parenthesis
itx.start() ->start iterator

*Getting pins for variables*

an_0 = board.get_pin('a:0:i')
di_0 = board.get_pin('d:6:p')
i -> input
o -> output
p -> pwm

*Pin Functions*

pin.read()
pin.write(val)
pin.mode(STATE)
pin.enable_reporting() -> allows reading inputs
"""
print("comms on")
while True:
    uno.digital[13].write(1)
    uno.digital[13].write(0)
