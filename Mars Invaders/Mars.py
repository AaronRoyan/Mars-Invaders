import pygame
import random
import sys
from math import pow, sqrt
from pygame import mixer

from menu import running

'#Initialize the Pygame'
pygame.init()
clock = pygame.time.Clock()


'#Create the screen'
screen = pygame.display.set_mode((800, 600))

'#Background'
background = pygame.image.load("background.png")

'#Background music'
mixer.music.load("background.wav")
mixer.music.play(-1)

'#Title & Icon'
pygame.display.set_caption("Mars Invaders")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

'#player'
playerImg = pygame.image.load("spaceship(Tron2).png")
player_fall = pygame.image.load("spaceship(Tron2) - Copy.png")
playerX = 370
playerY = 480
playerXR_change = 0
playerXL_change = 0
playerYU_change = 0
playerYD_change = 0
player_life = 5

'#Reinforcements'
maverick = pygame.image.load("spaceship(Tron).png")
maverickX = 320
maverickY = 520
maverickXR_change = playerXR_change
maverickXL_change = playerXL_change
maverickYU_change = playerYU_change
maverickYD_change = playerYD_change

'#Explosion'
exp = pygame.image.load("explosion.png")

'#Game over'
over_text = pygame.font.Font('SPACEBAR.ttf', 64)

'#Enemy1'
enemy1 = []
enemy1X = []
enemy1Y = []
enemy1X_change = []
enemy1Y_change = []
no_of_enemies = 6

for i in range(no_of_enemies):
    enemy1.append(pygame.image.load("enemy1.png"))
    enemy1X.append(random.randint(20, 725))
    enemy1Y.append(random.randint(20, 400))
    enemy1X_change.append(random.randint(15, 25))
    enemy1Y_change.append(random.randint(15, 25))

'#Bullet'
bullet = pygame.image.load("bullet2.png")
bulletX = 370
bulletY = 480
bulletX_change = 0
bulletY_change = 0
bullet_state = "ready & hot"

'#Bullet1'
bullet1 = pygame.image.load("bullet2.png")
bullet1X = 370
bullet1Y = 480
bullet1X_change = 0
bullet1Y_change = 0
bullet1_state = "ready & hot"

'#Bullet2'
bullet2 = pygame.image.load("hot.png")
bullet2X = 334
bullet2Y = 545
bullet2X_change = 0
bullet2Y_change = 0
bullet2_state = "ready & hot"

'#Score'
score1 = 0
score2 = 0

total = score1 + score2
total_font = pygame.font.Font("freesansbold.ttf", 22)
textX = 10
textY = 10

print(f"You have {player_life} lives")

'#Total score'
high_font = pygame.font.Font("freesansbold.ttf", 22)
high_score = 0

'#Enemy life'
enemy1_life = 1

'#Colours'
white = (255, 255, 255)


def show_score(x, y):
    score = total_font.render("Score:" + str(total), True, white)
    screen.blit(score, (x, y))


def high_total():
    score = total_font.render("High Score:" + str(high_score), True, white)
    screen.blit(score, (135, 10))


def game_over():
    over = over_text.render("GAME OVER", True, white)
    screen.blit(over, (170, 250))
    re_game = mixer.Sound("bowser-killed.wav")
    re_game.play()


def player(x, y):
    screen.blit(playerImg, (x, y))


def player_falling(x, y):
    screen.blit(player_fall, (x, y))


def cavalry(x, y, a, b):
    global bullet2_state
    bullet2_state = "fire"
    screen.blit(bullet2, (a, b))
    screen.blit(maverick, (x, y))



def enemy(x, y):
    screen.blit(enemy1[i], (x, y))


def fire_bullets(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x + 4, y + 25))


def fire_bullets1(x, y):
    global bullet1_state
    bullet1_state = "fire"
    screen.blit(bullet1, (x + 44, y + 25))


def explosion(x, y):
    screen.blit(exp, (x, y))


def collision(enemy1X, enemy1Y, bulletX, bulletY):
    distance = sqrt(pow(enemy1X - bulletX, 2) + pow(enemy1Y - bulletY, 2))
    if distance < 32:
        return True
    else:
        return False


def player_collision(enemy1X, enemy1Y, playerX, playerY):
    distance = sqrt(pow(enemy1X - playerX, 2) + pow(enemy1Y - playerY, 2))
    if distance < 27:
        return True
    else:
        return False


'#Game loop'
# running = True
# finished = True

