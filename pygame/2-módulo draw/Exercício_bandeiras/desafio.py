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

    pygame.draw.polygon(tela, (255, 255, 0), ((150, 350), (225, 250), (300,350)))
    pygame.draw.polygon(tela, (255, 255, 0), ((301, 350), (376, 250), (451,350)))
    pygame.draw.polygon(tela, (255, 255, 0), ((225,250), (300,150), (376,250)))

    pygame.display.update();