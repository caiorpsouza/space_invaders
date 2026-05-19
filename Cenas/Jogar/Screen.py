from Cenas.Jogar.Monstros import inicializar_monstros, monsters_combat, monstros_loop
from Cenas.Jogar.Nave import nave_loop
from Cenas.Jogar.Tiros import abate_monstros, tiros_loop, atualizar_explosoes
import config
from PPlay import *
import time

#Constantes da Nave
nave = sprite.Sprite("images/nave.png")
nave.set_position((config.janela.largura / 2) - nave.width/2,config.janela.altura - config.janela.altura/20 - nave.height )
background = sprite.Sprite("images/jogar-background.jpg")
background.set_position(0, 0)


#Constantes dos Tiros
tiro = sprite.Sprite("images/tiro.png")
tiro_speed = 20
tiros = []
explosoes = []


def play():
    #Controle de FPS
    fps_controller = time.time()
    fps = 0
    contador_fps = 0

    #Variavel de Tiros
    tempo = 0
    
    #Variaveis de Montros
    em_combate = True
    inverte = False
    monstro_velocidade = 200
    matriz_de_monstros = inicializar_monstros(3,7)

    while True:
        background.draw()
        #Loops dos monstros
        em_combate = monsters_combat(matriz_de_monstros, nave, em_combate)
        if em_combate:
            inverte = monstros_loop(matriz_de_monstros, monstro_velocidade, inverte)
        else: 
            matriz_de_monstros = inicializar_monstros(3,7)
            config.janela.draw_text("Aperte espaço para continuar", config.janela.largura/3, config.janela.altura* 3/4, tamanho=30, cor=(0,0,0), fonte='Arial')
            if (config.janela.keyboard.key_down('SPACE')):
                em_combate = True


        #Loop da nave
        nave_loop(nave)

        #Loops dos tiros
        tempo = tiros_loop(nave, tiros, tempo)
        abate_monstros(matriz_de_monstros, tiros, explosoes)
        atualizar_explosoes(explosoes)

        
        #Escrever o FPS na tela
        contador_fps += 1
        if time.time() - fps_controller >= 1:
            fps_controller = time.time()
            fps = contador_fps
            contador_fps = 0
        config.janela.draw_text(f"FPS: {fps}", 20, 20, tamanho=20, cor=(255,255,255), fonte="Arial")


        #Saída para o menu principal
        if (config.janela.keyboard.key_down('ESC')):
            config.Tela = 'Menu'
            return 0
        

        config.janela.update()