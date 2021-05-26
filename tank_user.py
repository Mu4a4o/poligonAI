import math
import pygame
'test'

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
        self.rect = self.image.get_rect(topright=(self.tank_x, self.tank_y))

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
        self.rect = self.image.get_rect(topright=(self.tank_x, self.tank_y))
        self.rect.center = round(self.tank_x), round(self.tank_y)

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
        self.rect = self.image.get_rect(topleft=(self.tank_x, self.tank_y))

    def update(self):
        self.rect = self.image.get_rect(topleft=(self.tank_x, self.tank_y))
        self.rect.center = round(self.tank_x), round(self.tank_y)

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

    def shoots(self, fire = False):
        if 0 < self.shoots_count <10:
            self.shoots_count += 1
        elif self.shoots_count >= 10 or self.shoots_count == 0:
            self.shoots_count = 0
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


