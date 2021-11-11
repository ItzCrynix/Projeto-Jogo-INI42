import pygame
import random
import math

largura = 1000
altura = 500
qtdcolunas = random.randint(5, 10)
qtdlinhas = random.randint(3, 5)

class Retangulo():
    def __init__(self, x, y, larg, alt, tela):
        self.x = x
        self.y = y
        self.width = larg
        self.height = alt
        self.__tela = tela
        self.obj = None
        self.cor = (int(random.random() * 255), int(random.random() * 255), int(random.random() * 255))

    def show(self):
        self.obj = pygame.draw.rect(self.__tela, self.cor, (self.x, self.y, self.width, self.height))


class Jogador():
    def __init__(self, x, y, larg, alt, tela):
        self.x = x
        self.y = y
        self.width = larg
        self.height = alt
        self.speed = 2
        self.tela = tela
        self.state = 'idle'
        self.obj = None

    def __str__(self) -> str:
        return f'(x: {self.x}, y: {self.y}, state: {self.state})'

    def __mexer(self):
        if self.state == 'idle':
            pass
        elif self.state == 'right':
            self.x += self.speed
        elif self.state == 'left':
            self.x -= self.speed

        if self.x < 0:
            self.x += self.speed
        elif self.x + self.width > largura:
            self.x -= self.speed

    def show(self):
        self.__mexer()
        self.obj = pygame.draw.rect(self.tela, (255, 255, 255), (self.x, self.y, self.width, self.height))


class Bola():
    def __init__(self, tela, x, y, raio, cor=(255, 255, 255)):
        self.x = x
        self.y = y
        self.raio = raio
        self.tela = tela
        self.xspeed = meurandom()
        self.yspeed = 0.7
        self.cor = cor
        self.obj = None

    def __mexer(self):
        self.x += self.xspeed
        self.y += self.yspeed

        if self.x > largura - self.raio:
            self.x = largura - self.raio
            self.mudax()
        elif self.x < self.raio:
            self.x = self.raio
            self.mudax()
        if self.y > altura - self.raio or self.y < 0 + self.raio:
            self.muday()
    
    def muday(self):
        self.yspeed = -self.yspeed
    def mudax(self):
        self.xspeed = -self.xspeed

    def show(self) -> None:
        self.__mexer()
        self.obj = pygame.draw.circle(self.tela, self.cor, (self.x, self.y), self.raio)

def meurandom() -> float:
    return random.random() * 0.7 + 0.3
