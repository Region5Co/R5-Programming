import serial
import socket
import json
from time import sleep
import RPi.GPIO as GPIO

in1 = 24
in2 = 23
en = 25
temp1 = 1

# value indexes
left_y_axis_sign = 0
left_y_axis_abs = 1
button_A = 2
button_menu = 3

HOST = "(insert host ip)"
PORT = 8001 # The port used on server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
p = GPIO.PWM(en, 1000)

p.start(25)

# usb_port = '/dev/ttyUSB0'  # find usb port name on raspberry pi
# ser = serial.Serial(usb_port, 9600, timeout=1)
# ser.flush()

input_array = []
buffer = b''
# test array format
# [button_A, button_B]
# [left_y_axis, right_y_axis]

while True:
    # if ser.in_waiting > 0:
    #    line = ser.readline().decode('utf-8').rstrip()  # we'll keep em for now
    #    input_array = json.loads(line)

    while b'\n' not in buffer:
        data = sock.recv(1024)
        if not data:
            break
        buffer += data
    line, sep, buffer = buffer.partition(b'\n')
    decoded_line = line.decode('utf-8').rstrip()
    input_array = json.loads(decoded_line)

    # example motor code
    if not input_array[button_A]:   # Hold A button to enable (mainly for safety)
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
    else:   # Adjust Direction
        if input_array[left_y_axis_sign] == 1:  # Forwards
            GPIO.output(in1, GPIO.HIGH)
            GPIO.output(in2, GPIO.LOW)
        else:
            GPIO.output(in1, GPIO.LOW)  # Backwards
            GPIO.output(in2, GPIO.HIGH)
        p.ChangeDutyCycle(input_array[left_y_axis_abs])  # Adjust Speed

    if input_array[button_menu]:  # In this case, a kill button?
        GPIO.cleanup()
        break

    sleep(0.5)

# ser.close()
sock.close()
