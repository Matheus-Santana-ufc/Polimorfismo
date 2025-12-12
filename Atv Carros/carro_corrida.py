from carro import Carro

class CarroCorrida(Carro):
    def __init__(self, velocidade_inicial):
        super().__init__(velocidade_inicial)

    def acelerar(self):
        self.velocidade += 5
        print('Aceleração de Corrida! A Velocidade aumentou em 5km/h')