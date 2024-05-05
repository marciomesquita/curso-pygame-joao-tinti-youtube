import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

#volume varia de 0 a 1
pygame.mixer.music.set_volume(0.2)
musica_ambiente = pygame.mixer.music.load('assets/BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)

som_colisao = pygame.mixer.Sound('assets/smw_coin.wav')
som_colisao.set_volume(1)

largura = 640
altura = 480
x = int(largura / 2)
y = int(altura / 2)

x_azul = randint(40, 600)
y_azul = randint(50, 430)

pontos = 0
# vc pode ver as fonte disponíveis usando pygame.font.get_fonts()
fonte = pygame.font.SysFont('arial', 40, bold = True, italic = True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo")
relogio = pygame.time.Clock()

while True:
    relogio.tick(10)
    tela.fill((0,0,0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, False, (255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
           
    if pygame.key.get_pressed()[K_a]:
        x -= 20
    if pygame.key.get_pressed()[K_d]:
        x += 20
    if pygame.key.get_pressed()[K_w]:
        y -= 20
    if pygame.key.get_pressed()[K_s]:
        y += 20

    retangulo_vermelho = pygame.draw.rect(tela, (255,0,0), (x,y,40,50))
    retangulo_azul = pygame.draw.rect(tela, (0,0,255), (x_azul,y_azul,40,50))

    if retangulo_vermelho.colliderect(retangulo_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos += 1
        som_colisao.play()
    
    tela.blit(texto_formatado, (450,40))

    pygame.display.update()