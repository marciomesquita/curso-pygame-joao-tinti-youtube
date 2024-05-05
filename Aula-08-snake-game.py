import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

# https://freemusicarchive.org/music/BoxCat_Games/Nameless_the_Hackers_RPG_Soundtrack
# volume varia de 0 a 1
pygame.mixer.music.set_volume(0.2)
musica_ambiente = pygame.mixer.music.load('assets/BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)

# https://themushroomkingdom.net/media/smw/wav
som_colisao = pygame.mixer.Sound('assets/smw_coin.wav')
som_colisao.set_volume(1)

largura = 640
altura = 480

x_cobra = int(largura / 2)
y_cobra = int(altura / 2)

x_controle = 20
y_controle = 0

x_maca = randint(40, 600)
y_maca = randint(50, 430)

pontos = 0
# vc pode ver as fonte disponíveis usando pygame.font.get_fonts()
fonte = pygame.font.SysFont('arial', 40, bold = True, italic = True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo")
relogio = pygame.time.Clock()

lista_cobra = []
comprimento_limite_cobra = 5

def aumenta_cobra(lista_cobra):
    for X_Y in lista_cobra:
        #X_Y = [x, y]
        #X_Y[0] = x
        #X_Y[1] = y
        pygame.draw.rect(tela, (0,255,0), (X_Y[0], X_Y[1], 20, 20))

while True:
    relogio.tick(10)
    tela.fill((255,255,255))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, False, (0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
                 
    if pygame.key.get_pressed()[K_a]:
        x_cobra -= 20
    if pygame.key.get_pressed()[K_d]:
        x_cobra += 20
    if pygame.key.get_pressed()[K_w]:
        y_cobra -= 20
    if pygame.key.get_pressed()[K_s]:
        y_cobra += 20

    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra,y_cobra,20,20))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,20,20))

    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos += 1
        som_colisao.play()
        comprimento_limite_cobra += 1

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)

    aumenta_cobra(lista_cobra)
    
    tela.blit(texto_formatado, (450,40))

    pygame.display.update()