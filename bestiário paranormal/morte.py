from criatura import Criatura

class Morte(Criatura):
    def __init__(self, bestiario):
        super().__init__(bestiario)
        self.bestiario = {'\nDeus da Morte': 'O Deus da Morte, também conhecido como Parasita de Dimensões, é uma entidade suprema e extremamente poderosa.'
        '\nOriginalmente essa entidade se manifesta em uma aparência disforme que infecta o ambiente inteiro consumindo a entropia, ou seja, '
        '\na energia potencial e o tempo de tudo que é vivo','\nNidere': '“Nidere, o lobo invertido” é um monstro que se manifesta somente em ambientes selvagens, '
        '\ne em condições extremamente específicas. Dentre equipes de resgate florestais, '
        '\né informalmente considerado como o maior responsável por desaparecimentos misteriosos de grupos de campistas.',
        '\nCarniçal':'Originada de uma tentativa fracassada de dar consciência à entidade da Morte dentro da Realidade, '
        '\no carniçal preto é uma criatura formada de Lodo entrelaçado a partir de um crânio humano apodrecido.'
            }