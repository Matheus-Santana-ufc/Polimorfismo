from criatura import Criatura
from conhecimento import Conhecimento
from energia import Energia
from sangue import Sangue
from morte import Morte

def processar_elemento(bestiario):
    elemento_paranormal = bestiario({})
    elemento_paranormal.exibir_bestiario()

if __name__ == '__main__':
    while True:
        print('\n---Bestiário Paranormal---\n1.Conhecimento\n2.Energia\n3.Morte\n4.Sangue')
        opcao = input('Escolha qual elemento de criaturas deseja ver: ').lower()
        if opcao == 'conhecimento':
            processar_elemento(Conhecimento)
        elif opcao == 'energia':
            processar_elemento(Energia)
        elif opcao == 'sangue':
            processar_elemento(Sangue)
        elif opcao == 'morte':
            processar_elemento(Morte)
        else:
            break