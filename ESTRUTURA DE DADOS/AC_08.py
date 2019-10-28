'''
    Vocês já usaram anteriormente a estrutura de dados dicionário do Python.
    O dicionário é comparável à lista, porém seus "índices" (dizemos CHAVES)
    não são necessariamente 0, 1, 2,... podemos usar valores float, valores
    não sequenciais, strings, tuplas, etc.

    (Qualquer item "hasheável" pode ser chave.)

'''

'''
EXERCÍCIO 1

Crie na variável "dicio" um novo dicionário com o seguinte conteúdo:
Chave 'idade' contém o número 19;
Chave 'altura' contém o valor 1.81;
chave 'curso' contém o valor 'arquitetura'.

Você pode criar tudo de uma vez ou simplesmente criar um dicionário vazio para
depois adicionar item por item.
Basta que ao final do programa a variável contenha o dicionário esperado.

'''

dicio = {'idade':19,'altura':1.81,'curso':'arquitetura'}
'''
EXERCÍCIO 2

Crie um novo dicionário, dicio2, que contém todos os itens de dicio
exceto o item "altura".
'''

dicio2 = {'idade':19,'curso':'arquitetura'}


'''
EXERCÍCIO 3

Escreva uma função que recebe um dicionário e imprime todos os pares de chave
e valor existentes na estrutura.

Exemplo:
exibe(dicio2) deverá imprimir
idade 19
curso arquitetura

'''

def exibe(dicionario):
    for chave in dicionario:
        print(chave, dicionario[chave])


'''
Explicação:

O dicionário oferece um método "get" para acessar o valor indexado por uma
determinada chave.

Exemplo:
dicio2.get('curso') --> retorna 'arquitetura'

A vantagem do get é que ele oferece um parâmetro opcional "default".
Se a chave pedida não existe no dicionário, é retornado o valor default.

Exemplo:
dicio2.get('curso', 'nada') --> retorna 'arquitetura', pois é o valor indexado pela chave 'curso'
dicio2.get('trabalho', 'nada') --> retorna 'nada', pois nesse dicionário não há chave 'trabalho'

'''

'''
EXERCÍCIO 4

Escreva uma função similar ao método get, chamada "acessa".
Sua função recebe três parâmetros: um dicionário, uma chave e um valor default.

acessa(dicionario, chave, default) deve retornar exatamente o mesmo que a chamada
dicionario.get(chave, default).

Ver exemplos na explicação acima.
'''

def acessa(dicionario, chave, default):
    return dicionario.get(chave,default)

'''
EXERCÍCIO 5

Podemos calcular o hash de um objeto x fazendo a chamada:
hash(x).

Quando temos um valor inteiro VAL e queremos limitá-lo para o intervalo de
0 até um determinado número MAX, podemos usar a expressão:

VAL & MAX,

Que realiza a operação "and" bit a bit entre VAL e MAX.

Se temos um dicionário com determinado tamanho N, o valor efetivo
que a chave x teria como índice na tabela de hash tem que ser de 0 até N-1.

Escreva uma função que recebe um objeto x e o tamanho n de um dicionário,
e retorna o índice efetivo que x teria como chave no dicionário.
'''

def indice_dicionario(x, n):
    return hash(x) & n-1


'''
Explicação

Um dicionário pode ser usado para fornecer uma "tabela de dependêcias".
Por exemplo, dependências de disciplinas na faculdade.

Para fazer Cálculo 3, preciso primeiro fazer Cálculo 2 e Vetores.
Para fazer Cálculo 2, preciso primeiro fazer Cálculo 1.
Para fazer Cálculo 1, não há pré-requisito.
Para fazer Vetores, não há pré-requisito.

Isso pode ser representado pelo dicionário a seguir:

dependencias = {
    'calculo3' : ['calculo2', 'vetores']
    'calculo2' : ['calculo1']
}

(As disciplinas sem dependência não precisam ser citadas.)

Note que, ao total, cálculo 3 acaba tendo TRÊS pré-requisitos efetivos:
cálculo 1, cálculo 2 e vetores.

Isso porque cálculo 1 não é citado diretamente mas é requisito indireto.

'''
'''
EXERCÍCIO 6

Escreva uma função que recebe um dicionário de dependências como no
exemplo acima e uma matéria desejada.
Imprime todas as dependências DIRETAS da disciplina, uma por linha.

Assim, a chamada
mostra_dependencias_diretas(dependencias, 'cálculo3')

irá imprimir
cálculo2
vetores

'''

def mostra_dependencias_diretas(dicionario, materia):

    
    dependencias = dicionario[materia]

    print(dependencias[0])
    print(dependencias[1])
    
'''
EXERCÍCIO 7

Escreva uma função que recebe um dicionário de dependências como no
exemplo acima e uma matéria.
A função deve imprimir TODAS as dependências da matéria, inclusive calculando as indiretas.
(As matérias devem ser impressas uma por linha.)

No exemplo dado no exercício anterior, 'calculo3' depende diretamente de 'calculo2' e de 'vetores'.
Mas, como 'calculo2' depende de 'calculo1', então 'calculo1' também está entre as dependências de 'calculo3'.

Obs.: pode haver uma "profundidade" arbitrária de dependências.
Exemplo:

'geometria_diferencial' depende de 'análise_complexa' e de 'topologia'
'análise_complexa' depende de 'análise_real'
'análise_real' depende de 'cálculo1'
etc...

Assim, se temos um dicionário de dependências como a seguir:
dependencias_complicado = {
    'geometria_diferencial' : [ 'análise_complexa', 'topologia' ],
    'análise_complexa' : [ 'análise_real' ],
    'análise_real' : [ 'cálculo1' ]
}


a chamada mostra_dependencias(dependencias_complicado, 'geometria_diferencial')
deverá imprimir a saída:
cálculo1
análise_real
análise_complexa
topologia

(É permitido que a saída seja em outra ordem)

'''
'''
def mostra_dependencias(dicionario, materia):

    dependencias = dicionario[materia]
    dic = {}
    for teste in dependencias:
        dic[dependencias.index(teste)] = teste

    teste = {}

    

    for chave in dependencias:
        print(chave)
    if acessa(dic, dependencias[0], 'nada') != 'nada':
        mostra_dependencias(dependencias, dependencias[0])
'''

