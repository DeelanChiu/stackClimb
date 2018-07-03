# import the pygame module, so you can use it
import pygame
from pygame.locals import *

# define a main function
def main():

    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((800,520))
    smiley = pygame.image.load('logo32x32.png').convert()

    position = smiley.get_rect()

    # define a variable to control the main loop
    running = True
    move_ticker = 0
    step = 10

    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        #    if event.type == pygame.KEYDOWN:
        #        if event.key == pygame.K_LEFT:
        #            position = position.move(-5, 0)
        #        if event.key == pygame.K_RIGHT:
        #            position = position.move(5, 0)
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[K_LEFT] and move_ticker == 0:
                move_ticker = 1
                position = position.move(-step, 0)
            if keys[K_RIGHT] and move_ticker == 0:
                move_ticker = 1
                position = position.move(step, 0)
            if keys[K_UP] and move_ticker == 0:
                move_ticker = 1
                position = position.move(0, -step)
            if keys[K_DOWN] and move_ticker == 0:
                move_ticker = 1
                position = position.move(0, step)

            if move_ticker > 0:
                move_ticker -= 1



        screen.fill((65,105,225))
        #position = position.move(2, 0)
        screen.blit(smiley,position)
        pygame.display.update()
        pygame.time.delay(100)


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
