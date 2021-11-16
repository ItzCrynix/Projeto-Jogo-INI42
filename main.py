import pygame
from pygame.locals import *
from sys import exit
import random
from Objetos import *

# -------------- parte principal ---------------- #
def init():
    # ------------ funções que repetem ------------ #
    def __redefine_blocos(blocos: list, qtdcolunas: int, qtdlinhas: int) -> None:
        """
        Basicamente, redefine a matriz de blocos do jogo
        """
        for linha in range(qtdlinhas):
            col = []
            for coluna in range(qtdcolunas):
                larg = tela.get_width() / qtdcolunas
                alt = (tela.get_height() * 0.4) / qtdlinhas
                col.append(Retangulo(larg * coluna, alt * linha, larg, alt, tela))
            blocos.append(col)

    # ------------------- códido do menu ---------------- #
    def __menu():
        """
        Tela do menu do jogo
        """

        # ----------------- Textos e imagens para o menu ---------------- #
        # Posições feitas usando calculos para que fiquem em uma posição proporcional ao tamanho da tela
        # para que não tenha problemas de posicionamento na hora de mudar o tamanho da tela

        fonte = pygame.font.SysFont('Arial', 30)

        imgLogo = pygame.image.load(r'./src/imgLogo.png')
        poslb1 = (tela.get_width() / 2 - imgLogo.get_width() / 2, tela.get_height() / 3  - imgLogo.get_height() /2)

        lbJogar = fonte.render('Jogar', False, (0, 0, 255), (0, 0, 0))
        posJogar = (tela.get_width() / 2 - lbJogar.get_width() / 2, (tela.get_height() * 2) / 3 - lbJogar.get_height() /2)

        lbSair = fonte.render('Sair', False, (0, 0, 255), (0, 0, 0))
        posSair = (tela.get_width() / 2 - lbSair.get_width() / 2, (tela.get_height() * 3) / 4 - lbSair.get_height() / 2)

        imgsDificuldades = [pygame.image.load(r'./src/easy.png'), pygame.image.load(r'./src/normal.png'), pygame.image.load(r'./src/hard.png')]
        posImgs = lambda img: (tela.get_width() - img.get_width(), tela.get_height() - img.get_height())
        atual = 0

        while True:
            tela.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                elif event.type == KEYDOWN:
                    keys = pygame.key.get_pressed()

                    if keys[K_RIGHT]:
                        atual += 1
                        if atual == len(imgsDificuldades):
                            atual = 0
                    if keys[K_LEFT]:
                        atual -= 1
                        if atual < 0:
                            atual = len(imgsDificuldades) - 1

                elif event.type == MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pressed()
                    # Caso seja o botão esquerdo do mouse que tenha sido apertado
                    if mouse[0]:
                        pos = pygame.mouse.get_pos()
                        # se estiver na mesma posição do "Botão" Jogar
                        if pos[1] > posJogar[1] and pos[1] < posJogar[1] + lbJogar.get_height() and pos[0] > posJogar[0] and pos[0] < posJogar[0] + lbJogar.get_width():
                            __main(atual)
                            break

            tela.blit(imgLogo, poslb1)
            tela.blit(lbJogar, posJogar)
            tela.blit(lbSair, posSair)
            tela.blit(imgsDificuldades[atual], posImgs(imgsDificuldades[atual]))
            pygame.display.update()


    # ------------------- código do jogo ---------------- #
    def __main(dificuldade: int):
        """
        Parte principal deste programa.
        Essa é a tela que roda o jogo
        """
        min = 3
        max = 4
        qtdColunas = random.randint(dificuldade + min, dificuldade + max)
        qtdLinhas = random.randint(dificuldade + min, dificuldade + max)

        # Cria a linha de blocos para serem destruidos >:)
        blocos = []
        __redefine_blocos(blocos, qtdColunas, qtdLinhas)

        # Jogador
        player = Jogador(tela.get_width() / 2 - (tela.get_width() * 0.3 / 2), tela.get_height() - 20, tela.get_width() * 0.3, 10, tela)
        # Bola
        bola = Bola(tela, tela.get_width() / 2, tela.get_height() / 2, 10)
        clock = pygame.time.Clock()

        while True:
            clock.tick(360)
            # Background a partir de cor
            tela.fill((0, 0, 0))
            #Background a partir de imagem

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
            # Verifica se a bola passou do jogador, fazendo o jogo parar (porque ai você perdeu)
            if bola.y > player.y:
                bola = None
                break

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
                    bloco.show()

            # Mostra tudo que atualizou na tela
            pygame.display.update()

            # Aqui ele basicamente conta quantos blocos ainda falta, se não sobrar nenhum ele para
            cont = 0
            for num in range(len(blocos)):
                # Ele ve se a linha ta zerada, incrementando se sim
                if len(blocos[num]) == 0:
                    cont += 1
            # Se o numero de linhas zeradas for igual a length da matriz, ele para o loop do jogo
            if cont == len(blocos):
                break


    # --------------- Parte de Inicialização ---------------- #
    pygame.init()
    #pygame.mixer.music.load(r'./src/ngcdaddy.mp3')
    #pygame.mixer.music.play(-1)

    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Jogo dos tijolos')
    #icone = pygame.image.load(r'./src/icon.png')
    #pygame.display.set_icon(icone)

    __menu()


if __name__ == '__main__':
    init()
