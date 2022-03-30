class Pared: 
    def __init__(self, orientacion):
        self.orientacion=orientacion

class Ventana: 
    def __init__(self,pared,superficie):
        self.superficie=superficie
        self.pared=pared #agregación

class Casa:
    def __init__(self ,ventanas):
        self.ventana0=ventanas[0] #agregación
        self.ventana1=ventanas[1] #agregación
        self.ventana2=ventanas[2] #agregación
        self.ventana3=ventanas[3] #agregación

    def superficie_acristalada(self):
        area=self.ventana0.superficie+self.ventana1.superficie+self.ventana2.superficie+self.ventana3.superficie
        return (area)
