from carro_corrida import CarroCorrida
from carro_esportivo import CarroEsportivo
from carro_inteligente import CarroInteligente

def test_drive(Carro):
    print(f'\nTestando {Carro.__class__.__name__}')
    Carro.acelerar()
    Carro.exibir_velocidade()

if __name__ == '__main__':
    carro_inteligente = CarroInteligente(10)
    print('Carro Inteligente: ')
    carro_inteligente.estaciona()
    test_drive(carro_inteligente)

    carro_esportivo = CarroEsportivo(50)
    print('Carro Esportivo: ')
    carro_esportivo.turbo()
    test_drive(carro_esportivo)

    carro_corrida = CarroCorrida(100)
    print('Carro Corrida: ')
    test_drive(carro_corrida)