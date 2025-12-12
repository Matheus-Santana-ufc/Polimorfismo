from criatura import Criatura

class Sangue(Criatura):
    def __init__(self, bestiario):
        super().__init__(bestiario)
        self.bestiario = {'\nDiabo':'Você com certeza já ouviu falar desse ser conhecido por inúmeros nomes. '
        '\nO Príncipe do Ódio, o Imperador das Aberrações, o Portador do Trono ou o Sangue Encarnado. '
        '\nAquele que rasga a Realidade com sua presença aterrorizante e devoradora.',
        '\nCarente':'A criatura mais famosa do escritor de terror Daniel Hartmann, o carente é uma manifestação paranormal originada de uma história de terror que se tornou popular no mundo todo.'
        '\nÉ uma criatura nascida da inveja de um ser que nunca sentiu amor e, por isso, busca devorar os órgãos de pessoas que já foram mães para consumir o amor que nunca recebeu.',
        '\nQuibungo':'Uma lenda que se originou no oeste do continente africano e cresceu no nordeste brasileiro através de contos para assustar crianças rebeldes, '
        '\ntomando uma forma distorcida e perturbadora através do Sangue, o Quibungo vaga por ambientes selvagens em busca de presas fáceis para devorar.'
        }