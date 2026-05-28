import random

from PPlay import sprite
import config


class TirosMonstros:
    def __init__(self):
        self.tiros = []
        self.tiro_speed = 200
        self.tiro_cooldown_timer = 0
        self.tiro_cooldown = 0.5
    

    def tiro_acerto(self, nave):
        for tiro in self.tiros:
            if tiro.y + tiro.height >= nave.y:
                    if tiro.collided(nave):
                        self.tiros.remove(tiro)
                        return True
        return False
    
    def loop(self, monstros):
        self.tiro_cooldown_timer += config.janela.delta_time()

        if self.tiro_cooldown_timer >= self.tiro_cooldown:
            self.tiro_cooldown_timer = 0
            if monstros:
                x = random.randint(0, len(monstros)-1)
                y = random.randint(0, len(monstros[x])-1)
                monstro_atirador = monstros[x][y]
                novo_tiro = sprite.Sprite('images/tiro_monstro.png')
                novo_tiro.set_position(monstro_atirador.x + monstro_atirador.width/2, monstro_atirador.y + monstro_atirador.height)
                self.tiros.append(novo_tiro)
            
        for tiro in self.tiros:   
            if tiro.y > config.janela.altura:
                self.tiros.remove(tiro)
            else:
                tiro.y += self.tiro_speed * config.janela.delta_time()
                tiro.draw()
