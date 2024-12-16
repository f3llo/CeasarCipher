import pygame
import random

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 1000, 600
PLAYER_SIZE = (WIDTH / 32 , HEIGHT / 3)
BALL_SIZE = (20,20)
PLAYER_COLOR = (255,255,255)
FONT_SIZE = 80
BALL_VELOCITY = 200

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
dt = 0 #delta time

player1_pos = pygame.Vector2(20, (HEIGHT/2)-(PLAYER_SIZE[1]/2))
player2_pos = pygame.Vector2(WIDTH-20-PLAYER_SIZE[0],(HEIGHT/2)-(PLAYER_SIZE[1]/2))
ball_pos = pygame.Vector2(WIDTH/2-BALL_SIZE[0], HEIGHT/2-BALL_SIZE[0])
score_1, score_2 = 0, 0
win_score = 5

text = pygame.font.SysFont("Arial MT", FONT_SIZE, bold=False)
restart_text = text.render("Press R to restart", True, PLAYER_COLOR)
win_text2 = text.render("Player 2 (left) Won!", True, PLAYER_COLOR)
win_text1 = text.render("Player 1 (left) Won!", True, PLAYER_COLOR)


running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if score_1 == win_score: 
        screen.fill("black")
        screen.blit(win_text1, (0,0))
        screen.blit(restart_text, (0,win_text1.get_height()))
        pygame.display.flip()
        input()
        running = False
    if score_2 == win_score:
        screen.fill("black")
        screen.blit(win_text2, (0,0))
        screen.blit(restart_text, (0,win_text2.get_height()))
        pygame.display.flip()
        running = False

    if keys[pygame.K_w]:
        if player1_pos.y > 0:
            player1_pos.y -= 200 * dt
    if keys[pygame.K_s]:
        if player1_pos.y < HEIGHT-PLAYER_SIZE[1]:
            player1_pos.y += 200 * dt
    if keys[pygame.K_UP]:
        if player2_pos.y > 0:
            player2_pos.y -= 200 * dt
    if keys[pygame.K_DOWN]:
        if player2_pos.y < HEIGHT-PLAYER_SIZE[1]:
            player2_pos.y += 200 * dt

    #ball logic
    if pygame.Rect(player2_pos, PLAYER_SIZE).colliderect(pygame.Rect(ball_pos, BALL_SIZE)):
        BALL_VELOCITY = -BALL_VELOCITY
    if pygame.Rect(player1_pos, PLAYER_SIZE).colliderect(pygame.Rect(ball_pos, BALL_SIZE)):
        BALL_VELOCITY = -BALL_VELOCITY
    if ball_pos.x < 0:
        score_2 += 1
        ball_pos = pygame.Vector2(WIDTH/2-BALL_SIZE[0], HEIGHT/2-BALL_SIZE[0])
    if ball_pos.x > WIDTH:
        score_1 += 1
        ball_pos = pygame.Vector2(WIDTH/2-BALL_SIZE[0], HEIGHT/2-BALL_SIZE[0])

    ball_pos.x += BALL_VELOCITY 

    screen.fill("black")
    pygame.draw.rect(screen, PLAYER_COLOR, pygame.Rect(player1_pos, PLAYER_SIZE))
    pygame.draw.rect(screen, PLAYER_COLOR, pygame.Rect(player2_pos, PLAYER_SIZE))
    pygame.draw.rect(screen, PLAYER_COLOR, pygame.Rect(ball_pos, BALL_SIZE))
    
    score1_text = text.render(str(score_1), True, PLAYER_COLOR)
    score2_text = text.render(str(score_2), True, PLAYER_COLOR)

    screen.blit(score1_text, (WIDTH/2-(score1_text.get_width())-BALL_SIZE[0], BALL_SIZE[0]*2))
    screen.blit(score2_text, ((WIDTH/2)+BALL_SIZE[0], BALL_SIZE[0]*2))
 
    pygame.draw.line(screen, PLAYER_COLOR, (WIDTH/2,0), (WIDTH/2, HEIGHT), width=2)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