# dica: esse exercício fica complicado se você não usar recursão.
def mostra_dependencias(dicionario, materia):

    dependencias = dicionario[materia]
    dic = {}
    for teste in dependencias:
        dic[dependencias.index(teste)] = teste

    teste = {}

    

    for chave in dependencias:
        print(chave)
    if acessa(dic, dependencias[0], 'nada') != 'nada':
        mostra_dependencias(dependencias, dependencias[0])

    


    '''
    dependencias = dicionario[materia]

    depende = True

    while depende == True:
        mat = dependencias[0]
        if dependencias[0] in dicionario:
            dependencias.insert(0, dicionario[dependencias[0]])

        else:
            depende = False

    for dependencia in dependencias:
        print(dependencia)
'''
    '''
    for materia in dicionario - 1:
'''
    
    '''
    dependencias = dicionario[materia]

    dependenciasExtras = []

    dependenciasExtras.insert(0, dependencias.pop())
    dependenciasExtras.insert(0, dependencias.pop())

    dependenciasExtras.insert(0, 'teste')
 

    for valor in dependenciasExtras:
        print(valor)
        '''
    '''
    lst = []

    lst.append(dicionario[materia])
'''



    
    '''
    while depende == True:
'''



# FIM DA AC. O código abaixo é para os testes automatizados.
# --------------------------------------------------------------------------
import unittest
import sys
import inspect
import hashlib

import io
from contextlib import redirect_stdout

def pega_saida(funcao, *entrada):
    f = io.StringIO()
    with redirect_stdout(f):
        funcao(*entrada)
    return f.getvalue()

class TestStringMethods(unittest.TestCase):

    
    def test_01_var_dicio(self):
        self.assertEqual(dicio, {'idade':19,'altura':1.81,'curso':'arquitetura'})

    def test_02_var_dicio2(self):
        self.assertEqual(dicio2, {'idade':19,'curso':'arquitetura'})

    def test_03_exibe(self):
        self.assertEqual(pega_saida(exibe,{'a':1,'b':2}), "a 1\nb 2\n")
        self.assertEqual(pega_saida(exibe,{1:'teste'}), "1 teste\n")

    def test_04_acessa(self):
        dicio = {'faculdade': 'impacta', 'materia': 'ED', 'semestre': 3}
        self.assertEqual(acessa(dicio, 'faculdade', 'teste'), 'impacta')
        self.assertEqual(acessa(dicio, 'curso', 0), 0)
    
    def test_05_indice_dicionario(self):
        self.assertEqual(indice_dicionario(8, 15), 8)
        self.assertEqual(indice_dicionario(90, 15), 10)
        self.assertEqual(indice_dicionario(170, 256), 170)
        self.assertEqual(indice_dicionario(500, 256), 244)
        self.assertEqual(indice_dicionario(10239, 2048), 2047)
    
    
    def test_06_dependencias_diretas(self):
        simples = {
            'calculo3' : ['calculo2', 'vetores'],
            'calculo2' : ['calculo1']
        }
        complicado = {
            'geometria_diferencial' : [ 'analise_complexa', 'topologia' ],
            'analise_complexa' : [ 'analise_real' ],
            'analise_real' : [ 'calculo1' ]
        }
        s1 = pega_saida(mostra_dependencias_diretas, simples, 'calculo3')
        s2 = pega_saida(mostra_dependencias_diretas, complicado, 'geometria_diferencial')
        self.assertEqual(sorted(s1.split()), ['calculo2', 'vetores'])
        self.assertEqual(sorted(s2.split()), ['analise_complexa', 'topologia' ])
    
    def test_07_dependencias(self):
        simples = {
            'calculo3' : ['calculo2', 'vetores'],
            'calculo2' : ['calculo1']
        }
        complicado = {
            'geometria_diferencial' : [ 'analise_complexa', 'topologia' ],
            'analise_complexa' : [ 'analise_real' ],
            'analise_real' : [ 'calculo1' ]
        }
        tamanho = 9 
        profundo = {}
        for i in range(tamanho):
            profundo[i] = [i+1]
        s1 = pega_saida(mostra_dependencias, simples, 'calculo3')
        s2 = pega_saida(mostra_dependencias, complicado, 'geometria_diferencial')
        s3 = pega_saida(mostra_dependencias, profundo, 0)
        self.assertEqual(sorted(s1.split()), ['calculo1', 'calculo2', 'vetores' ])
        self.assertEqual(sorted(s2.split()), ['analise_complexa', 'analise_real', 'calculo1', 'topologia' ])
        self.assertEqual(sorted(s3.split()), (list(map(str,list(range(1,tamanho+1))))))
        
def runTests(rapido = False):
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=rapido).run(suite)


#---------------------------------------------------------------------------
# para SEMPRE rodar os testes, descomentar uma das linhas de  código abaixo:

# roda TODOS os testes:
#runTests()

# roda só até a primeira falha:
runTests(rapido = True)
