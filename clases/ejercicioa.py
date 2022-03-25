class NuevaYork: 
 
    def __del__(self): 
        print("Destrucción Nueva York") 
 
    def __init__(self): 
        # Declaración de una lista de instancias de Habitacion 
        # con nombres diferentes. 
        self.edificio = [edificio(name) for name in ["A","B"] ]
        self.empleado = [empleado(name) for name in ["Sres. Martin","Salim","Sra.Xing"]]

class edificio: 
 
    def __del__(self): 
        print("Destrucción {}".format(self.name)) 
 
    def __init__(self, name): 
        self.name = name 

class empleado: 
 
    def __del__(self): 
        print("Destrucción {}".format(self.name)) 
 
    def __init__(self, name): 
        self.name = name 

ny = NuevaYork()
del ny