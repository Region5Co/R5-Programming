import pygame
import json
from math import copysign
import serial

usb_port = 'COM3'
ser = serial.Serial(usb_port, 9600, timeout=1)  # add as serial windows edition
# ser = serial.Serial()
#  ser.open() I'm losing my gourd

buttonA = 0  # Button 0
buttonB = 0  # Button 1
buttonX = 0  # Button 2
buttonY = 0  # Button 3
bumperLeft = 0  # Button 4
bumperRight = 0  # Button 5
buttonShare = 0  # Button 6 yeah idk
buttonMenu = 0  # Button 7
buttonLStick = 0  # Button 8
buttonRStick = 0  # Button 9

leftXAxis = 0  # Axis 0
leftYAxis = 0  # Axis 1 (inverted i.e. up is negative values) thrust?
rightXAxis = 0  # Axis 2
rightYAxis = 0  # Axis 3
leftTrigger = 0  # Axis 4 (neutral is -1)
rightTrigger = 0  # Axis 5

inputArray = {}

# Hat we'll save for later (POV for my FRC heads)

pygame.init()

# Loop until close
done = False

pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)
joystick.init()

clock = pygame.time.Clock()

buttons = joystick.get_numbuttons()

while not done:
    # There's surely a better way to do this
    for event in pygame.event.get():
        pass

    buttonA = joystick.get_button(0)
    # buttonB = joystick.get_button(1)
    # buttonX = joystick.get_button(2)
    # buttonY = joystick.get_button(3)
    # buttonLeft = joystick.get_button(4)
    # buttonRight = joystick.get_button(5)
    # buttonShare = joystick.get_button(6)

    leftYAxis = -joystick.get_axis(1)  # Propeller Left Thrust (negative to invert value)
    leftYAxisSign = copysign(1, leftYAxis)
    leftYAxisAbs = round(abs(leftYAxis), 2)  # also rounds to two decimals


    rightYAxis = -joystick.get_axis(3)  # Propeller Right Thrust
    buttonMenu = joystick.get_button(7)  # Select: " "
    leftTrigger = joystick.get_axis(4)  # Depth Down
    rightTrigger = joystick.get_axis(5)  # Depth Up
    bumperLeft = joystick.get_button(4)  # : " "
    bumperRight = joystick.get_button(5)  # : " "
    buttonX = joystick.get_button(2)  # Intake
    buttonY = joystick.get_button(3)  # Output

    # inputArray = [
    #    leftYAxis,
    #    rightYAxis,
    #    buttonMenu,
    #    leftTrigger,
    #    rightTrigger,
    #    bumperLeft,
    #    bumperRight,
    #    buttonX,
    #    buttonY
    #]

    # test input arrays
    inputArray = [leftYAxisSign, leftYAxisAbs, buttonA]
    # inputArray = [buttonX, buttonY]

    jsonInputArray = json.dumps(inputArray).encode('utf-8')
    ser.write(jsonInputArray)  # this should work once connection is established

    # Limit fps to 30
    clock.tick(30)

pygame.quit()
