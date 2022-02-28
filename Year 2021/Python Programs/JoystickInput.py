import pygame

buttonA = 0 # Button 0
buttonB = 0 # Button 1
buttonX = 0 # Button 2
buttonY = 0 # Button 3
bumperLeft = 0 # Button 4
bumperRight = 0 # Button 5
buttonShare = 0 # Button 6 yeah idk
buttonMenu = 0 # Button 7
buttonLStick = 0 # Button 8
buttonRStick = 0 # Button 9

leftXAxis = 0 # Axis 0
leftYAxis = 0 # Axis 1 (inverted i.e. up is negative values) thrust?
rightXAxis = 0 # Axis 2
rightYAxis = 0 # Axis 3
leftTrigger = 0 # Axis 4 (neutral is -1)
rightTrigger = 0 # Axis 5

#Hat we'll save for later (POV for my FRC heads)

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

    #buttonA = joystick.get_button(0)
    #buttonB = joystick.get_button(1)
    #buttonX = joystick.get_button(2)
    #buttonY = joystick.get_button(3)
    #buttonLeft = joystick.get_button(4)
    #buttonRight = joystick.get_button(5)
    #buttonShare = joystick.get_button(6)

    leftYAxis = -joystick.get_axis(1) # Propeller Left Thrust (invert value)
    rightYAxis = -joystick.get_axis(3) # Propeller Right Thrust
    buttonMenu = joystick.get_button(7) # Select: " "
    leftTrigger = joystick.get_axis(4) # Depth Down
    rightTrigger = joystick.get_axis(5) # Depth Up
    bumperLeft = joystick.get_button(4) # : " "
    bumperRight = joystick.get_button(5) # : " "
    buttonX = joystick.get_button(2) # Intake
    buttonY = joystick.get_button(3) # Output

    # maybe it should be event handling style, that depends if I can juice
    if leftYAxis > .8:
        print("Left Forward")
    elif leftYAxis < -.8:
        print("Left Backward")

    if rightYAxis > .8:
        print("Right Forward")
    elif rightYAxis < -.8:
        print("Right Backward")

    if leftTrigger > .8:
        print("Depth Down")
    elif rightTrigger > .8:
        print("Depth Up")

    if buttonX == 1:
        print("Intake On")
    if buttonY == 1:
        print("Output On")

    # Limit fps to 30
    clock.tick(30)

pygame.quit()