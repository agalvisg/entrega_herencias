class Punto2d:
    
    def __init__(self,x,y):#constructor con los métodos
        self.x=x
        self.y=y
    
    def __str__(self):
        return "X: {}; Y: {}".format(self.x, self.y)
    
    def traslacion(self,dx,dy):
        self.x +=dx
        self.y +=dy

        
class Punto3d(Punto2d):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z=z
        
    def __str__(self):
        return "{}; Z= {}".format(super().__str__(),self.z)
    
    def traslacion(self, dx, dy, dz):
        super().traslacion(dx, dy)
        self.z += dz
        
        
def obtener_coordenadas():
    x=int(input("Ingrese la coordenada x: "))
    y=int(input("Ingrese la coordenada y: "))
    z=int(input("Ingrese la coordenada z (para el punto en 3d si se desea): "))
    return x, y, z if z else None
    
#importane completar y mirar los uml's    

def main():
    #Punto A
    x1, y1=obtener_coordenadas()
    punto_a=Punto2d(x1,y1)
    print("A={}".format(punto_a))
    dx,dy=obtener_coordenadas()
    punto_a.traslacion(dx,dy)
    print("A={}".format(punto_a))
    
    
    #Punto B
    x2, y2=obtener_coordenadas()
    punto_b=Punto2d(x2,y2)
    print("B={}".format(punto_b))
    dx,dy=obtener_coordenadas()
    punto_b.traslacion(dx,dy)
    print("B={}".format(punto_b))
    
    
    #Punto C
    x3, y3, z3 =obtener_coordenadas()
    punto_c=Punto3d(x3,y3,z3)
    print("C={}".format(punto_c))
    dx,dy,dz=obtener_coordenadas()
    punto_c.traslacion(dx,dy,dz)
    print("C={}".format(punto_c))
    
if __name__=="__main__":
    main()