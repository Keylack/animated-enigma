from rayon import Rayon

class Scene:
    def __init__(self, objList : list, lightSources : list):
        #lightSources pour plus tard

        self.objects = objList
        self.lights = lightSources

    def add_object(self, obj):
        self.objects.append(obj)

    def add_lightSource(self, light):
        self.lights.append(light)

    def find_closest(self,ray):
        
        t_closest = None
        closest = None
        for obj in self.objects:
            t = obj.intersect(ray)
            if t is not None and t > 0:
                if t_closest is None:
                    t_closest = t
                    closest = obj
                else:
                    if t < t_closest:
                        t_closest = t 
                        closest = obj

        return closest, t_closest


class Object3D:
    def __init__(self, material):
        self.material = material


    def intersect(self, ray):
        raise NotImplementedError("intersect() must be implemented in derived classes")

    def getNormal(self, ray):
        raise NotImplementedError("getNormal() must be implemented in derived classes")

class Sphere(Object3D):
    def __init__(self, centre, radius, material):
        super().__init__(material)
        self.centre = centre
        self.radius = radius

    def intersect(self, ray):
        L = ray.origin - self.centre
        b = 2 * (ray.direction.dot(L))
        c = L.dot(L) - self.radius**2

        delta = b**2 - 4 * c

        if delta < 0:
            return None
        
        elif delta == 0:
            if -b/2 > 0:
                return -b/2
        elif delta > 0:
            #Deux solutions (on prend la plus petite (première collision))
            a1 = max(0, (-b + delta**(1/2))/2) 
            a2 = max(0, (-b - delta**(1/2))/2)


            if min(a1,a2) > 0:
                return min(a1,a2)
        
        return None
        
    def getNormal(self, pt):
        return (pt - self.centre).normalize()
    


class Plane(Object3D):
    def __init__(self, pt0 : "Vector", normal : "Vector", material):
        super().__init__(material)
        self.pt0 = pt0 #Point appartenant au plan
        self.normal = normal #Vecteur normal au plan

    def intersect(self, ray : "Rayon"):
        #formule
        t = max(0, (self.normal.dot(self.pt0 - ray.origin)) / (self.normal.dot(ray.direction)))
        if t > 0:
            return t 
        else:
            return None        
    
    def getNormal(self, pt = None):
        return self.normal


class Light:
    def __init__(self, position, intensite : "0-1" = 1,k_att = 1, color=(255,255,255)):
        self.position = position
        self.intensite = intensite #intensité nominale
        self.k = k_att
        self.color = color

    
    def intensite_att(self, pt):
        d = self.distance_pt(pt)
        return self.intensite * 1 / (1 + self.k * d**2)
    
    def orientation_ray(self, pt):  
        #Vecteur normalisé direction du point vers la source
        vec = (self.position - pt).normalize()

        return Rayon(pt, vec) 

    def distance_pt(self, pt):
        return (pt - self.position).norm()