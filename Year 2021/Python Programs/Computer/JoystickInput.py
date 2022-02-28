import pygame
import json
from math import copysign
# import serial
import socket

# usb_port = 'COM3'
# ser = serial.Serial(usb_port, 9600, timeout=1)  # add as serial windows edition

HOST = "localhost"
PORT = 8001

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))

dead_zone = 25  # Arbitrary dead zone

button_A = 0  # Button 0
buttonB = 0  # Button 1
button_X = 0  # Button 2
button_Y = 0  # Button 3
bumper_left = 0  # Button 4
bumper_right = 0  # Button 5
buttonShare = 0  # Button 6 yeah idk
button_menu = 0  # Button 7
buttonLStick = 0  # Button 8
buttonRStick = 0  # Button 9

leftXAxis = 0  # Axis 0
leftYAxis = 0  # Axis 1 (inverted i.e. up is negative values) thrust?
rightXAxis = 0  # Axis 2
right_y_axis = 0  # Axis 3
trigger_left = 0  # Axis 4 (neutral is -1)
trigger_right = 0  # Axis 5

inputArray = []

# Hat we'll save for later (POV for my FRC heads)

pygame.init()

# Loop until close
done = False

pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)
joystick.init()

clock = pygame.time.Clock()

print("Currently listening for connection...")
sock.listen()
conn, addr = sock.accept() # will wait to get joystick inputs until 1st successful connection
print(f"Connected by {addr}")

while not done:
    # There's surely a better way to do this
    for event in pygame.event.get():
        pass

    button_A = joystick.get_button(0)
    # button_B = joystick.get_button(1)
    # button_X = joystick.get_button(2)
    # button_Y = joystick.get_button(3)
    # button_left = joystick.get_button(4)
    # button_right = joystick.get_button(5)
    # button_share = joystick.get_button(6)

    left_y_axis = -joystick.get_axis(1) * 100   # Propeller Left Thrust (negative to invert value)
    left_y_axis_sign = copysign(1, left_y_axis)
    left_y_axis_abs = round(abs(left_y_axis))   # rounds to clean number
    if left_y_axis_abs < dead_zone:             # apply dead zone
        left_y_axis_abs = 0

    #  Possible inputs
    right_y_axis = -joystick.get_axis(3) * 100 # Propeller Right Thrust
    button_menu = joystick.get_button(7)  # Select: " "
    trigger_left = joystick.get_axis(4)  # Depth Down
    trigger_right = joystick.get_axis(5)  # Depth Up
    bumper_left = joystick.get_button(4)  # : " "
    bumper_right = joystick.get_button(5)  # : " "
    button_X = joystick.get_button(2)  # Intake
    button_Y = joystick.get_button(3)  # Output

    # inputArray = [
    #    left_y_axis,
    #    right_x_axis,
    #    button_menu,
    #    trigger_left,
    #    trigger_right,
    #    bumper_left,
    #    bumper_right,
    #    button_X,
    #    button_Y
    # ]

    # test input arrays
    inputArray = [left_y_axis_sign, left_y_axis_abs, button_A, button_menu]
    # inputArray = [buttonX, buttonY]

    jsonInputArray = json.dumps(inputArray).encode('utf-8')

    conn.sendall(jsonInputArray)

    # ser.write(jsonInputArray)  # this should work once connection is established

    # Limit fps to 30
    clock.tick(30)

pygame.quit()
