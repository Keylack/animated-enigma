class Material:
    def __init__(self, color, ks, shine, kd = 1.0, metallic = False):
        self.color = color
        self.ks = ks
        self.shine = shine
        self.metallic = metallic
        if self.metallic == True:
            self.kd = 0
            self.F0 = ([x / 255 for x in self.color])
        else:
            self.kd = kd
            self.F0 = (0.04,0.04,0.04)




plastic_red = Material(color=(255,50,50), kd=0.9, ks=0.4, shine = 50)
metal_blue  = Material(color=(50,50,255), ks=1.0, shine=200, metallic = True)
ground_gray = Material(color=(100,100,100), kd=1.0, ks=0.0, shine=1)
gold = Material(color=(255,181,74), ks=1.0, metallic = True, shine=200)