import pygame
from tank_user import Tank_gissinits, Tank_base, Tank_tower

pygame.init()
sc = pygame.display.set_mode((1024, 768), pygame.DOUBLEBUF | pygame.HWSURFACE)
pygame.display.set_caption('poligonAI')
сlock = pygame.time.Clock()
RED = (255, 0, 0)
image_size = 1
surf = pygame.Surface((200, 200))
surf.fill(RED)

tank_one = pygame.sprite.Group()
tank_gissinits_left = Tank_gissinits(tank_x=400, tank_y=400, image_size=image_size)
tank_gissinits_right = Tank_gissinits(tank_x=400, tank_y=400, right_true=True, image_size=image_size)
tank_base = Tank_base(tank_gissinits_left.rect.topright[0], tank_gissinits_left.rect.topright[1], image_size=image_size)
tank_tower = Tank_tower(tank_gissinits_left.rect.topright[0], tank_gissinits_left.rect.topright[1], image_size=image_size)
tank_one.add(tank_gissinits_left, tank_gissinits_right, tank_base, tank_tower)


running = True
while running:
    for event in pygame.event.get():
        # действие при выходе
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    mouse = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()
    if mouse[0]:
        tank_tower.shoots(fire=True)
    # управление танком и изменение его свойств
    if keys[pygame.K_UP] and not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
        tank_gissinits_left.rotate(up=True)
        tank_gissinits_right.rotate(up=True)
        tank_base.rotate(up=True)
        tank_tower.rotate(up=True)
    elif keys[pygame.K_DOWN] and not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
        tank_gissinits_left.rotate(down=True)
        tank_gissinits_right.rotate(down=True)
        tank_base.rotate(down=True)
        tank_tower.rotate(down=True)

    if keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
        tank_gissinits_left.rotate(right_up_rot=True)
        tank_gissinits_right.rotate(right_up_rot=True)
        tank_base.rotate(right_up_rot=True)
        tank_tower.rotate(right_up_rot=True)
    elif keys[pygame.K_LEFT] and keys[pygame.K_UP]:
        tank_gissinits_left.rotate(left_up_rot=True)
        tank_gissinits_right.rotate(left_up_rot=True)
        tank_base.rotate(left_up_rot=True)
        tank_tower.rotate(left_up_rot=True)
    elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
        tank_gissinits_left.rotate(left_down_rot=True)
        tank_gissinits_right.rotate(left_down_rot=True)
        tank_base.rotate(left_down_rot=True)
        tank_tower.rotate(left_down_rot=True)
    elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
        tank_gissinits_left.rotate(right_down_rot=True)
        tank_gissinits_right.rotate(right_down_rot=True)
        tank_base.rotate(right_down_rot=True)
        tank_tower.rotate(right_down_rot=True)

    sc.fill((0, 0, 0))
    tank_one.draw(sc)
    tank_one.update()
    pygame.display.update()

    # FPS 60

    сlock.tick(60)
