from PPlay import *
import config

facil_btn = sprite.Sprite("images/facil.png")
medio_btn = sprite.Sprite("images/medio.png")
dificil_btn = sprite.Sprite("images/dificil.png")
background = sprite.Sprite("images/diff-background.png")
background.set_position(0, -(background.height/4))


def play() :
    while True:
        background.draw()



        facil_btn.set_position(config.janela.largura/2-facil_btn.width/2, medio_btn.y - medio_btn.height - 50)
        medio_btn.set_position(config.janela.largura/2-medio_btn.width/2, config.janela.altura/2 - medio_btn.height/2)
        dificil_btn.set_position(config.janela.largura/2-dificil_btn.width/2, medio_btn.y + medio_btn.height + 50)
        
        #Clique nos botões
        if (config.janela.mouse.button_down(1) and config.janela.mouse.is_over_object(facil_btn)):
            config.dificuldade = 1

        if (config.janela.mouse.button_down(1) and config.janela.mouse.is_over_object(medio_btn)):
            config.dificuldade = 2

        if (config.janela.mouse.button_down(1) and config.janela.mouse.is_over_object(dificil_btn)):
            config.dificuldade = 3


        if (config.janela.keyboard.key_down('ESC')):
            config.Tela = 'Menu'
            return 0

        facil_btn.draw()
        medio_btn.draw()
        dificil_btn.draw()
        config.janela.update()
