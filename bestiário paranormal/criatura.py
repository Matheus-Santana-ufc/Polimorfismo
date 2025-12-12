class Criatura:
    def __init__(self, bestiario):
        self.bestiario = bestiario

    def exibir_bestiario(self):
        print(f'\n--- Bestiário de {self.__class__.__name__} ---')

        for nome, descricao in self.bestiario.items():
            print(f'{nome}: {descricao}')
