from criatura import Criatura

class Conhecimento(Criatura):
    def __init__(self, bestiario):
        super().__init__(bestiario)
        self.bestiario = {'\nMáscara do Desespero': 'Uma máscara indestrutível que contém toda a verdade do Outro Lado, '
        '\num semblante desesperado e permanente que esconde os segredos incompreensíveis, as memórias de tudo que já existiu, '
        '\na lucidez de todas as explicações, todas as respostas… todo o Conhecimento.','\nAnjo': 'Um Anjo é uma manifestação Paranormal de Conhecimento com complemento de Medo extremamente impactante '
        '\nque pode se revelar a partir de uma Transcendência espontânea. '
        '\nA experiência de encontrar um Anjo é inesquecível, indescritível, reveladora e, ao mesmo tempo, aterrorizante. '
        '\nUm encontro com essa criatura é tão extremo que ela pode desmantelar a mente de qualquer um que a observe instantaneamente, '
        '\nderretendo seus olhos como se fossem lágrimas douradas.',
        '\nEstrangeiro':
        '\nO ser nomeado Estrangeiro é uma manifestação paranormal muitíssimo inteligente, '
        '\ncom motivações complexas e misteriosas. Ao contrário de muitas criaturas, '
        '\no Estrangeiro parece ter desenvolvido algum tipo de linguagem própria e '
        '\ntambém parece ser capaz de aprender novas linguagens.'
        }
