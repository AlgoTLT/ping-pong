from pygame import *

window = display.set_mode((1080, 720))
display.set_caption('ping pong')

background = transform.scale(image.load("кухня.jpg"), (1080, 720))

font.init()
font2 = font.SysFont('Arial', 36)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 640:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 640:
            self.rect.y += self.speed

player_left = Player('left.png', 10, 350, 10, 20, 80)
player_right = Player('right.png', 1050, 350, 10, 20, 80)

clock = time.Clock()
FPS = 60

finish = False

run = True 
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.blit(background,(0,0))

        player_left.update_l()
        player_right.update_r()

        player_left.draw()
        player_right.draw()

        display.update()

    time.delay(50)
