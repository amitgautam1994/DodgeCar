import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (19, 96, 189)
pink = (255, 128, 192)
yellow = (255,255,128)

d_red = (255, 0, 0)
d_green = (0, 255, 0)

car_width = 100

pause = False

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Dodge Car')
clock = pygame.time.Clock()

carImg = pygame.image.load('jeep1.png')

icon = pygame.image.load("jeepicon.png")

pygame.display.set_icon(icon)

def gamequit():
    pygame.quit()
    quit()

def button(msg, x, y, w, h, ac,ic, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # print(mouse)

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))


    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = (round(x + (w / 2)), round(y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)

def unpause():
    global pause
    pause = False

def paused():

    largeText = pygame.font.SysFont("comicsansms", 80)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = (round(display_width / 2), round(display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)



    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue", 200, 400, 100, 50, green, d_green, unpause)
        button("Quit", 500, 400, 100, 50, red, d_red, gamequit)


        pygame.display.update()

        clock.tick(10)

def game_intro():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(yellow)

        largeText = pygame.font.SysFont("comicsansms", 80)
        TextSurf, TextRect = text_objects("A Bit Racey", largeText)
        TextRect.center = (round(display_width / 2), round(display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!", 200, 400, 100, 50, green, d_green, game_loop)
        button("Quit", 500, 400, 100, 50, red, d_red, gamequit)

        pygame.display.update()

        clock.tick(10)


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged : " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def crash():

    largeText = pygame.font.SysFont("comicsansms", 80)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = (round(display_width / 2), round(display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play Again", 200, 400, 100, 50, green, d_green, game_loop)
        button("Quit", 500, 400, 100, 50, red, d_red, gamequit)

        pygame.display.update()

        clock.tick(10)


def game_loop():
    global pause

    x = round(display_width * 0.45)
    y = round(display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 90
    thing_height = 90

    dodged = 0
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(pink)

        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, blue)
        thing_starty += thing_speed
        car(x, y)

        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()


        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1

            if dodged % 3 == 0:
                thing_speed += 1

        if y < thing_starty + thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                crash()


        pygame.display.update()
        clock.tick(60)


game_intro()
game_loop()
pygame.quit()
quit()
