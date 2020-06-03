from Model.Character import Character
from Model.Factory import *


class Builder:
    def get_sprites(self):
        pass

class Builder_Satyr(Builder):
    def __init__(self):
        self.factory = Factory_Satyr()

    def get_sprites(self):
        return {"walk": self.factory.create_walking(), "idle": self.factory.create_idle(), "attack": self.factory.create_attack(), "die": self.factory.create_dying()}

class Director:
    __builder = None

    def set_builder(self,builder):
        self.__builder = builder

    def get_player(self):
        player = Character()
        player.set_sprites(self.__builder.get_sprites())
        return player





