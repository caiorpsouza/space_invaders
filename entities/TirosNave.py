from PPlay import sprite
import config


class TirosNave:
    def __init__(self):
        self.tiros = []
        self.tiro_speed = 250
        self.cooldown_timer = 0
        self.cooldown = 0.5 * config.dificuldade
        self.explosoes = []
        self.explosao_duracao = 0.4 


    def atualizar_explosoes(self):
        for explosao in self.explosoes:
            explosao['tempo'] -= config.janela.delta_time()
            
            explosao['sprite'].update()
            explosao['sprite'].draw()
            
            if explosao['tempo'] <= 0:
                self.explosoes.remove(explosao)

    def abate_monstros(self, monstros):
        if monstros:
            ultimo_monstro = monstros[-1][-1]
            for tiro in self.tiros:
                if tiro.y > ultimo_monstro.y+ultimo_monstro.height:
                    break
                else:
                    for linha in monstros:
                        for monstro in linha:
                            if tiro.collided(monstro):
                                explosao_sprite = sprite.Sprite("images/explosion2.png", 4)
                                explosao_sprite.set_total_duration(400)
                                
                                explosao_sprite.set_position(
                                    monstro.x + monstro.width / 2 - explosao_sprite.width / 2,
                                    monstro.y + monstro.height / 2 - explosao_sprite.height / 2
                                )
                                
                                self.explosoes.append({
                                    'sprite': explosao_sprite,
                                    'tempo': self.explosao_duracao
                                })
                                
                                # Remove tiro e monstro
                                self.tiros.remove(tiro)
                                linha.remove(monstro)
                                
                                return 

    def loop(self, nave, monstros):
        self.cooldown_timer += config.janela.delta_time()
        if (config.janela.keyboard.key_pressed('SPACE')) and (self.cooldown_timer >= self.cooldown):
            self.cooldown_timer = 0
            novo_tiro = sprite.Sprite('images/tiro.png')
            novo_tiro.set_position(nave.x + nave.sprite.width/2 - novo_tiro.width/2, nave.y)
            self.tiros.append(novo_tiro)
        
        for tiro in self.tiros:
            if tiro.y < 0:
                self.tiros.remove(tiro)
            else:
                tiro.y -= self.tiro_speed * config.janela.delta_time()
                tiro.draw()

        self.abate_monstros(monstros)
        self.atualizar_explosoes()