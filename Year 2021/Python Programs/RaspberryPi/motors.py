#read line works, I'm happy (i think)
import serial
import json
import time

usb_port = '/dev/ttyACM0' # find usb port name on raspberry pi
ser = serial.Serial(usb_port, 9600, timeout=1)
ser.flush()

input_array = []
# test array format
# [left_y_axis, right_y_axis]

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip() # we'll keep em for now
        input_array = json.loads(line)

    # motor code

    time.sleep(0.5)

ser.close()

