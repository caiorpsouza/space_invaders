import config
from Cenas import Menu, Dificuldade, Jogar


while config.is_running:
    if config.Tela == 'Menu':
        Menu.play()
    if config.Tela == 'Jogar':
        Jogar.play()
    if config.Tela == 'Dificuldade':
        Dificuldade.play()