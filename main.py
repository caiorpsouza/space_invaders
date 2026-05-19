from Cenas.Jogar import Screen
import config
from Cenas import Menu, Dificuldade


while config.is_running:
    if config.Tela == 'Menu':
        Menu.play()
    if config.Tela == 'Jogar':
        Screen.play()
    if config.Tela == 'Dificuldade':
        Dificuldade.play()