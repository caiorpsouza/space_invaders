import config
from PPlay import *

from entities.DisplayVidas import Vidas
from entities.TirosMonstros import TirosMonstros
from entities.HordaMonstros import HordaMonstros
from entities.Nave import Nave
from entities.TirosNave import TirosNave

#Objeto da nave
nave = Nave("images/nave.png")
monstros = HordaMonstros()
tiros_nave = TirosNave()
tiros_monstros = TirosMonstros()
vidas = Vidas()
background = sprite.Sprite("images/jogar-background.jpg")
background.set_position(0, 0)


#Constantes dos Tiros
tiro = sprite.Sprite("images/tiro.png")
tiro_speed = 20
tiros = []
explosoes = []


def play():
    #Tempo de Jogo
    game_time = 0
    #Controle de FPS
    fps_controller = 0
    fps = 0
    contador_fps = 0
    
    #Variaveis invencivel
    invencivel = False
    invencivel_timer = 0
    invencivel_cooldown = 2

    #Variaveis de Montros
    monstros.spawnar_monstros(3, 7)

    while True:
        game_time += config.janela.delta_time()
        background.draw()

        #Loops dos montros
        monstros.loop(nave)
        #Loop da nave
        nave.loop()
        #Loop dos tiros
        tiros_nave.loop(nave, monstros.matriz)
        tiros_monstros.loop(monstros.matriz)

        #Checagem de invencivel
        if invencivel:
            invencivel_timer += config.janela.delta_time()

            if int(invencivel_timer * 10) % 3 == 0:
                nave.draw(monstros.em_combate)

            if invencivel_timer >= invencivel_cooldown:
                invencivel = False
                invencivel_timer = 0
        else:
            nave.draw(monstros.em_combate)
            if  tiros_monstros.tiro_acerto(nave.sprite):
                invencivel = True
                vidas.vidas -= 1
        
        #Escrever o FPS na tela
        contador_fps += 1
        fps_controller += config.janela.delta_time()
        if  fps_controller >= 1:
            fps_controller = 0
            fps = contador_fps
            contador_fps = 0
        config.janela.draw_text(f"FPS: {fps}", 20, 20, tamanho=20, cor=(255,255,255), fonte="Arial")
        
        if not monstros.em_combate:
            game_time = 0
            monstros.fora_de_combate()
            vidas.vidas = 0

        if game_time > 0 and game_time < 0.2:
            vidas.vidas = config.vidas_total
        #Desenha as vidas na tela
        vidas.loop()

        #Saída para o menu principal
        if (config.janela.keyboard.key_down('ESC')):
            config.Tela = 'Menu'
            return 0
        
        config.janela.update()