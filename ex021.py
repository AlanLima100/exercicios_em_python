#faça UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA O AUDIO DE UM ARQUIVO MP3

import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
input()
pygame.event.wait()







