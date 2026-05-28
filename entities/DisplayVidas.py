from PPlay import sprite
import config


class Vidas:
    def __init__(self):
        self.vidas = config.vidas_total
        self.vida_sprite = sprite.Sprite("images/vida.png")

    def loop(self):
        for i in range(self.vidas):
            nova_vida = self.vida_sprite
            nova_vida.set_position(config.janela.largura - (i * (self.vida_sprite.width + 20)) - self.vida_sprite.width - 30, 30)
            nova_vida.draw()