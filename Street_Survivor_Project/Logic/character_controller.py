import pygame

class Controller:

    def __init__(self, character):
        self.character = character
        self.frame = 0

    def motion(self,state):
        if self.frame >= len(state) - 1:
            self.frame = 0
        self.frame += 1

    def walk_right(self):
        self.motion(self.character.sprites["walk"])
        self.character.pos_x += self.character.movement_speed
        return pygame.image.load(self.character.sprites["walk"][self.frame])

    def walk_left(self):
        self.motion(self.character.sprites["walk"])
        self.character.pos_x -= self.character.movement_speed
        return pygame.transform.flip((pygame.image.load(self.character.sprites["walk"][self.frame])),True,False)

    def idle_right(self):
        self.motion(self.character.sprites["idle"])
        return pygame.image.load(self.character.sprites["idle"][self.frame])

    def idle_left(self):
        self.motion(self.character.sprites["idle"])
        return pygame.transform.flip((pygame.image.load(self.character.sprites["idle"][self.frame])),True,False)


