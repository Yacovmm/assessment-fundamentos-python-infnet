"""
Usando a biblioteca Pygame,
escreva um programa que desenha 1 quadrado amarelo de tamanho 50 na tela em posição aleatória.
"""
import pygame
import random

pygame.init()
pygame.display.set_caption("--Assessment questão 7 YacovR.--")
size = width, heitgh = 800, 600

screen = pygame.display.set_mode(size)

green = (34, 139, 34)

clock = pygame.time.Clock()

# random.randint(20, 255), random.randint(20, 255), random.randint(20, 255)
class Quadradinho():
    def __init__(self):
        self.width = 50
        self.heitgh = 50
        self.x = random.randint(0, width - self.width)
        self.y = random.randint(0, heitgh - self.heitgh)
        self.color = (255, 255, 0)
        self.area = pygame.Rect(self.x, self.y, self.width, self.heitgh)

    def draw(self, tela):
        pygame.draw.rect(tela, self.color, self.area)


q = Quadradinho()
q.draw(screen)


def main():
    done = True

    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False

        clock.tick(60)
        pygame.display.update()

    pygame.quit()


main()
