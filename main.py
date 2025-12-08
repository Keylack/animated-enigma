from vector import Vector
from rayon import Camera
from scene import *
from renderer import Renderer
import pygame
import numpy as np 
from materials import *


def save_ppm(filename, np_array):
    height, width, _ = np_array.shape
    
    # ⚠️ HEADER EXACTEMENT COMME ÇA
    header = f"P6\n{width} {height}\n255\n"
    
    with open(filename, "wb") as f:
        f.write(header.encode("ascii"))
        f.write(np_array.astype(np.uint8).tobytes())

#Scene
my_cam = Camera(Vector(0,0,1), position = Vector(0,0,0), image_width = 1024, image_height = 576, aspect_ratio = 16/9)

sphere = Sphere(Vector(-4,3,10), 2, metal_blue)
sphere2 = Sphere(Vector(4,3,10), 2, plastic_red)
plane = Plane(Vector(0,-3,0), Vector(0,1,0), ground_gray) #pt0, vec normal

light = Light(Vector(0,0,0),k_att = 0)

# light2 = Light(Vector(4,2,3),k_att = 0)

# light = Light(Vector(0,2,3),k_att = 0)


scene = Scene([sphere, sphere2, plane], [light])




#PyGame params
# cell_size = 1

# fps = 1
# pygame.init()


# clock = pygame.time.Clock()
# running = True



# screen = pygame.display.set_mode((my_cam.image_width * cell_size, my_cam.image_height * cell_size))



# while running:

#     image = Renderer.render(scene, my_cam)

#     height, width, _ = image.shape

#     for j in range(height):
#         for i in range(width):
#             pygame.draw.rect(screen, image[j][i] , (i * cell_size, j * cell_size, cell_size, cell_size))

#     pygame.display.flip()
#     clock.tick(fps)


image = Renderer.render(scene, my_cam)

save_ppm("test.ppm", image)