import pygame;
from pygame.locals import *;

from sys import exit;

pygame.init();

largura=640;
altura=480;

tela=pygame.display.set_mode((largura, altura));

while True:

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit();
            exit();

    #bandeira da frança
    # pygame.draw.rect(tela, (0, 35, 149), (0, 0, 213, 480))
    # pygame.draw.rect(tela, (255, 255, 255), (213, 0, 213, 480))
    # pygame.draw.rect(tela, (237, 41, 57), (426, 0, 213, 480))

    #bandeira japão:
    tela.fill((255, 255, 255))
    pygame.draw.circle(tela, (255, 0, 0), (320, 240), 150)

    pygame.display.update();