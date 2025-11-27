import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Science Fair by Samuel 5G")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

PADDLE_W, PADDLE_H = 15, 100
BALL_SIZE = 15
PADDLE_SPEED = 6
BALL_X_SPEED = 5
BALL_Y_SPEED = 4

left = pygame.Rect(30, HEIGHT//2 - PADDLE_H//2, PADDLE_W, PADDLE_H)
right = pygame.Rect(WIDTH-45, HEIGHT//2 - PADDLE_H//2, PADDLE_W, PADDLE_H)
ball = pygame.Rect(WIDTH//2, HEIGHT//2, BALL_SIZE, BALL_SIZE)

clock = pygame.time.Clock()

ball_dx = BALL_X_SPEED
ball_dy = BALL_Y_SPEED

# Movement states
left_dir = 0     # -1 = up, 1 = down
right_dir = 0    # -1 = up, 1 = down


def move_paddles():
    # Left paddle
    if left_dir == -1 and left.top > 0:
        left.y -= PADDLE_SPEED
    if left_dir == 1 and left.bottom < HEIGHT:
        left.y += PADDLE_SPEED

    # Right paddle
    if right_dir == -1 and right.top > 0:
        right.y -= PADDLE_SPEED
    if right_dir == 1 and right.bottom < HEIGHT:
        right.y += PADDLE_SPEED


def move_ball():
    global ball_dx, ball_dy

    ball.x += ball_dx
    ball.y += ball_dy

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1

    if ball.colliderect(left) or ball.colliderect(right):
        ball_dx *= -1

    if ball.left <= 0 or ball.right >= WIDTH:
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_dx *= -1


def draw():
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, RED, left)
    pygame.draw.rect(WIN, BLUE, right)
    pygame.draw.ellipse(WIN, WHITE, ball)
    pygame.draw.aaline(WIN, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))
    pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            # LEFT PADDLE TOGGLE
            if event.key == pygame.K_w:
                left_dir = -1
            if event.key == pygame.K_s:
                left_dir = 1

            # LEFT STOP KEYS , .
            if event.key == pygame.K_COMMA:      # ,
                if left_dir == -1:
                    left_dir = 0
            if event.key == pygame.K_PERIOD:     # .
                if left_dir == 1:
                    left_dir = 0

            # RIGHT PADDLE TOGGLE
            if event.key == pygame.K_UP:
                right_dir = -1
            if event.key == pygame.K_DOWN:
                right_dir = 1

            # RIGHT STOP KEYS ; '
            if event.key == pygame.K_SEMICOLON:  # ;
                if right_dir == -1:
                    right_dir = 0
            if event.key == pygame.K_QUOTE:      # '
                if right_dir == 1:
                    right_dir = 0

    move_paddles()
    move_ball()
    draw()
    clock.tick(60)
