from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()

        class(Sprite):
            self.image = transform.scale()
            self.speed = player_speed()
            self.rect = self.image.get_rect()
            self.rect.x = player_x
            self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect))

    background = (190, 255, 100)
    win_width = 680
    win_height = 500
    window = display.set_mode((win_width, win_height))
    window.fill(back)