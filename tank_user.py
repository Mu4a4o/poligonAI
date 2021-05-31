import math
import pygame
import time


class Tank_gissinits(pygame.sprite.Sprite):
    def __init__(self, tank_x, tank_y, right_true=False, image_size=5):
        pygame.sprite.Sprite.__init__(self)
        self._gissinits_count = 0
        self.tank_x = tank_x
        self.tank_y = tank_y
        self.tank_rotate_angle = 90
        self.angle = 0
        self.image_size = image_size
        if right_true:
            self.image_group = [pygame.image.load('sprite/tank gissinits/0_r.png').convert_alpha(),
                                pygame.image.load('sprite/tank gissinits/1_r.png').convert_alpha(),
                                pygame.image.load('sprite/tank gissinits/2_r.png').convert_alpha(),
                                pygame.image.load('sprite/tank gissinits/3_r.png').convert_alpha()]
        else:
            self.image_group = [pygame.image.load('sprite/tank gissinits/0_l.png').convert_alpha(),
                                pygame.image.load('sprite/tank gissinits/1_l.png').convert_alpha(),
                                pygame.image.load('sprite/tank gissinits/2_l.png').convert_alpha(),
                                pygame.image.load('sprite/tank gissinits/3_l.png').convert_alpha()]
        self.image = pygame.transform.scale(self.image_group[0], (self.image_group[0].get_width() // self.image_size,
                                                                  self.image_group[0].get_height() // self.image_size))
        self.image = pygame.transform.rotate(self.image, 0)
        self.rect = self.image.get_rect(center=(self.tank_x, self.tank_y))

    @property
    def gissinits_count(self):
        return self._gissinits_count

    @gissinits_count.setter
    def gissinits_count(self, gissinits_count):
        if gissinits_count > 3:
            self._gissinits_count = 0
        elif gissinits_count < 0:
            self._gissinits_count = 3
        else:
            self._gissinits_count = gissinits_count

    def update(self):
        self.image = pygame.transform.scale(self.image_group[self.gissinits_count],
                                            (self.image_group[self.gissinits_count].get_width() // self.image_size,
                                             self.image_group[self.gissinits_count].get_height() // self.image_size))
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect(center=(self.tank_x, self.tank_y))

    def rotate(self, up=False, down=False, left_up_rot=False,
               right_up_rot=False, left_down_rot=False, right_down_rot=False):
        if up:
            self.gissinits_count += 1
            self.tank_y += 2 * math.cos(math.radians(self.tank_rotate_angle + 90))
            self.tank_x -= 2 * math.sin(math.radians(self.tank_rotate_angle + 90))
        elif down:
            self.gissinits_count -= 1
            self.tank_y -= 2 * math.cos(math.radians(self.tank_rotate_angle + 90))
            self.tank_x += 2 * math.sin(math.radians(self.tank_rotate_angle + 90))

        if left_up_rot:
            first_y = self.tank_y
            first_x = self.tank_x
            self.tank_rotate_angle -= 0.6
            self.gissinits_count += 1
            self.tank_y += 2 * math.cos(math.radians(self.tank_rotate_angle + 90))
            self.tank_x -= 2 * math.sin(math.radians(self.tank_rotate_angle + 90))
            self.image = pygame.transform.scale(self.image_group[self.gissinits_count],
                                                (self.image_group[self.gissinits_count].get_width() // self.image_size,
                                                 self.image_group[
                                                     self.gissinits_count].get_height() // self.image_size))
            self.angle = math.degrees(math.atan2((self.tank_x - first_x), (self.tank_y - first_y)))
            self.image = pygame.transform.rotate(self.image, self.angle - 180)
        elif right_up_rot:
            first_y = self.tank_y
            first_x = self.tank_x
            self.tank_rotate_angle += 0.6
            self.gissinits_count += 1
            self.tank_y += 2 * math.cos(math.radians(self.tank_rotate_angle + 90))
            self.tank_x -= 2 * math.sin(math.radians(self.tank_rotate_angle + 90))
            self.image = pygame.transform.scale(self.image_group[self.gissinits_count],
                                                (self.image_group[self.gissinits_count].get_width() // self.image_size,
                                                 self.image_group[
                                                     self.gissinits_count].get_height() // self.image_size))
            self.angle = math.degrees(math.atan2((self.tank_x - first_x), (self.tank_y - first_y)))
            self.image = pygame.transform.rotate(self.image, self.angle - 180)

        if left_down_rot:
            first_y = self.tank_y
            first_x = self.tank_x
            self.tank_rotate_angle += 0.6
            self.gissinits_count -= 1
            self.tank_y -= 2 * math.cos(math.radians(self.tank_rotate_angle + 90))
            self.tank_x += 2 * math.sin(math.radians(self.tank_rotate_angle + 90))
            self.image = pygame.transform.scale(self.image_group[self.gissinits_count],
                                                (self.image_group[self.gissinits_count].get_width() // self.image_size,
                                                 self.image_group[
                                                     self.gissinits_count].get_height() // self.image_size))
            self.angle = math.degrees(math.atan2((self.tank_x - first_x), (self.tank_y - first_y)))
            self.image = pygame.transform.rotate(self.image, self.angle)
        elif right_down_rot:
            first_y = self.tank_y
            first_x = self.tank_x
            self.tank_rotate_angle -= 0.6
            self.gissinits_count -= 1
            self.tank_y -= 2 * math.cos(math.radians(self.tank_rotate_angle + 90))
            self.tank_x += 2 * math.sin(math.radians(self.tank_rotate_angle + 90))
            self.image = pygame.transform.scale(self.image_group[self.gissinits_count],
                                                (self.image_group[self.gissinits_count].get_width() // self.image_size,
                                                 self.image_group[
                                                     self.gissinits_count].get_height() // self.image_size))
            self.angle = math.degrees(math.atan2((self.tank_x - first_x), (self.tank_y - first_y)))
            self.image = pygame.transform.rotate(self.image, self.angle)


class Tank_base(pygame.sprite.Sprite):
    def __init__(self, tank_x, tank_y, image_size=5):
        pygame.sprite.Sprite.__init__(self)
        self.tank_y = tank_y
        self.tank_x = tank_x
        self.angle = 90
        self.tank_rotate_angle = 90
        self.image_size = image_size
        self.path_image = pygame.image.load('sprite/tank base/0.png').convert_alpha()
        self.image = pygame.transform.scale(self.path_image, (self.path_image.get_width() // self.image_size,
                                                              self.path_image.get_height() // self.image_size))
        self.image = pygame.transform.rotate(self.image, 0)
        self.rect = self.image.get_rect(center=(self.tank_x, self.tank_y))

    def update(self):
        self.rect = self.image.get_rect(center=(self.tank_x, self.tank_y))

    def rotate(self, up=False, down=False, left_up_rot=False,
               right_up_rot=False, left_down_rot=False, right_down_rot=False):
        if up:
            self.tank_y += 2 * math.cos(math.radians(self.tank_rotate_angle + 90))
            self.tank_x -= 2 * math.sin(math.radians(self.tank_rotate_angle + 90))
        elif down:
            self.tank_y -= 2 * math.cos(math.radians(self.tank_rotate_angle + 90))
            self.tank_x += 2 * math.sin(math.radians(self.tank_rotate_angle + 90))

        if left_up_rot:
            first_y = self.tank_y
            first_x = self.tank_x
            self.tank_rotate_angle -= 0.6
            self.tank_y += 2 * math.cos(math.radians(self.tank_rotate_angle + 90))
            self.tank_x -= 2 * math.sin(math.radians(self.tank_rotate_angle + 90))
            self.image = pygame.transform.scale(self.path_image, (self.path_image.get_width() // self.image_size,
                                                                  self.path_image.get_height() // self.image_size))
            self.angle = math.degrees(math.atan2((self.tank_x - first_x), (self.tank_y - first_y)))
            self.image = pygame.transform.rotate(self.image, self.angle - 180)
        elif right_up_rot:
            first_y = self.tank_y
            first_x = self.tank_x
            self.tank_rotate_angle += 0.6
            self.tank_y += 2 * math.cos(math.radians(self.tank_rotate_angle + 90))
            self.tank_x -= 2 * math.sin(math.radians(self.tank_rotate_angle + 90))
            self.image = pygame.transform.scale(self.path_image, (self.path_image.get_width() // self.image_size,
                                                                  self.path_image.get_height() // self.image_size))
            self.angle = math.degrees(math.atan2((self.tank_x - first_x), (self.tank_y - first_y)))
            self.image = pygame.transform.rotate(self.image, self.angle - 180)

        if left_down_rot:
            first_y = self.tank_y
            first_x = self.tank_x
            self.tank_rotate_angle += 0.6
            self.tank_y -= 2 * math.cos(math.radians(self.tank_rotate_angle + 90))
            self.tank_x += 2 * math.sin(math.radians(self.tank_rotate_angle + 90))
            self.path_image = pygame.image.load('sprite/tank base/0.png').convert_alpha()
            self.image = pygame.transform.scale(self.path_image, (self.path_image.get_width() // self.image_size,
                                                                  self.path_image.get_height() // self.image_size))
            self.angle = math.degrees(math.atan2((self.tank_x - first_x), (self.tank_y - first_y)))
            self.image = pygame.transform.rotate(self.image, self.angle)
        elif right_down_rot:
            first_y = self.tank_y
            first_x = self.tank_x
            self.tank_rotate_angle -= 0.6
            self.tank_y -= 2 * math.cos(math.radians(self.tank_rotate_angle + 90))
            self.tank_x += 2 * math.sin(math.radians(self.tank_rotate_angle + 90))
            self.path_image = pygame.image.load('sprite/tank base/0.png').convert_alpha()
            self.image = pygame.transform.scale(self.path_image, (self.path_image.get_width() // self.image_size,
                                                                  self.path_image.get_height() // self.image_size))
            self.angle = math.degrees(math.atan2((self.tank_x - first_x), (self.tank_y - first_y)))
            self.image = pygame.transform.rotate(self.image, self.angle)


class Tank_tower(pygame.sprite.Sprite):
    def __init__(self, tank_y, tank_x, image_size=5):
        pygame.sprite.Sprite.__init__(self)
        self.tank_y = tank_y
        self.tank_x = tank_x
        self.angle = 90
        self.tank_rotate_angle = 90
        self.image_size = image_size
        self.shoots_count = 0
        self.shoots_first = time.time()
        self.image_group_shoots = [pygame.image.load('sprite/tank tower/shoot/0.png').convert_alpha(),
                                   pygame.image.load('sprite/tank tower/shoot/1.png').convert_alpha(),
                                   pygame.image.load('sprite/tank tower/shoot/2.png').convert_alpha(),
                                   pygame.image.load('sprite/tank tower/shoot/3.png').convert_alpha(),
                                   pygame.image.load('sprite/tank tower/shoot/4.png').convert_alpha(),
                                   pygame.image.load('sprite/tank tower/shoot/5.png').convert_alpha(),
                                   pygame.image.load('sprite/tank tower/shoot/6.png').convert_alpha(),
                                   pygame.image.load('sprite/tank tower/shoot/7.png').convert_alpha(),
                                   pygame.image.load('sprite/tank tower/shoot/8.png').convert_alpha(),
                                   pygame.image.load('sprite/tank tower/shoot/9.png').convert_alpha(),
                                   pygame.image.load('sprite/tank tower/shoot/10.png').convert_alpha()]
        self.image = pygame.transform.scale(self.image_group_shoots[0],
                                            (self.image_group_shoots[0].get_width() // self.image_size,
                                             self.image_group_shoots[0].get_height() // self.image_size))
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect(center=(self.tank_x, self.tank_y))

    def shoots(self, fire=False):
        shoots_first = time.time() - self.shoots_first
        if 0 < self.shoots_count < 10:
            self.shoots_count += 1
        elif self.shoots_count == 10 and shoots_first >= 2:
            self.shoots_count = 0
            self.shoots_first >= time.time()
        if fire and self.shoots_count == 0:
            self.shoots_count += 1

    def rotate(self, up=False, down=False, left_up_rot=False,
               right_up_rot=False, left_down_rot=False, right_down_rot=False):
        if up:
            self.tank_y += 2 * math.cos(math.radians(self.tank_rotate_angle + 90))
            self.tank_x -= 2 * math.sin(math.radians(self.tank_rotate_angle + 90))
        elif down:
            self.tank_y -= 2 * math.cos(math.radians(self.tank_rotate_angle + 90))
            self.tank_x += 2 * math.sin(math.radians(self.tank_rotate_angle + 90))

        if left_up_rot:
            self.tank_rotate_angle -= 0.6
            self.tank_y += 2 * math.cos(math.radians(self.tank_rotate_angle + 90))
            self.tank_x -= 2 * math.sin(math.radians(self.tank_rotate_angle + 90))

        elif right_up_rot:
            self.tank_rotate_angle += 0.6
            self.tank_y += 2 * math.cos(math.radians(self.tank_rotate_angle + 90))
            self.tank_x -= 2 * math.sin(math.radians(self.tank_rotate_angle + 90))

        if left_down_rot:
            self.tank_rotate_angle += 0.6
            self.tank_y -= 2 * math.cos(math.radians(self.tank_rotate_angle + 90))
            self.tank_x += 2 * math.sin(math.radians(self.tank_rotate_angle + 90))

        elif right_down_rot:
            self.tank_rotate_angle -= 0.6
            self.tank_y -= 2 * math.cos(math.radians(self.tank_rotate_angle + 90))
            self.tank_x += 2 * math.sin(math.radians(self.tank_rotate_angle + 90))

    def update(self):
        self.shoots()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.angle = math.degrees(math.atan2((self.tank_x - mouse_x), (self.tank_y - mouse_y)))
        self.image = pygame.transform.scale(self.image_group_shoots[self.shoots_count],
                                            (self.image_group_shoots[self.shoots_count].get_width() // self.image_size,
                                             self.image_group_shoots[
                                                 self.shoots_count].get_height() // self.image_size))
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect(center=(self.tank_x, self.tank_y))


def bresenham(x1=0, y1=0, x2=0, y2=0, speed=1) -> object:

    dx = x2 - x1
    dy = y2 - y1

    sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
    sign_y = 1 if dy > 0 else -1 if dy < 0 else 0

    if dx < 0: dx = -dx
    if dy < 0: dy = -dy

    if dx > dy:
        pdx, pdy = sign_x, 0
        es, el = dy, dx
    else:
        pdx, pdy = 0, sign_y
        es, el = dx, dy

    x, y = x1, y1

    error, t = el / 2, 0

    list_line_all = []
    while t < el:
        error -= es
        if error < 0:
            error += el
            x += sign_x
            y += sign_y
        else:
            x += pdx
            y += pdy
        t += 1
        list_line_all.append((x, y))
    list_line_speed = []
    for i in range(0, len(list_line_all), speed):
        list_line_speed.append(list_line_all[i])
    return iter(list_line_speed)


class Rocket(pygame.sprite.Sprite):
    def __init__(self, tank_y, tank_x, image_size=5):
        pygame.sprite.Sprite.__init__(self)
        self.tank_y = tank_y
        self.tank_x = tank_x
        self.tank_y_first = tank_y
        self.tank_x_first = tank_x
        self.angle = 90
        self.tank_rotate_angle = 90
        self.image_size = image_size
        self.shoots_count = 0
        self.shoots_first = time.time()
        self.shot = False
        self.mouse_x_shoot = 0
        self.mouse_y_shoot = 0
        self.bresenham_line = []
        self.path_image = pygame.image.load('sprite/rocket/0.png').convert_alpha()
        self.image = pygame.transform.scale(self.path_image, (self.path_image.get_width() // self.image_size,
                                                              self.path_image.get_height() // self.image_size))
        self.rect = self.image.get_rect(center=(self.tank_x, self.tank_y))

    def shoot(self):
        self.shot = True
        self.mouse_x_shoot, self.mouse_y_shoot = pygame.mouse.get_pos()
        self.bresenham_line = bresenham(self.tank_x, self.tank_y, self.mouse_x_shoot, self.mouse_y_shoot, speed=7)

    def update(self, tank_x, tank_y):
        if self.shot:
            try:
                self.tank_x, self.tank_y = next(self.bresenham_line)
            except StopIteration:
                self.tank_x = tank_x
                self.tank_y = tank_y
                self.shot = False
            self.angle = math.degrees(
                math.atan2((self.tank_x - self.mouse_x_shoot), (self.tank_y - self.mouse_y_shoot)))
            self.image = pygame.transform.scale(self.path_image, (self.path_image.get_width() // self.image_size,
                                                                  self.path_image.get_height() // self.image_size))
            print(self.angle)
            self.image = pygame.transform.rotate(self.image, self.angle)
            self.rect = self.image.get_rect(center=(self.tank_x, self.tank_y))


        else:
            self.tank_y = tank_y
            self.tank_x = tank_x
            self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
            self.angle = math.degrees(math.atan2((self.tank_x - self.mouse_x), (self.tank_y - self.mouse_y)))
            self.image = pygame.transform.scale(self.path_image, (self.path_image.get_width() // self.image_size,
                                                                  self.path_image.get_height() // self.image_size))
            self.tank_x = math.sin(self.angle/57) * -45 + self.tank_x;
            self.tank_y = math.cos(self.angle/57) * -45 + self.tank_y;
            self.image = pygame.transform.rotate(self.image, self.angle)
            self.rect = self.image.get_rect(center=(self.tank_x, self.tank_y))
            self.image.set_alpha(0)


