class Vector:
    def __init__(self, x, y, z):
        self.coord = (x, y, z)

    
    def norm(self):
        return sum([x**2 for x in self.coord])**(1/2)

    def __add__(self, v2 : 'Vector') -> 'Vector':
        if not isinstance(v2, Vector):
            return NotImplemented
        #x
        x = self.coord[0] + v2.coord[0]
        #y
        y = self.coord[1] + v2.coord[1]
        #z            
        z = self.coord[2] + v2.coord[2]
        return Vector(x,y,z)
    
    def __sub__(self, v2 : 'Vector'):
        if not isinstance(v2, Vector):
            return NotImplemented
        #x
        x = self.coord[0] - v2.coord[0]
        #y
        y = self.coord[1] - v2.coord[1]
        #z            
        z = self.coord[2] - v2.coord[2]
        return Vector(x,y,z)

    def __mul__(self, k):

        
        if isinstance(k, (int, float)):
            x = k * self.coord[0]
            y = k * self.coord[1]
            z = k * self.coord[2]
        
        return Vector(x,y,z)

    def dot(self,v2):

        if isinstance(v2, Vector):
            scal = 0
        
            for i in range(3):
                scal += self.coord[i] * v2.coord[i]
        
            return scal
        else:
            return None

    def __rmul__(self, v2):
        return self.__mul__(v2)

    def __matmul__(self, v2):
        coords = []
        for i in range(0, 3):
            idx_1 = (i +1) % 3
            idx_2 = (i + 2) % 3
            k = self.coord[idx_1] * v2.coord[idx_2] - self.coord[idx_2] * v2.coord[idx_1]
        
            coords.append(k)
        return Vector(*coords)


    def normalize(self):
        norm = self.norm()
        x = self.coord[0] / norm
        y = self.coord[1] / norm
        z = self.coord[2] / norm
        return Vector(x,y,z)
    



