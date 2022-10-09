import pygame
import sys

number = int(input("input number : "))
screen_size_x = (input("input screen size x : "))
if bool(screen_size_x) == False:
    screen_size_x = 800
screen_size_x = int(screen_size_x)

screen_size_y = (input("input screen size y : "))
if bool(screen_size_y) == False:
    screen_size_y = 750
screen_size_y = int(screen_size_y)

scale_y = (input("input scale : "))
if bool(scale_y) == False:
    scale_y = 0.5
scale_y = float(scale_y)

space = input("input space between points : ")
if bool(space) == False:
    space = 2
space = float(space)

width = input("input width : ")
if bool(width) == False:
    width = 1
width = int(width)

speed = input("input speed : ")
if bool(speed) == False:
    speed = 30
speed = int(speed)

new_pos_x = 0
new_pos_y = number

old_pos_x = 0
old_pos_y = 0

pygame.init()
screen = pygame.display.set_mode((screen_size_x, screen_size_y))
pygame.display.set_caption("3x+1 graphing tool")
Clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if number % 2 == 0:
           number = number / 2
           old_pos_x = new_pos_x
           old_pos_y = new_pos_y
           new_pos_y = number
           new_pos_x = new_pos_x + space
    elif number % 2 != 0:
        number = (number * 3) + 1
        old_pos_x = new_pos_x
        old_pos_y = new_pos_y
        new_pos_y = number
        new_pos_x = new_pos_x + space
    pygame.draw.line(screen, "red", ((old_pos_x), ((old_pos_y*scale_y)-screen_size_y)*-1), ((new_pos_x), ((new_pos_y*scale_y)-screen_size_y)*-1), width)
    pygame.display.update()
    Clock.tick(speed)
    
    