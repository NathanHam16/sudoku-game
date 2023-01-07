import pygame
from gridgenerator import possible
import numpy as np
background_colour = (255,255,255)
buffer = 5
red = (255,160,122)

def insert(grid, grid_copy, win, position):
    i,j = position[1], position[0]
    myfont = pygame.font.SysFont('Calibri', 90)
    if(grid_copy[i-1][j-1] != 0):
        return
    pygame.draw.rect(win, red, (position[0]*100 + 6, position[1]*100+5,100 - 2*5 , 90))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                input = event.key - 48
                if(event.key == 48): #checking with 0
                    grid[i-1][j-1] = input
                    pygame.draw.rect(win, background_colour, (position[0]*100+3, position[1]*100+3, 96, 96))
                    pygame.display.update()
                    return
                if(0 < input <10):  #We are checking for valid input
                    pygame.draw.rect(win, background_colour, (position[0]*100 + 6, position[1]*100+5,100 -2*5 , 100 - 2*5))
                    value = myfont.render(str(event.key-48), True, (100,100,100))
                    wrongvalue = myfont.render(str(event.key-48), True, (238, 75, 43))
                    if (possible(grid, i-1, j-1, input) == True):
                        win.blit(value, (position[0]*100 + 30, position[1]*100 + 15))
                    else:
                        win.blit(wrongvalue, (position[0]*100 + 30, position[1]*100 + 15))
                    grid[i-1][j-1] = input
                    pygame.display.update()
                    return
                return