class Criatura:
    def __init__(self, bestiario):
        self.bestiario = bestiario

    def exibir_bestiario(self):
        print(f'\n--- Bestiário de {self.__class__.__name__} ---')

        for nome, descricao in self.bestiario.items():
            print(f'{nome}: {descricao}')

    def adicionar_criatura(self):
        nome = input('Digite o nome da criatura: ').capitalize()
        descricao = input('Digite uma breve descrição da criatura: ')
        self.bestiario.update({nome: descricao})

    def remover_criatura(self):
        nome = input('Digite o nome da criatura: ').capitalize()
        if nome in self.bestiario:
            self.bestiario.pop(nome)