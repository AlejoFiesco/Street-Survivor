import pygame

class Controller:

    def __init__(self, character):
        self.character = character
        self.frame = 0
        self.state = "idle"
        self.last_state = self.state

    def motion(self,state):
        if self.state != self.last_state:
            self.frame = 0
            self.last_state = self.state
        if self.frame >= len(state) - 1:
            self.frame = 0
        self.frame += 1

    def walk_right(self):
        self.state = "walking"
        self.motion(self.character.sprites["walk"])
        self.character.pos_x += self.character.movement_speed
        return pygame.image.load(self.character.sprites["walk"][self.frame])

    def walk_left(self):
        self.state = "walking"
        self.motion(self.character.sprites["walk"])
        self.character.pos_x -= self.character.movement_speed
        return pygame.transform.flip((pygame.image.load(self.character.sprites["walk"][self.frame])),True,False)

    def idle_right(self):
        self.state = "idle"
        self.motion(self.character.sprites["idle"])
        return pygame.image.load(self.character.sprites["idle"][self.frame])

    def idle_left(self):
        self.state = "idle"
        self.motion(self.character.sprites["idle"])
        return pygame.transform.flip((pygame.image.load(self.character.sprites["idle"][self.frame])),True,False)

    def attack_right(self):
        self.state = "attacking"
        self.motion(self.character.sprites["attack"])
        return pygame.image.load(self.character.sprites["attack"][self.frame])

    def attack_left(self):
        self.state = "attacking"
        self.motion(self.character.sprites["attack"])
        return pygame.transform.flip((pygame.image.load(self.character.sprites["attack"][self.frame])),True,False)

    def die_right(self):
        self.state = "dying"
        self.motion(self.character.sprites["die"])
        return pygame.image.load(self.character.sprites["die"][self.frame])

    def die_left(self):
        self.state = "dying"
        self.motion(self.character.sprites["die"])
        return pygame.transform.flip((pygame.image.load(self.character.sprites["die"][self.frame])),True,False)
