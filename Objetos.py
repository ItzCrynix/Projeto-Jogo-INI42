import pygame
import random
import math

largura = 1000
altura = 500
qtdcolunas = 10
qtdlinhas = 4

class Retangulo():
    def __init__(self, x, y, larg, alt, tela):
        self.x = x
        self.y = y
        self.width = larg
        self.height = alt
        self.tela = tela
        self.obj = None
        self.cor = (int(random.random() * 255), int(random.random() * 255), int(random.random() * 255))

    def show(self):
        self.obj = pygame.draw.rect(self.tela, self.cor, (self.x, self.y, self.width, self.height))


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

    def mexer(self):
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
        self.mexer()
        self.obj = pygame.draw.rect(self.tela, (255, 255, 255), (self.x, self.y, self.width, self.height))


class Bola():
    def __init__(self, tela, x, y, raio, cor=(255, 255, 255)):
        self.x = x
        self.y = y
        self.raio = raio
        self.tela = tela
        self.xspeed = random.random() * 0.7 + 0.3
        self.yspeed = 0.5
        self.cor = cor
        self.obj = None

    def mexer(self):
        self.x += self.xspeed
        self.y += self.yspeed

        if self.x > largura - self.raio or self.x < 0 + self.raio:
            self.xspeed = -self.xspeed
        if self.y > altura - self.raio or self.y < 0 + self.raio:
            self.yspeed = -self.yspeed
    
    def mudadirecao(self):
        self.yspeed = -self.yspeed

    def show(self):
        self.mexer()
        self.obj = pygame.draw.circle(self.tela, self.cor, (self.x, self.y), self.raio)
