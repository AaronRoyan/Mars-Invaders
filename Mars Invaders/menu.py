import pygame

pygame.init()
clock = pygame.time.Clock()

'#Background'
background = pygame.image.load("menubackground.jpg")

'#Create the screen'
screen = pygame.display.set_mode((800, 600))

grey = (140, 93, 87)
sun_yellow = (217, 149, 111)
'#Play'
play = pygame.font.Font("freesansbold.ttf", 40)

'#Exit'
leave = pygame.font.Font("freesansbold.ttf", 40)

def play_game(x, y):
    boom = play.render("Play", True, grey)
    screen.blit(boom, (x, y))

def exit_game(x, y):
    laid = leave.render("Exit", True, grey)
    screen.blit(laid, (x, y))

show_menu = True

while show_menu:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = show_menu = False
    
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    
    button_1 = pygame.Rect(560, 80, 200, 50)
    button_2 = pygame.Rect(560, 200, 200, 50)
    
    if 560 + 200 > mouse[0] > 560 and 80 + 50 > mouse[1] > 80:
        pygame.draw.rect(screen, sun_yellow, button_1)
        if click[0] == 1:
            # exec(open("Mars.py").read())
            running = True
            break
    else:
        pygame.draw.rect(screen, grey, button_1)
    if 560 + 200 > mouse[0] > 560 and 200 + 50 > mouse[1] > 200:
        pygame.draw.rect(screen, sun_yellow, button_2)
        if click[0] == 1:
            running = show_menu = False
    
    else:
        pygame.draw.rect(screen, grey, button_2)

    play_game(620, 85)
    exit_game(620, 206)
    clock.tick(60)
    pygame.display.update()
