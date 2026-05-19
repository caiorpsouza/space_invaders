from PPlay import *
import config

inverte = False

def inicializar_monstros(c, l):
    monstros = []
    for i in range(c):
        linha_atual = []
        for j in range(l):
            m = sprite.Sprite('images/monstro_spritesheet.png', 4)
            m.set_total_duration(1000)


            m.set_position(j * (m.width/2 + m.width + 20)+50, i * (m.height/2 + m.height + 10)+30)
            linha_atual.append(m)
        monstros.append(linha_atual)
    return monstros


def desce_monstros(monstros, lado, monstro_vel):
    for linha in monstros:
        for monstro in linha:
            monstro.y += monstro.height/2
            if lado == 'right':
                monstro.x += monstro_vel * config.janela.delta_time() * -1
            if lado == 'left':
                monstro.x += monstro_vel * config.janela.delta_time()


def monstros_loop(monstros, monstro_vel, inverte):
    for linha in monstros:
        for monstro in linha:
            #Inversão do movimento de cada monstro
            if monstro.x + monstro.width >= config.janela.largura*39/40:
                inverte = True
                desce_monstros(monstros, 'right', monstro_vel)
            if monstro.x <= config.janela.largura/40:
                desce_monstros(monstros, 'left', monstro_vel)
                inverte = False
            #Movimentação de cada monstro
            if inverte:
                monstro.x += monstro_vel * config.janela.delta_time() * -1
            else:
                monstro.x += monstro_vel * config.janela.delta_time()
            
            monstro.update()
            monstro.draw()
    return inverte

def monsters_combat(monstros, nave, em_combate):
    for linha in monstros:
            for monstro in linha:
                if monstro.y + monstro.height >= nave.y:
                    em_combate = False
    return em_combate