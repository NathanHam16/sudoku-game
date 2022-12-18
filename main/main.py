import pygame
import requests
pygame.init()

# INITIALISE DISPLAY #
WIDTH = 1100
background_colour = (255,255,255)
text_colour = (255, 255, 255)
win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Sudoku")
win.fill(background_colour)
pygame.display.update()
myfont = pygame.font.SysFont('Calibri', 32)

# LEVELS #
intro = True
instruction = False
game_start = False
difficulty = ""

# GAME LOAD SECTION #
page1 = pygame.image.load("main/startscreen.png").convert_alpha()
page2 = pygame.image.load("main/instructions.png").convert_alpha()
easy_button = pygame.Rect(200, 640, 250, 100) #xy width height
medium_button = pygame.Rect(400, 640, 250, 100)
hard_button = pygame.Rect(700, 640, 250, 100)

# LOOP #
while True:
    # GAME START MENU # 
    if intro:
        win.blit(page1, (0,0))
        pos = pygame.mouse.get_pos()
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP and easy_button.collidepoint(pos[0], pos[1]):
            difficulty = "Difficuly: Easy"
            response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
            intro = False
            instruction = True
        if event.type == pygame.MOUSEBUTTONUP and medium_button.collidepoint(pos[0], pos[1]):
            difficulty = "Difficulty: Medium"
            response = requests.get("https://sugoku.herokuapp.com/board?difficulty=medium")
            intro = False
            instruction = True
        if event.type == pygame.MOUSEBUTTONUP and hard_button.collidepoint(pos[0], pos[1]):
            difficulty = "Difficulty: Hard"
            response = requests.get("https://sugoku.herokuapp.com/board?difficulty=hard")
            intro = False
            instruction = True
        
    # CHOOSE DIFFICULTY MENU #
    if instruction:
        grid = response.json()['board']
        grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]
        win.fill(background_colour)
        win.blit(page2, (0,0))
        difficultystring = myfont.render(difficulty, True, text_colour)
        win.blit(difficultystring, (20,20))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    instruction = False
                    game_start = True
                    
    if game_start:
        display()
    
    def display():    
        pygame.init()
        pygame.display.set_caption("Sudoku")
        win.fill(background_colour)

        myfont = pygame.font.SysFont('Calibri', 90)
        pygame.display.update()
        
        for i in range(0,10):
            if(i%3 == 0):
                pygame.draw.line(win, (0,0,0), (100 + 100*i, 100), (100 + 100*i ,1000 ), 4)
                pygame.draw.line(win, (0,0,0), (100, 100 + 100*i), (1000, 100 + 100*i), 4)
            pygame.draw.line(win, (0,0,0), (100 + 100*i, 100), (100 + 100*i ,1000 ), 2)
            pygame.draw.line(win, (0,0,0), (100, 100 + 100*i), (1000, 100 + 100*i), 2)
        pygame.display.update()
        
        for i in range(0, len(grid[0])):
            for j in range(0, len(grid[0])):
                if(0<grid[i][j]<10):
                    value = myfont.render(str(grid[i][j]), True, text_colour)
                    win.blit(value, ((j+1)*100 + 30, (i+1)*100 + 15))
        pygame.display.update()


def insert(win, position):
    i,j = position[1], position[0]
    myfont = pygame.font.SysFont('Calibri', 90)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if(grid_original[i-1][j-1] != 0):
                    return
                if(event.key == 48): #checking with 0
                    grid[i-1][j-1] = event.key - 48
                    pygame.draw.rect(win, background_colour, (position[0]*100+3, position[1]*100+3, 96, 96))
                    pygame.display.update()
                    return
                if(0 < event.key - 48 <10):  #We are checking for valid input
                    pygame.draw.rect(win, background_colour, (position[0]*100 + 5, position[1]*100+5,100 -2*5 , 100 - 2*5))
                    value = myfont.render(str(event.key-48), True, (0,0,0))
                    win.blit(value, (position[0]*100 + 30, position[1]*100 + 15))
                    grid[i-1][j-1] = event.key - 48
                    pygame.display.update()
                    return
                return


    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            pos = pygame.mouse.get_pos()
            # insert(win, (pos[0]//100, pos[1]//100))
            pygame.display.update()
                
        if event.type == pygame.QUIT:
            pygame.quit()
    


    

