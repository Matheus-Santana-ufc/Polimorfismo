from carro import Carro

class CarroEsportivo(Carro):
    def __init__(self, velocidade_inicial):
        super().__init__(velocidade_inicial)

    def turbo(self):
        self.velocidade += 10
        print('Turbo Ativado! A velocidade aumentou em 10km/h')