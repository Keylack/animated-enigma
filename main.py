from vector import Vector
from rayon import Camera
from scene import *
from renderer import Renderer
import pygame


#Scene
my_cam = Camera(Vector(0,-2,1), position = Vector(0,6,0), image_width = 1024, image_height = 576)

sphere = Sphere(Vector(-4,4,5), 1)
sphere2 = Sphere(Vector(4,0,5), 1)
plane = Plane(Vector(0,-3,0), Vector(0,1,0)) #pt0, vec normal

light = Light(Vector(0,2,5),k_att = 0)

scene = Scene([sphere,sphere2,plane], [light])

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
    
        