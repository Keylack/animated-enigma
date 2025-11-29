import numpy as np

class Renderer:
    def render(scene, camera):
        image = np.zeros((camera.image_height, camera.image_width, 3), dtype=np.float32)
        for i, j, rayon in camera.generate_rayons():
            #Les rayons envoyés par la caméra touchent un objet ?
            obj, hit = scene.find_closest(rayon)
            #Si oui
            if obj is not None:
                #Point de contact et normal à la surface
                pt = camera.position + hit * rayon.direction
                vecN = obj.getNormal(pt)
                #Calcul de la couleur
                #rayon du pt vers la source de lumière
                diffuse = 0
                for light in scene.lights:
                    reverse_ray_light = light.orientation_ray(pt)
                    #objet le plus proche de la source dans la direction + distance
                    _, hit_light = scene.find_closest(reverse_ray_light)
                    #Si pas de contact ou plus loin que la source de lumière -> éclairage
                    if hit_light is None or hit_light > (light.position - pt).norm():
                        diffuse += light.intensite_att(pt) * max(0, vecN.dot(-1 * reverse_ray_light.direction)) 
                        print(diffuse, 0, vecN.dot(1 * reverse_ray_light.direction))

                color = ([x * diffuse for x in obj.color])
                image[j,i] = color
        image = np.clip(image, 0, 255)

        return image
