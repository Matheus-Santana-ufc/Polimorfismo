from criatura import Criatura

class Energia(Criatura):
    def __init__(self, bestiario):
        super().__init__(bestiario)
        self.bestiario = {'\nAnfitrião': 'UMA ENTIDADE PARANORMAL EXTREMAMENTE PODEROSA E COMPLETAMENTE INSANA,\nO ANFITRIÃO É UMA MANIFESTAÇÃO PARANORMAL QUE SE ATRELA A CONSCIÊNCIAS HUMANAS DENTRO DA REALIDADE.\n'
        '\nOBCEADO EM SE DIVERTIR COM A AGONIA E O CAOS, \nO ANFITRIÃO REALIZA DIVERSOS JOGOS COM REGRAS TOTALMENTE IMPREVISÍVEIS A4H4HA4A4 E QUE ESTÃO FORA ATÉ MESMO DO SEU PRÓPRIO CONTROLE.',
        '\nTelopsia': 'Você já deve ter escutado a lenda do filme amaldiçoado: telopsia. Uma fita VHS amaldiçoada que contém uma gravação misteriosa e terrível\n'
        '\ncausando a todos aqueles que a assistiram uma morte aterrorizante pouco tempo depois.\nTodos aqueles que assistiram ao filme eventualmente são encontrados pela criatura.\n'
        '\nEntão, é ela que os assiste, enquanto distorce e desintegra a forma de suas vítimas.\nDelas, resta apenas uma mancha preta no formato de silhueta no local em que morreram.',
        '\nSukkal': 'Uma alma torturada através do fogo, as sukkal se originaram na antiga Suméria como resultado de um processo enlouquecedor\nem que textos eram cravados com brasa ardente em na pele de vítimas,'
        '\nregistrando os feitos e massacres de seu captor.\n',
                          }