import pygame

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
    buttonB = joystick.get_button(1)

    # insert update values here
    if buttonA == 1:
        print("A")
    if buttonB == 1:
        print("B")

    # Limit fps to 60
    clock.tick(60)

pygame.quit()