while running:

    '#RGB'
    screen.fill((0, 0, 0))

    '#Background'
    screen.blit(background, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("User has exited")
            running = False
            sys.exit()

        "#Game over"
        if player_life == 0:
            playerX = 370
            playerY = 480
            print("Game Over")
            player_life = 5
            score1 = 0
            score2 = 0

        '#KeyBinding'

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_LEFT:
                playerXL_change = 10
                # print("Left key is pressed")
            if event.key == pygame.K_RIGHT:
                playerXR_change = 10
                # print("Right key is pressed")
            if event.key == pygame.K_UP:
                playerYU_change = 10
                # print("UP key is pressed")
            if event.key == pygame.K_DOWN:
                playerYD_change = 10
                # print("DOWN key is pressed")
            if event.key == pygame.K_SPACE:
                "#Bullet"
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound("fire.wav")
                    bullet_sound.play()

                    bullet_state = "fire"
                    fire_bullets(bulletX, bulletY)

                '#Bullet Movement'

                if bullet_state is "fire":
                    bulletX = playerX
                    bulletY = playerY
                    fire_bullets(bulletX, bulletY)
                    bulletY_change = -20
                    # print("Fire !")
                if bulletY <= 0:
                    bulletX = 370
                    bulletY = 480
                    bullet_state = "ready"

                '#Bullet1'

                if bullet1_state is "ready":
                    bullet_sound = mixer.Sound("fire.wav")
                    bullet_sound.play()

                    bullet1_state = "fire"
                    bullet1X = playerX
                    bullet1Y = playerY
                    fire_bullets1(bullet1X, bullet1Y)

                '#Bullet1 Movement'

                if bullet1_state is "fire":
                    bullet1X = playerX
                    bullet1Y = playerY
                    fire_bullets1(bullet1X, bullet1Y)
                    bullet1Y_change = -20
                    # print("Fire 1 !")
                if bullet1Y <= 0:
                    bullet1X = 370
                    bullet1Y = 480
                    bullet1_state = "ready"

                '#Bullet2'

                if bullet2_state is "ready":
                    bullet_sound = mixer.Sound("fire.wav")
                    bullet_sound.play()
                    bullet2_state = "fire"
                    bullet2X = maverickX
                    bullet2Y = maverickY
                    cavalry(maverickX, maverickY, bullet2X, bullet2Y)
 
                '#Bullet2 Movement'

                if bullet2_state is "fire":
                    bullet2X = maverickX
                    bullet2Y = maverickY
                    cavalry(maverickX, maverickY, bullet2X, bullet2Y)
                    bullet2Y_change = -20
                    bullet2Y += bullet2Y_change
                    # print("Fire 1 !")
                if bullet2Y <= 0:
                    bullet2X = 334
                    bullet2Y = 540
                    bullet2_state = "ready"

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP \
                    or event.key == pygame.K_DOWN:
                playerXR_change = 0
                playerXL_change = 0
                playerYU_change = 0
                playerYD_change = 0
                # print("Key Stroke has been released")

    '#Boundaries'

    if playerX <= 0:
        playerX = 0
    elif playerX >= 725:
        playerX = 725

    if playerY <= 0:
        playerY = 0
    elif playerY >= 525:
        playerY = 525

    for i in range(no_of_enemies):
        '#Game over'
        if player_life == 0:
            playerX = 370
            playerY = 480
            for j in range(no_of_enemies):
                enemy1Y[j] = 2000
            total = 0
            game_over()
            break

        '#Enemy movement'

        enemy1X[i] += enemy1X_change[i]
        if enemy1X[i] <= 0:
            enemy1X_change[i] = 6
            enemy1Y[i] += enemy1Y_change[i]
        elif enemy1X[i] >= 750:
            enemy1X_change[i] = -6
            enemy1Y[i] += enemy1Y_change[i]

        enemy1Y[i] += enemy1Y_change[i]
        if enemy1Y[i] <= 0:
            enemy1Y_change[i] = 6
            enemy1Y[i] += enemy1Y_change[i]
        elif enemy1Y[i] >= 550:
            enemy1Y_change[i] = -6
            enemy1Y[i] += enemy1Y_change[i]

        'Collision course'
        collision1 = collision(enemy1X[i], enemy1Y[i], bulletX, bulletY)
        if collision1:
            bulletX = playerX
            bulletY = playerY
            bullet_state = "ready"
            score1 += 0.5
            enemy1_life -= 0.5

        collision2 = collision(enemy1X[i], enemy1Y[i], bullet1X, bullet1Y)
        if collision2:
            bullet1X = playerX
            bullet1Y = playerY
            bullet1_state = "ready"
            enemy1_life -= 0.5
            score2 += score1
            total = score1 + score2

        if collision1 and collision2:
            explosion(enemy1X[i], enemy1Y[i])
            explosion_sound = mixer.Sound("exp911.wav")
            explosion_sound.play()
            enemy1_life = 1
            enemy1X[i] = random.randint(20, 725)
            enemy1Y[i] = random.randint(20, 400)
        enemy(enemy1X[i], enemy1Y[i])

        P1_collision = player_collision(enemy1X[i], enemy1Y[i], playerX, playerY)
        if P1_collision:
            player_falling(playerX, playerY)
            maverickX = 320
            maverickY = 520
            playerX = 370
            playerY = 480
            player_life -= 1
            respawn = mixer.Sound("sm-killed.wav")
            respawn.play()
            enemy1X[i] = random.randint(20, 725)
            enemy1Y[i] = random.randint(20, 400)
            print(f"You have {player_life} lives left")

    playerX += playerXR_change
    playerX -= playerXL_change
    playerY -= playerYU_change
    playerY += playerYD_change
    maverickX += playerXR_change
    maverickX -= playerXL_change
    maverickY -= playerYU_change
    maverickY += playerYD_change
    bulletY += bulletY_change
    bullet1Y += bullet1Y_change
    fire_bullets(bulletX, bulletY)
    fire_bullets1(bullet1X, bullet1Y)
    show_score(textX, textY)
    high_total()
    player(playerX, playerY)
    if total >= 0:
        cavalry(maverickX, maverickY, bullet2X, bullet2Y)
    if total > high_score:
        high_score = total
    # bulletY_change = playerYU_change, playerYD_change
    # bullet1Y_change = playerYU_change, playerYD_change
    bulletX_change = playerXL_change, playerXR_change
    bullet1X_change = playerXL_change, playerXR_change
    clock.tick(60)
    pygame.display.update()
