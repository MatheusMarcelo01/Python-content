
import pygame, random
from pygame.locals  import *


#alinhar cobra e comida - todas casas serão multiplas de 10 e ficarão alinhadas
def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 *10)

#colisões
def collision(c1, c2):
    return (c1[0] == c2[0] and (c1[1] == c2[1]))

#direcoes
up = 0
right  = 1
down = 2
left = 3


#A cobra
snake = [(200,200), (210,200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255)) #cor da cobra

#a comida da cobra
apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0)) #cor da comida

#limitar FPS do jogo, pra não ficar muito rápido
clock = pygame.time.Clock()



my_direction = left

#Criando uma janela vazia preta, e loop principal do jogo
pygame.init()
screen = pygame.display.set_mode ((600,600))
pygame.display.set_caption('Snake')


while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        #controlar a cobrinha
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = up
            if event.key == K_DOWN:
                my_direction = down
            if event.key == K_LEFT:
                my_direction = left
            if event.key == K_RIGHT:
                my_direction = right

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0)) #crescer a cobrinha

    #corpo da cobra indo atras do próprio corpo
    for i in range(len(snake)-1,0, -1):
        snake[i]= (snake[i-1][0], snake[i-1][1])

    #movimentação
    if my_direction == up:
        snake[0] = (snake[0][0], snake[0][1] -10) 
    if my_direction == down:
        snake[0] = (snake[0][0], snake[0][1] +10) 
    if my_direction == left:
        snake[0] = (snake[0][0] -10, snake[0][1])
    if my_direction == right:
        snake[0] = (snake[0][0] +10, snake[0][1]) 

    

    #fim da movimentação
    
    screen.fill((0,0,0)) #limpar a tela
    screen.blit(apple, apple_pos)

    for pos in snake: 
        screen.blit(snake_skin,pos)

    pygame.display.update()

