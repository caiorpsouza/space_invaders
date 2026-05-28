from PPlay import sprite
import config


class Nave:
    def __init__(self, imagem):
        self.sprite = sprite.Sprite(imagem)
        self.speed = 250
        self.margem = config.janela.largura / 20

        self.x = config.janela.largura / 2 - self.sprite.width / 2
        self.y = (config.janela.altura * 19/20) - self.sprite.height

        self.sprite.set_position(self.x, self.y)
    
    def vai_pra_esquerda(self):
        if self.x >= self.margem:
            self.x -= self.speed * config.janela.delta_time()
    
    def vai_pra_direita(self):
        if self.x + self.sprite.width <= config.janela.largura - self.margem:
            self.x += self.speed * config.janela.delta_time()

    def verificar_inputs(self):
        if (config.janela.keyboard.key_pressed('LEFT') or config.janela.keyboard.key_pressed("A")):
            self.vai_pra_esquerda()
        if (config.janela.keyboard.key_pressed('RIGHT') or config.janela.keyboard.key_pressed("D")):
            self.vai_pra_direita()

    def get_position(self):
        return (self.x, self.y)

    def loop(self):
        self.verificar_inputs()
        self.sprite.set_position(self.x, self.y)
    
    def draw(self, em_combate):
        if em_combate:
            self.sprite.draw()
    
    def collided(self, outro_sprite):
        return self.sprite.collided(outro_sprite)