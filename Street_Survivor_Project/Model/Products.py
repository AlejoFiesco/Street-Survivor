class Walking:
    def get_sprites(self):
        pass

class satyr_walking(Walking):
    def get_sprites(self):
        self.walking_states = list()
        for i in range (18):
            if i < 10:
                self.walking_states.append("img/Satyr_Sprites/Walking/Satyr_01_Walking_00" + str(i) + ".png")
            else:
                self.walking_states.append("img/Satyr_Sprites/Walking/Satyr_01_Walking_0" + str(i) + ".png")
        return self.walking_states

class Idle:
    def get_sprites(self):
        pass

class satyr_idle(Idle):
    def get_sprites(self):
        self.idle_states = list()
        for i in range(12):
            if i < 10:
                self.idle_states.append("img/Satyr_Sprites/Idle/Satyr_01_Idle_00" + str(i) + ".png")
            else:
                self.idle_states.append("img/Satyr_Sprites/Idle/Satyr_01_Idle_0" + str(i) + ".png")
        return  self.idle_states

class Attack:
    def get_sprites(self):
        pass

class satyr_attack(Attack):
    def get_sprites(self):
        self.attack_sprites = list()
        for i in range(12):
            if i < 10:
                self.attack_sprites.append("img/Satyr_Sprites/Attack/Satyr_01_Attacking_00" + str(i) + ".png")
            else:
                self.attack_sprites.append("img/Satyr_Sprites/Attack/Satyr_01_Attacking_0" + str(i) + ".png")
        return  self.attack_sprites

class Die:
    def get_sprites(self):
        pass

class satyr_die(Die):
    def get_sprites(self):
        self.die_sprites = list()
        for i in range(15):
            if i < 10:
                self.die_sprites.append("img/Satyr_Sprites/Dying/Satyr_01_Dying_00" + str(i) + ".png")
            else:
                self.die_sprites.append("img/Satyr_Sprites/Dying/Satyr_01_Dying_0" + str(i) + ".png")
        return self.die_sprites