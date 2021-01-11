import os
import sys
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Car(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image('car.png', -1)
        self.dir = True
        self.x, self.y = 0, 0

    def move(self, speed=1):
        if self.dir:
            self.x += speed
        else:
            self.x -= speed
        if (self.x == 0) or (self.x + 150 == width):
            self.change_dir()

    def change_dir(self):
        self.dir = not self.dir
        self.image = pygame.transform.flip(self.image, True, False)

    def ret_pos(self):
        return self.x, self.y


if __name__ == '__main__':
    pygame.init()
    size = width, height = 700, 95
    pygame.mouse.set_visible(False)
    screen = pygame.display.set_mode(size)
    running = True
    car = Car()
    move = False
    fps = 60
    clock = pygame.time.Clock()
    while running:
        screen.fill('white')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        car.move()
        clock.tick(fps)
        screen.blit(car.image, car.ret_pos())
        pygame.display.flip()
