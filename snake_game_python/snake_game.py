import pygame
import time
import random

# initialising pygame
pygame.init()

snake_speed = 10.0

# window size
window_x = 1280
window_y = 720

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(245, 76, 53)
green = pygame.Color(129, 226, 122)
blue = pygame.Color(0, 0, 255)
lilac = pygame.Color(158, 156, 230)

# initialising game window
pygame.display.set_caption('Python Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS controller
fps = pygame.time.Clock()

# default snake position
snake_position = [100, 50]

# first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

# setting default snake direction to right
direction = 'RIGHT'
change_to = direction

# initial score
score = 0


# displaying Score function
def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    speed_surface = score_font.render('Speed : ' + str(round(snake_speed, 1)), True, color)

    # create rectangular object for
    # text surface object
    score_rect = score_surface.get_rect()
    speed_rect = speed_surface.get_rect(topleft=(window_x-130, 0))

    # displaying text
    game_window.blit(score_surface, score_rect)
    game_window.blit(speed_surface, speed_rect)


# game over function
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)

    # creating text surface for text
    game_over_surface = my_font.render('Your score is : ' + str(score), True, red)

    # creating rectangular object for
    # text surface
    game_over_rect = game_over_surface.get_rect()

    # text position
    game_over_rect.midtop = (window_x/2, window_y/4)

    # draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # defining delay
    time.sleep(2)

    # deactivate pygame
    pygame.quit()

    # quit the game
    quit()


# main function
while True:

    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            elif event.key == pygame.K_ESCAPE:
                game_over()

    # if two keys pressed simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    elif direction == 'DOWN':
        snake_position[1] += 10
    elif direction == 'LEFT':
        snake_position[0] -= 10
    elif direction == 'RIGHT':
        snake_position[0] += 10

    # snake body growing mechanism
    # when fruits and snake collide
    # score incremented by 1
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 1
        snake_speed += 0.1
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]

    fruit_spawn = True

    # background color
    game_window.fill(lilac)

    # drawing snake
    for pos in snake_body:
        pygame.draw.circle(game_window, green, pos, 7)

    # drawing apples
    pygame.draw.circle(game_window, red, fruit_position, 7)

    # game over conditions
    # don't collide with borders
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
    # don't bite yourself
    if snake_body[0] in snake_body[1:]:
        game_over()

    # displaying score
    show_score(white, 'times new roman', 20)

    # refresh game screen
    pygame.display.update()

    # FPS / refresh rate
    fps.tick(snake_speed)
