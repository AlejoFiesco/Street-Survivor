class Character:

    def __init__(self):
        self.pos_x = 50
        self.pox_y = 450
        self.facing_at = "right"
        self.state = "idle"
        self.movement_speed = 10

    def set_sprites(self,sprites):
        self.sprites = sprites