class Pared: 
    def __init__(self, horientacion):
        self.horientacion=horientacion

class Ventana: 
    def __init__(self, horientacion, superficie):
        super().__init__(horientacion)
        self.superficie=superficie
        return self.superficie

class Casa:
    def __init__(self, paredes, horientacion, superficie):
        self.paredes=paredes
    def superficieacristalada(self):
        return(self.paredes.superficie)