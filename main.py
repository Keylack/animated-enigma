from vector import Vector
from rayon import Camera
from scene import *
from renderer import Renderer
import pygame


#Scene
my_cam = Camera(Vector(0,0,1), image_width = 10, image_height = 10)

sphere = Sphere(Vector(0,2,10), 4)
sphere2 = Sphere(Vector(0,-2,5), 2)

light = Light(Vector(0,6,5),k_att = 0.)

scene = Scene([sphere], [light])

#PyGame params
cell_size = 1

fps = 1
pygame.init()


clock = pygame.time.Clock()
running = True



screen = pygame.display.set_mode((my_cam.image_width * cell_size, my_cam.image_height * cell_size))


while running:

    image = Renderer.render(scene, my_cam)

    height, width, _ = image.shape

    for j in range(height):
        for i in range(width):
            pygame.draw.rect(screen, image[j][i] , (i * cell_size, j * cell_size, cell_size, cell_size))

    pygame.display.flip()

    clock.tick(fps)
    break
        