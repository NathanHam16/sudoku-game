import pygame
from gridgenerator import get_grid
background_colour = (255,255,255)
buffer = 5
red = (255,160,122)

def insert(win, position):
    grid = get_grid()
    i,j = position[1], position[0]
    myfont = pygame.font.SysFont('Calibri', 90)
    while True:
        pygame.draw.rect(win, red, (position[0]*100 + 6, position[1]*100+5,100 - 2*5 , 90))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if(event.key == 48): #checking with 0
                    grid[i-1][j-1] = event.key - 48
                    pygame.draw.rect(win, background_colour, (position[0]*100+3, position[1]*100+3, 96, 96))
                    pygame.display.update()
                    return
                if(0 < event.key - 48 <10):  #We are checking for valid input
                    pygame.draw.rect(win, background_colour, (position[0]*100 + 6, position[1]*100+5,100 -2*5 , 100 - 2*5))
                    value = myfont.render(str(event.key-48), True, (0,0,0))
                    win.blit(value, (position[0]*100 + 30, position[1]*100 + 15))
                    grid[i-1][j-1] = event.key - 48
                    pygame.display.update()
                    return
                return