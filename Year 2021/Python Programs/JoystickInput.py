import pygame

pygame.init()

# Loop until close
done = False

pygame.joystick.init()

# while not done:
#    for event in pygame.event.get():
joystick = pygame.joystick.Joystick(0)
joystick.init()

buttonA = joystick.get_button(1) # Things to configure
buttons = joystick.get_numbuttons()

print(buttons)

while not done:
    for i in range(buttons):
        button = joystick.get_button(i)
        print("Button {:>2} value: {}".format(i, button))
