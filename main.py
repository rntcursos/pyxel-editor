import pygame, sys
from settings import *

pygame.init()

display = pygame.display.set_mode((WIDTH,HEIGHT))

#bar_tools
bar_tools = pygame.Surface(BAR_TOOLS_SIZE)
bar_tools.fill(TOOLS_COLOR)

#canvas
canvas = pygame.Surface(CANVAS_SIZE)
canvas.fill(TOOLS_COLOR)

#buttons
pencil = pygame.image.load("assets/pencil.png")
pencil_rect = pencil.get_rect(topleft=(20,70))

eraser = pygame.image.load("assets/eraser.png")
eraser_rect = pencil.get_rect(topleft=(100,70))

save = pygame.image.load("assets/save.png")
save_rect = pencil.get_rect(topleft=(20,150))

clean = pygame.image.load("assets/clean.png")
clean_rect = pencil.get_rect(topleft=(100,150))

#Tools
tool = "pencil"
size = 10
color = "white"

#UI_INFO
font = pygame.font.Font(None, 25)
info_size = font.render("size: " + str(size), False, "white")

info_color = pygame.Surface((60,60))
info_color.fill(color)
info_color_rect = info_color.get_rect(topleft=(60,260))

black = pygame.Surface((60,60))
black.fill("black")
black_rect = black.get_rect(topleft=(20,370))

white = pygame.Surface((60,60))
white.fill("white")
white_rect = white.get_rect(topleft=(100,370))

red = pygame.Surface((60,60))
red.fill("red")
red_rect = red.get_rect(topleft=(20,448))

green = pygame.Surface((60,60))
green.fill("green")
green_rect = green.get_rect(topleft=(100,448))

blue = pygame.Surface((60,60))
blue.fill("blue")
blue_rect = blue.get_rect(topleft=(20,524))

yellow = pygame.Surface((60,60))
yellow.fill("yellow")
yellow_rect = yellow.get_rect(topleft=(100,524))

orange = pygame.Surface((60,60))
orange.fill("orange")
orange_rect = orange.get_rect(topleft=(20,600))

pink = pygame.Surface((60,60))
pink.fill("pink")
pink_rect = pink.get_rect(topleft=(100,600))

while True:

    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
    key = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            if pencil_rect.collidepoint(event.pos):
                pencil.fill("black")
            else:
                pencil = pygame.image.load("assets/pencil.png")
            
            if eraser_rect.collidepoint(event.pos):
                eraser.fill("black")
            else:
                eraser = pygame.image.load("assets/eraser.png")
            
            if save_rect.collidepoint(event.pos):
                save.fill("black")
            else:
                save = pygame.image.load("assets/save.png")
            
            if clean_rect.collidepoint(event.pos):
                clean.fill("black")
            else:
                clean = pygame.image.load("assets/clean.png")
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and pencil_rect.collidepoint(event.pos):
                tool = "pencil"
            elif event.button == 1 and eraser_rect.collidepoint(event.pos):
                tool = "eraser"
            elif event.button == 1 and save_rect.collidepoint(event.pos):
                pygame.image.save(canvas, "image.png")
            elif event.button == 1 and clean_rect.collidepoint(event.pos):
                canvas.fill(TOOLS_COLOR)
            
            if event.button == 1 and black_rect.collidepoint(event.pos):
                color = "black"
                info_color.fill(color)
            elif event.button == 1 and white_rect.collidepoint(event.pos):
                color = "white"
                info_color.fill(color)
            elif event.button == 1 and red_rect.collidepoint(event.pos):
                color = "red"
                info_color.fill(color)
            elif event.button == 1 and green_rect.collidepoint(event.pos):
                color = "green"
                info_color.fill(color)
            elif event.button == 1 and blue_rect.collidepoint(event.pos):
                color = "blue"
                info_color.fill(color)
            elif event.button == 1 and yellow_rect.collidepoint(event.pos):
                color = "yellow"
                info_color.fill(color)
            elif event.button == 1 and orange_rect.collidepoint(event.pos):
                color = "orange"
                info_color.fill(color)
            elif event.button == 1 and pink_rect.collidepoint(event.pos):
                color = "pink"
                info_color.fill(color)
            
            if event.button == 4:
                size += 1
                info_size = font.render("size: " + str(size), False, "white")
            elif event.button == 5:
                size -= 1
                info_size = font.render("size: " + str(size), False, "white")

    if key[0] and tool == "pencil":
        pygame.draw.rect(canvas, color, [x - (x % size) - 270, y - (y % size) - 60,size,size])
    elif key[0] and tool == "eraser":
        pygame.draw.rect(canvas, TOOLS_COLOR, [x - (x % size) - 270, y - (y % size) - 60,size,size]) 

    display.blit(bar_tools, [0,0])
    display.blit(canvas, [270,60])

    bar_tools.fill(TOOLS_COLOR)
    bar_tools.blit(pencil, pencil_rect)
    bar_tools.blit(eraser, eraser_rect)
    bar_tools.blit(save, save_rect)
    bar_tools.blit(clean, clean_rect)
    bar_tools.blit(info_color, info_color_rect)
    bar_tools.blit(black, black_rect)
    bar_tools.blit(white, white_rect)
    bar_tools.blit(red, red_rect)
    bar_tools.blit(green, green_rect)
    bar_tools.blit(blue, blue_rect)
    bar_tools.blit(yellow, yellow_rect)
    bar_tools.blit(orange, orange_rect)
    bar_tools.blit(pink, pink_rect)
    bar_tools.blit(info_size, [20,10])

    pygame.display.update()