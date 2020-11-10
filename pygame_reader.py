import pygame, sys
from PIL import Image
import cv2 as cv

#window setup
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Document Reader Beta')
screen_width= 800
screen_height= 800
screen = pygame.display.set_mode((screen_width,screen_height),0,0) #check args

img = Image.open('Bonilla, Martha J 907023423UB.png')
width, height = Image.open('Bonilla, Martha J 907023423UB.png').size
# new_size = (int(width/4),int(height/4))
# resized = img.resize(new_size)
# small_img = resized.save('small Bonilla.png')

img = pygame.image.load('Bonilla, Martha J 907023423UB.png').convert()

print('image size is', width,'x',height)

#upper left caption
med_icon = Image.open('medical icon33small.png')
new_size = (32,32)
med_icon = med_icon.resize(new_size)
med_icon = med_icon.save('med_icon_pillow_small.png')
med_icon_img = pygame.image.load('med_icon_pillow_small.png').convert()
pygame.display.set_icon(med_icon_img)

left_click = False

#get ROI coordinates
while True:
    screen.fill((0,0,0))
    mx, my = pygame.mouse.get_pos()
    x_dest = 10
    y_dest = 10
    screen.blit(img,(x_dest,y_dest))
    screen.scroll(1250,800)


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button ==1:
                x1, y1 = (pygame.mouse.get_pos())
                left_click = True
        if event.type == MOUSEBUTTONUP:
            if event.button ==1:
                x2, y2 = (pygame.mouse.get_pos())
                print('screen position is', (x1, y1),(x2, y2))
                print('image position is', (x1-x_dest, y1 - y_dest),
                'x', (x2- x_dest, y2-y_dest))

    pygame.display.update()
    mainClock.tick(60)
