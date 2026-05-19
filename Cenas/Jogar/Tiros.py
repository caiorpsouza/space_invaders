from PPlay import *
import config

Tiro = sprite.Sprite("images/tiro.png")
tiro_cooldown = 0.5 * config.dificuldade
tiro_speed = 250
explosao_duracao = 0.4  # 4 frames em 0.4 segundos = 0.1s por frame

def tiros_loop(nave, tiros, tempo):
    tempo += config.janela.delta_time()
    if (config.janela.keyboard.key_pressed('SPACE')) and (tempo >= tiro_cooldown):
        tempo = 0
        novo_tiro = sprite.Sprite('images/tiro.png')
        novo_tiro.set_position(nave.x + nave.width/2 - Tiro.width/2, nave.y)
        tiros.append(novo_tiro)
    
    for tiro in tiros[:]:
        if tiro.y < 0:
            tiros.remove(tiro)
        else:
            tiro.y -= tiro_speed * config.janela.delta_time()
            tiro.draw()

    return tempo

def atualizar_explosoes(explosoes):
    """Desenha, anima e atualiza as explosões, removendo as que expiraram"""
    for explosao in explosoes[:]:
        explosao['tempo'] -= config.janela.delta_time()
        
        # Atualiza a animação do sprite
        explosao['sprite'].update()
        explosao['sprite'].draw()
        
        if explosao['tempo'] <= 0:
            explosoes.remove(explosao)

def abate_monstros(monstros, tiros, explosoes):
    """Remove monstros ao colidir com tiros e cria explosão"""
    for tiro in tiros[:]:
        for linha in monstros:
            for monstro in linha[:]:
                if tiro.collided(monstro):
                    # Cria explosão na posição do monstro (centralizada)
                    explosao_sprite = sprite.Sprite("images/explosion2.png", 4)
                    explosao_sprite.set_total_duration(400)  # 400ms de animação
                    
                    # Centraliza a explosão na posição do monstro
                    explosao_sprite.set_position(
                        monstro.x + monstro.width / 2 - explosao_sprite.width / 2,
                        monstro.y + monstro.height / 2 - explosao_sprite.height / 2
                    )
                    
                    explosoes.append({
                        'sprite': explosao_sprite,
                        'tempo': explosao_duracao
                    })
                    
                    # Remove tiro e monstro
                    if tiro in tiros:
                        tiros.remove(tiro)
                    if monstro in linha:
                        linha.remove(monstro)
                    
                    return  # Sai para evitar problemas com iteração
