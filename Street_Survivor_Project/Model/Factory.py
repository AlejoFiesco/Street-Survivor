from Model.Products import *

class Factory:
    def create_walking(self):
        pass

    def create_idle(self):
        pass

    def create_attack(self):
        pass

    def create_dying(self):
        pass


class Factory_Satyr(Factory):
    def create_walking(self):
        walking = satyr_walking()
        return walking.get_sprites()

    def create_idle(self):
        idle = satyr_idle()
        return idle.get_sprites()

    def create_attack(self):
        attack = satyr_attack()
        return attack.get_sprites()

    def create_dying(self):
        die = satyr_die()
        return die.get_sprites()
