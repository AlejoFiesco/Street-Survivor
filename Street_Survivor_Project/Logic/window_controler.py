class Window_Controller:
    def __init__(self , character_controller , screen):
        self.character_controller = character_controller
        self.screen = screen

    def action(self , action):



        if action == "right":
            self.character_controller.character.facing_at = "right"
            self.screen.blit(self.character_controller.walk_right(),
                             (self.character_controller.character.pos_x,self.character_controller.character.pox_y))

        if action == "left":
            self.character_controller.character.facing_at = "left"
            self.screen.blit(self.character_controller.walk_left(),
                             (self.character_controller.character.pos_x,self.character_controller.character.pox_y))

        if action == "idle":
            if self.character_controller.character.facing_at == "right":
                self.screen.blit(self.character_controller.idle_right(),
                                 (self.character_controller.character.pos_x, self.character_controller.character.pox_y))
            else:self.screen.blit(self.character_controller.idle_left(),
                                 (self.character_controller.character.pos_x, self.character_controller.character.pox_y))

        if action == "die":
            if self.character_controller.character.facing_at == "right":
                self.screen.blit(self.character_controller.die_right(),
                                 (self.character_controller.character.pos_x, self.character_controller.character.pox_y))
            else:self.screen.blit(self.character_controller.die_left(),
                                 (self.character_controller.character.pos_x, self.character_controller.character.pox_y))

        if action == "attack":
            if self.character_controller.character.facing_at == "right":
                self.screen.blit(self.character_controller.attack_right(),
                                 (self.character_controller.character.pos_x, self.character_controller.character.pox_y))
            else:self.screen.blit(self.character_controller.attack_left(),
                                 (self.character_controller.character.pos_x, self.character_controller.character.pox_y))