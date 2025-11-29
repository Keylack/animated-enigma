import math
from vector import Vector

class Rayon:
    def __init__(self, origin : 'Vector', direction : 'Vector normalisé'):
        self.origin = origin
        self.direction = direction
    

class Camera:
    def __init__(self, orientation : 'Vector',FOV = 90, aspect_ratio = 16/9, image_width = 1280, image_height = 720 ):
        self.position = Vector(0,0,0)
        self.orientation = orientation.normalize()

        #Plan
        self.d = 1
        self.FOV = FOV
        self.aspect_ratio = aspect_ratio
        self.image_height = image_height
        self.image_width = image_width


    def get_plan_dim(self):
        h = 2 * math.tan(math.radians(self.FOV/2))
        w = h * self.aspect_ratio
        return (w,h)

    def get_center_plan(self):
        origin_plan = self.position + (self.d * self.orientation.normalize())
        return origin_plan


    def plan_axis(self):

        #Axes du plan d projection
        up_world = Vector(0,1,0)

        right = (up_world @ self.orientation).normalize()

        up = (right @ self.orientation).normalize()

        return right, up

    def generate_rayons(self):

        #Disposition des pixels

        width, height = self.get_plan_dim()

        right, up = self.plan_axis()

        rayons = []

        #position dans -0.5 - +0.5 widht/height
        for i in range(0, self.image_width):
            for j in range(0, self.image_height):
                x1 = ((i + 1/2) / self.image_width - 0.5) * width
                x2 = ((j + 1/2) / self.image_height - 0.5) * height
                
                pt_origin = self.get_center_plan() + x1 * right + x2 * up
                new_ray = Rayon(self.position, (pt_origin - self.position).normalize())
                rayons.append((i, j, new_ray))

        return rayons



