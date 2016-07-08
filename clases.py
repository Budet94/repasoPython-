#Ejemplo de una clase:

class carro:
    #Metodo encargado de inicializar el carro
    #self hace referencia al objeto carro. (Equivalente a this en JAVA)
    def __init__(self,gomas,puertas,motor):
        self.gomas = gomas
        self.puertas = puertas
        self.motor = motor

    def prenderCarro(self):
        self.motor ="Brrmmmmmmrmmmm"
        print (self.motor)
    def cambiarGomas(self):
        self.gomas = 4
        print (self.gomas)
        self.gomas = 0
        print (self.gomas)
        self.gomas= 4
        print (self.gomas)
mercedes = carro(4,2,1)

#mercedes.prenderCarro()

class guagua:
    #Metodo encargado de inicializar el carro
    #self hace referencia al objeto carro. (Equivalente a this en JAVA)
    def __init__(self,gomas,puertas,motor):
        self.gomas = gomas
        self.puertas = puertas
        self.motor = motor

    def prenderCarro(self):
        self.motor ="Brrmmmmmmrmmmm"
        print (self.motor)
    def cambiarGomas(self):
        self.gomas = 4
        print (self.gomas)
        self.gomas = 0
        print (self.gomas)
        self.gomas= 4
        print (self.gomas)
mercedes = carro(4,2,1)
