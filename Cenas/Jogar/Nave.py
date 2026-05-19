import config

nave_speed = 250

def nave_loop(nave):
        #Movimentação da nave
        if ((config.janela.keyboard.key_pressed('LEFT')or config.janela.keyboard.key_pressed("A")) and (nave.x >= config.janela.largura/20)):
            nave.x -= nave_speed * config.janela.delta_time()
        if ((config.janela.keyboard.key_pressed('RIGHT')or config.janela.keyboard.key_pressed("D")) and (nave.x + nave.width <= config.janela.largura * 19/20)):
            nave.x += nave_speed * config.janela.delta_time()

        nave.draw()