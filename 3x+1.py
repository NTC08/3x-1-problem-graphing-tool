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
    scale_y = 0.07
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

ss = 1

pygame.init()
screen = pygame.display.set_mode((screen_size_x, screen_size_y))
pygame.display.set_caption("3x+1 graphing tool")
Clock = pygame.time.Clock()
font = pygame.font.Font(None, 25)
input_number = number
steps = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if ss == 1:
        if number % 2 == 0:
            number = number / 2
            old_pos_x = new_pos_x
            old_pos_y = new_pos_y
            new_pos_y = number
            new_pos_x = new_pos_x + space
            steps = steps + 1
            print(number)
        else:
            number = (number * 3) + 1
            old_pos_x = new_pos_x
            old_pos_y = new_pos_y
            new_pos_y = number
            new_pos_x = new_pos_x + space
            steps = steps + 1
            print(number)
    if ss != 0:
        pygame.draw.line(screen, "red", ((old_pos_x), ((old_pos_y*scale_y)-screen_size_y)*-1), ((new_pos_x), ((new_pos_y*scale_y)-screen_size_y)*-1), width)
        text = font.render("input = " + str(input_number) + " ", False, "white")
        text_rec = text.get_rect(topleft = (10,10))
        pygame.draw.rect(screen, "black",  text_rec,)
        screen.blit(text,(10,10))
        
        steps_text = font.render("current step = " + str(steps) + " ", False, "white")
        step_rec = steps_text.get_rect(topleft = (10,30))
        pygame.draw.rect(screen, "black",  step_rec,)
        screen.blit(steps_text,(step_rec))
        
        number_text = font.render("current number = " + str(number) + "           ", False, "white")
        number_rec = number_text.get_rect(topleft = (10,50))
        pygame.draw.rect(screen, "black",  number_rec,)
        screen.blit(number_text,(number_rec))
        
        pygame.display.update()
        Clock.tick(speed)
    if number == 1.0:
        ss = 0