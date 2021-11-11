import pygame
from pygame.locals import *
from sys import exit
import random
from Objetos import *

# -------------- parte principal ---------------- #
def init():
    # ------------ funções que repetem ------------ #
    def __redefine_blocos():
        """
        Basicamente, redefine a matriz de blocos do jogo
        """
        for linha in range(qtdlinhas):
            col = []
            for coluna in range(qtdcolunas):
                larg = largura / qtdcolunas
                alt = (altura * 0.4) / qtdlinhas
                col.append(Retangulo(larg * coluna, alt * linha, larg, alt, tela))
            blocos.append(col)

    # ------------------- códido do menu ---------------- #
    def __menu():
        fonte = pygame.font.SysFont('Arial', 30)

        lb1 = fonte.render('Bem vindo ao nosso jogo!', False, (255, 255, 255), (0, 0, 0))
        poslb1 = (largura / 2 - lb1.get_width() / 2, altura / 3  - lb1.get_height() /2)

        lbJogar = fonte.render('Jogar', False, (0, 0, 255), (0, 0, 0))
        posJogar = (largura / 2 - lbJogar.get_width() / 2, altura / 2 - lbJogar.get_height() /2)

        lbSair = fonte.render('Sair', False, (0, 0, 255), (0, 0, 0))

        while True:
            tela.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                
                if event.type == MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pressed()
                    # Caso seja o botão esquerdo que tenha sido apertado
                    if mouse[0]:
                        pos = pygame.mouse.get_pos()
                        # se estiver na mesma posição do "Botão" Jogar
                        if pos[1] > altura / 2 - lb1.get_height() / 2 and pos[1] < altura / 2 + lbJogar.get_height():
                            __main()
                            break

            tela.blit(lb1, poslb1)
            tela.blit(lbJogar, posJogar)
            pygame.display.update()


    # ------------------- código do jogo ---------------- #
    def __main():
        while True:
            tela.fill((0, 0, 0))

            # ------------- eventos ------------- #
            for event in pygame.event.get():
                # Evento de saida
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                
                # Evento de tecla apertada
                elif event.type == KEYDOWN:
                    keys = pygame.key.get_pressed()

                    # Muda o estado do jogador baseado na tecla pressionada
                    if keys[K_RIGHT] or keys[K_d]:
                        player.state = 'right'
                    if keys[K_LEFT] or keys[K_a]:
                        player.state = 'left'

                    if keys[K_r]: # Reinicia os blocos se a tecla for 'R'
                        __redefine_blocos()
                
                # Evento de tecla "soltada"
                elif event.type == KEYUP:
                    # Volta para o estado parado quando a tecla não estiver mais pressionada
                    player.state = 'idle'

            player.show()
            bola.show()
            # Colisão bola com player
            if bola.obj.colliderect(player.obj):
                # Inverte a velocidade do y, para ele ir na direção contraria ao player
                bola.muday()

                # Verifica em que metade do player a bola está, mudando sua direção baseado nisso
                if bola.x >= player.x and bola.x < player.x + player.width / 2:
                    bola.xspeed = - (meurandom())
                elif bola.x > player.x + player.width / 2 and bola.x < player.x + player.width:
                    bola.xspeed = meurandom()

            # Iteração entre todos os blocos para mostra-los na tela    
            for linha in blocos:
                for bloco in linha:
                    bloco.show()

                    # Verifica se a bola colidiu com o bloco
                    if bola.obj.colliderect(bloco.obj):
                        # Aqui ele analisa em que posição a bola colidiu com o bloco (do lado, em baixo ou em cima)
                        if bola.y > bloco.y + bloco.height:
                            bola.muday()
                        elif bola.y <= bloco.y + bloco.height and bola.y >= bloco.y:
                            bola.mudax()
                        elif bola.y < bloco.y:
                            bola.muday()
                        linha.remove(bloco) # Remove o bloco acertado da linha

            # Mostra tudo que atualizou na tela
            pygame.display.update()

            # Aqui ele basicamente conta quantos blocos ainda falta, se não sobrar nenhum ele para
            cont = 0
            for num in range(len(blocos)):
                # Ele ve se a linha ta zerada, incrementando se sim
                if len(blocos[num]) == 0:
                    cont += 1
            # Se o numero de linhas zeradas for igual a length da matriz, ele para
            if cont == len(blocos):
                break


    # --------------- Parte de Inicialização ---------------- #
    pygame.init()
    pygame.mixer.music.load(r'ngcdaddy.mp3')
    pygame.mixer.music.play(-1)

    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Jogo dos tijolos')

    # Cria a linha de blocos para serem destruidos >:)
    blocos = []
    __redefine_blocos()

    # Jogador
    player = Jogador(largura / 2 - (largura * 0.3 / 2), altura - 20, largura * 0.3, 10, tela)
    bola = Bola(tela, largura / 2, altura / 2, 10)

    __menu()


if __name__ == '__main__':
    init()
