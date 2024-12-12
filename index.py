import pygame
import random

pygame.init()

#tupla
largura, altura = 800,600
tela = pygame.display.set_mode((largura, altura))

black = (0, 0, 0)

# Tiros
tiros =[]
velocidade_tiro = 5

# jogador
jogador_altura = 30
jogador_largura = 30
jogador_x = 400
jogador_y = 500
jogador_cor = (255, 255, 122)
velocidade_jogador = 1

# inimigo
inimigo_altura = 50
inimigo_largura = 30
inimigos = []
num_inimigos = 3 
inimigo_cor = (122, 155, 122)
velocidade_inimigo = 0.5


executando = True


while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    #Movimentos Jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jogador_x > 0:
        jogador_x = jogador_x - velocidade_jogador
    if teclas[pygame.K_RIGHT] and jogador_x < largura - jogador_largura:
        jogador_x = jogador_x + velocidade_jogador
    
    if teclas[pygame.K_SPACE]:
        tiros.append([jogador_x + jogador_largura // 2 - 2, jogador_y])


    # Atualização dos tiros
    for tiro in tiros[:]:
        tiro[1] -= velocidade_tiro
        if tiro[1] < 0:
            tiros.remove(tiro)
    pygame.draw.rect(tela, inimigo_cor, (inimigo_x,inimigo_y,inimigo_largura,inimigo_altura))   
    pygame.draw.rect(tela, jogador_cor, (jogador_x,jogador_y,jogador_largura,jogador_altura))
    
    for tiro in tiros:
        pygame.draw.rect(tela, (255, 0, 0),(tiro[0] , tiro[1], 4, 10) )
    pygame.display.flip()

    tela.fill(black)
pygame.quit()