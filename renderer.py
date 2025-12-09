import numpy as np
from rayon import Rayon

black = (0,0,0)
depth_max = 2

def render(scene, camera):
    image = np.zeros((camera.image_height, camera.image_width, 3), dtype=np.float32)
    for i, j, rays in camera.generate_rayons():
        #Les rayons envoyés par la caméra touchent un objet ?
        color = [0,0,0]
        for n, rayon in enumerate(rays):
            current_color = trace(scene, rayon, 0)

            color = [(k1 * n + k2)/(n+1) for k1, k2 in zip(color, current_color)]

        image[j,i] = color
    image = np.clip(image, 0, 255)

    return image


def trace(scene, ray, depth):
    if depth > depth_max: return black


    obj, hit = scene.find_closest(ray)
    #Si oui

    if obj is not None:
        #Point de contact et normal à la surface
        pt = ray.origin + hit * ray.direction
        vecN = obj.getNormal(pt)
        #Calcul de la couleur
        #rayon du pt vers la source de lumière
        diffuse = 0
        specular_total = [0,0,0]


        #Formule de fresnel
        V = (-1 * ray.direction).normalize()
        cos_theta = max(0, vecN.dot(V))
        reflection_strength = [f + (1 - f) * (1 - cos_theta)**5 for f in obj.material.F0]
        for light in scene.lights:
            epsilon = 1e-5
            shadow_ray = light.orientation_ray(pt + vecN * epsilon)
            #objet le plus proche de la source dans la direction + distance
            _, hit_light = scene.find_closest(shadow_ray)
            #Si pas de contact ou plus loin que la source de lumière -> éclairage
            if hit_light is None or hit_light > (light.position - pt).norm():
                diffuse += light.intensite_att(pt) * max(0, vecN.dot(shadow_ray.direction)) 
                L = shadow_ray.direction 

                #Spéculaire uniquement sur un rayon direct
                if depth == 0:
                    #Spéculaire Blinn Phong
                    H = (L + V).normalize()

                    specular_brilliance = max(0, vecN.dot(H))**obj.material.shine
                    for l in range(3):
                        specular_total[l] += specular_brilliance * obj.material.ks * reflection_strength[l] * light.color[l]

        current_color = ([diffuse * obj.material.kd * obj.material.color[l]  + specular_total[l] \
                        for l in range(3)])

        #Calcul des rayons réfléchis
        epsilon = 1e-3
        relfected_ray = Rayon(pt + epsilon * vecN, ray.direction - 2 * (ray.direction.dot(vecN)) * vecN)
        reflection_color = trace(scene, relfected_ray, depth + 1)

        color = ([(1 - reflection_strength[l]) * current_color[l] + reflection_color[l] * reflection_strength[l] for l in range(3)])
    else:
        color = black
    
    return color


