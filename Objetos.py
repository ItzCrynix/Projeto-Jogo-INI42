import pygame
import random
import math

largura = 1376
altura = 720
qtdcolunas = 20
qtdlinhas = 5

class Retangulo():
    def __init__(self, x, y, larg, alt, tela):
        self.x = x
        self.y = y
        self.width = larg
        self.height = alt
        self.tela = tela
        self.cor = (int(random.random() * 255), int(random.random() * 255), int(random.random() * 255))

    def mexer(self):
        self.x += 1

    def show(self):
        pygame.draw.rect(self.tela, self.cor, (self.x, self.y, self.width, self.height))


class Jogador():
    def __init__(self, x, y, larg, alt, tela):
        self.x = x
        self.y = y
        self.width = larg
        self.height = alt
        self.speed = 3
        self.tela = tela
        self.state = 'idle'

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
        pygame.draw.rect(self.tela, (255, 255, 255), (self.x, self.y, self.width, self.height))


class Bola():
    def __init__(self, x, y, raio, tela):
        self.x = x
        self.y = y
        self.raio = raio
        self.tela = tela
        self.xspeed = 2
        self.yspeed = 2

    def mexer(self):
        self.x += self.xspeed
        self.y += self.yspeed

        if self.x > largura - self.raio or self.x < 0 + self.raio:
            self.xspeed = -self.xspeed
        if self.y > altura - self.raio or self.y < 0 + self.raio:
            self.yspeed = -self.yspeed

    def show(self):
        self.mexer()
        pygame.draw.circle(self.tela, (0, 0, 0), (self.x, self.y), self.raio)

def colidiucirculo(obj1, obj2):
    varx = abs(obj1.x - obj2.x)
    vary = abs(obj1.y - obj2.y)
    distancia = math.sqrt(varx ** 2 + vary ** 2)

    return distancia <= obj1.raio + obj2.raio
