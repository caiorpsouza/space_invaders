import random

from PPlay import sprite
import config


class HordaMonstros:
    def __init__(self):
        self.monstro_velocidade = 700
        self.matriz = []
        self.inverte = False
        self.em_combate = True
        self.try_again = sprite.Sprite("images/try_again.png")
        self.try_again.set_position(config.janela.largura/2 - self.try_again.width/2, config.janela.altura* 3/4 - self.try_again.height/2)
        

    def spawnar_monstros(self, c, l):
        self.matriz = []
        self.em_combate = True
        for i in range(c):
            linha_atual = []
            for j in range(l):
                m = sprite.Sprite('images/monstro_spritesheet.png' ,4)
                m.set_total_duration(800)

                m.set_position(j * (m.width/2 + m.width + 20)+50, i * (m.height/2 + m.height + 10)+30)
                linha_atual.append(m)
            self.matriz.append(linha_atual)
    
    def deleta_monstros(self):
        if not self.em_combate:
            self.matriz = False
            self.inverte = False
    
    def desce_monstros(self, lado):
        for linha in self.matriz:
            for monstro in linha:
                monstro.y += monstro.height/2
                if lado == 'right':
                    monstro.x += self.monstro_velocidade * config.janela.delta_time() * -1
                if lado == 'left':
                    monstro.x += self.monstro_velocidade * config.janela.delta_time()

    def combate_check(self, nave):
        if self.matriz:
            for linha in self.matriz:
                for monstro in linha:
                    if monstro.y + monstro.height >= nave.y:
                        self.em_combate = False
                    else:
                        self.em_combate = True
    
    def loop(self, nave):
        if self.matriz:
            if self.matriz == []:
                self.matriz = False
                return
            else:
                for linha in self.matriz:
                    if linha == []:
                        self.matriz.remove(linha)
                    else:
                        for monstro in linha:
                            #Inversão do movimento de cada monstro
                            if monstro.x + monstro.width >= config.janela.largura*39/40:
                                self.inverte = True
                                self.desce_monstros('right')
                            if monstro.x <= config.janela.largura/40:
                                self.inverte = False
                                self.desce_monstros('left')
                            #Movimentação de cada monstro
                            if self.inverte:
                                monstro.x += self.monstro_velocidade * config.janela.delta_time() * -1
                            else:
                                monstro.x += self.monstro_velocidade * config.janela.delta_time()
                            
                            monstro.update()
                            monstro.draw()
            self.deleta_monstros()
            self.combate_check(nave)

    def fora_de_combate(self):
        if (config.janela.keyboard.key_down('SPACE')):
                self.spawnar_monstros(3, 7)
        self.try_again.draw()