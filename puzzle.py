class Base: 
 
    def __init__(self): #constructor que indica el esqueleto de la clase padre
        self.a = "a" 
        self.b = "b" 
        self.c = "c" 
 
    def A(self): 
        print(self.a) 
 
    def B(self): 
        print(self.b) 
 
    def C(self): 
        print(self.c) 
 #los métodos A, B y C se utilizan para llamar a las variables que representan sus métodos
class Derivada(Base): 
 #clase derivada hereda de clase Base
    def __init__(self): 
        self.a = "aa" 
        super().__init__() 
        self.c = "cc" 
 
    def A(self): 
        print(self.a) 
 
    def B(self): 
        self.b = "bb" 
        super().B() #al usar por primera vez el .B con la clase derivada se utlizará el método B de la clase Base
        print(self.b) #a partir de la segunda vez ya se usará el método de la clase Derivada
 
base = Base() 
derivada = Derivada() 
 #se identifican las variables con sus clases respectivas para sentar el marco de las mismas
base.A() # se llama a la clase Base y a su método A
derivada.A() #se llama al método A de la clase Base  
print() 
base.B() #se llama al método B de la clase Base 
print()
derivada.B()
print() 
base.C() #se llama a
derivada.C() #se llama al método c de la clase derivada
derivada = base 
derivada.C() #se está llamando a la clase Base mediante la variable derivada
base.B() #se llama al método B de la clase Base 
print()
derivada.B()
