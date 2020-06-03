import pygame
from Logic.window_controler import Window_Controller
from Logic.character_controller import Controller
from Model.Builder import *

pygame.init()
screen = pygame.display.set_mode((1340,680))
pygame.display.set_caption("Street Survivor Project")

game_running = True
clock = pygame.time.Clock()

director = Director()
director.set_builder(Builder_Satyr())
player = director.get_player()
player_controller = Controller(player)

background = pygame.transform.scale(pygame.image.load("img/Background/bg.png"),(1320,640))

controller = Window_Controller(player_controller , screen)

while game_running:
    clock.tick(25)

    screen.blit(pygame.transform.scale((background),(1350,700)), (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            controller.action("left")
        elif event.key == pygame.K_d:
            controller.action("right")
        elif event.key == pygame.K_w:
            controller.action("up")
        elif event.key == pygame.K_s:
            controller.action("down")
        else:
            controller.action("idle")
    else:
        controller.action("idle")

    pygame.display.update()