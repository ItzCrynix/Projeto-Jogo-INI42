import pygame
from pygame.locals import *
from sys import exit
import random
from Objetos import *

# -------------- parte principal ---------------- #
def init():
    def main():
        fundo = (0,0,0)
        while True:
            tela.fill(fundo)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                elif event.type == KEYDOWN:
                    keys = pygame.key.get_pressed()

                    # Muda o estado do jogador baseado na tecla pressionada
                    if keys[K_RIGHT]:
                        player.state = 'right'
                    elif keys[K_LEFT]:
                        player.state = 'left'
                elif event.type == KEYUP:
                    # Volta para o estado parado quando a tecla não estiver mais pressionada
                    player.state = 'idle'

            player.show()
            for linha in blocos:
                for bloco in linha:
                    bloco.show()
            pygame.display.update()


    pygame.init()
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Jogo dos tijolos')

    # Cria a linha de blocos para serem destruidos >:)
    blocos = []
    for linha in range(qtdlinhas):
        col = []
        for coluna in range(qtdcolunas):
            larg = largura / qtdcolunas
            alt = (altura * 0.4) / qtdlinhas
            col.append(Retangulo(larg * coluna, alt * linha, larg, alt, tela))
        blocos.append(col)

    # Jogador
    player = Jogador(largura / 2 - 150, altura - 20, 300, 10, tela)

    main()


if __name__ == '__main__':
    init()
