"""
Usando a biblioteca Pygame, escreva um programa que desenha 1 botão (retângulo) com o texto “clique”
sobre ele na parte superior da tela.
 Quando o botão for clicado, ele deve desenhar um retângulo em posição aleatória na tela.
"""
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

font = pygame.font.Font(None, 50)
text = font.render('Clique', False, (0, 0, 0))

clock = pygame.time.Clock()


# self.x = random.randint(0, width - self.width)
# self.y = random.randint(0, heitgh - self.heitgh)

class Quadradinho():
    def __init__(self, x, y):
        self.width = 300
        self.heitgh = 75
        self.x = x
        self.y = y
        self.color = (random.randint(20, 255), random.randint(20, 255), random.randint(20, 255))
        self.area = pygame.Rect(self.x, self.y, self.width, self.heitgh)

    def draw(self, tela):
        pygame.draw.rect(tela, self.color, self.area)


q = Quadradinho(width / 2 - 150, 100)
q.draw(screen)
screen.blit(text, (width / 2 - 75, 100))

a = Quadradinho(random.randint(0, width - 100), random.randint(0, heitgh - 50))


def main():
    done = True

    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()
                if q.area.collidepoint(x):
                    a.draw(screen)

        clock.tick(60)
        pygame.display.update()

    pygame.quit()


main()
