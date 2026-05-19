from PPlay import *
import config

jogar_btn = sprite.Sprite("images/jogar-btn.png")
diff_btn = sprite.Sprite("images/diff-btn.png")
rank_btn = sprite.Sprite("images/rank-btn.png")
sair_btn = sprite.Sprite("images/sair-btn.png")
background = sprite.Sprite("images/main-menu-background.jpg")
background.set_position(0, 0)


def play() :
    while True:
        background.draw()

        #Clique no botão Jogar
        if (config.janela.mouse.button_down(1) and config.janela.mouse.is_over_object(jogar_btn)):
            config.Tela = 'Jogar'
            return 0
        #Clique no botão Dificuldade
        if (config.janela.mouse.button_down(1) and config.janela.mouse.is_over_object(diff_btn)):
            config.Tela = 'Dificuldade'
            return 0
        #Clique no botão Sair
        if (config.janela.mouse.button_down(1) and config.janela.mouse.is_over_object(sair_btn)):
            config.is_running = False
            return 0
        



        jogar_btn.set_position(config.janela.largura/2-jogar_btn.width/2, 75)
        diff_btn.set_position(config.janela.largura/2-diff_btn.width/2, jogar_btn.y + jogar_btn.height + 50)
        rank_btn.set_position(config.janela.largura/2-rank_btn.width/2, diff_btn.y + diff_btn.height + 50)
        sair_btn.set_position(config.janela.largura/2-sair_btn.width/2, rank_btn.y + rank_btn.height + 50)

        sair_btn.draw()
        rank_btn.draw()
        diff_btn.draw()
        jogar_btn.draw()

        config.janela.update()
