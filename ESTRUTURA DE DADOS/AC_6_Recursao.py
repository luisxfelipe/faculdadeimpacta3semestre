# Nome e R.A. da pessoa 1
# Nome e R.A. da pessoa 2 (se feito em dupla)


'''

    RECURSÃO

Damos o nome de FUNÇÃO RECURSIVA a uma função que tem dentro do seu código
uma chamada a ela mesma.

EXEMPLO:
def func(n):
    if (n < 0):
        return
    print(n)
    func(n-1)

Essa função imprime os inteiros de n até 0.
Por exemplo, numa chamada func(3), a saída do programa será
3
2
1
0
'''

'''
EXERCÍCIO 1

Escreva uma função recursiva, chamada intervalo, que recebe dois inteiros,
INICIO e FIM, e imprime todos os inteiros no intervalo de INICIO até FIM.

EXEMPLOS:
intervalo(10, 14) --> imprime:
10
11
12
13
14

intervalo(10, 10) --> imprime:
10

intervalo(2, 1) --> não imprime nada

'''

def intervalo(inicio, fim):
    if inicio > fim:
        return
    print(inicio)
    if inicio <= fim:
        intervalo(inicio+1, fim)

'''
NÚMERO DE COLLATZ

Veja o seguinte processo:
Começando com um determinado inteiro N, o próximo número será um dos dois casos:
    -> N/2, se N é par
    -> 3*N + 1, se N é ímpar

EXEMPLOS:
Se começamos com N = 5, o próximo número é 16
Se começamos com N = 4, o próximo número é 2

Podemos aplicar a mesma regra sucessivas vezes:
26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 -> 4 -> 2 -> 1 -> ...

Observe que, após chegar ao número 1, entramos em "loop" (1 -> 4 -> 2 -> 1 -> ...)

Por isso, vamos sempre TERMINAR a sequência de operações assim que chegar no 1.
_____________________________

Se N é um número inteiro, dizemos que o número de Collatz de N é o número
de passos necessários para que N chegue ao 1 pela primeira vez.

Exemplos:
Collatz(1) = 0, pois 1 já é o próprio 1.
Collatz(2) = 1, pois basta um passo: 2->1
Collatz(26) = 10, pois: 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 
'''

'''
EXERCÍCIO 2

Escreva uma função recursiva, chamada collatz, que recebe um inteiro positivo N
e retorna seu número de Collatz.

EXEMPLOS:
collatz(1) = 0
collatz(26) = 10
collatz(7) = 16

'''


def collatz(n):
    if n < 1:
        return
    print('\nN = ',n)

    passos = 0
    
    if n == 1:
        
        print('\nPassos = ', passos)
        print('\n############################################')
        
        return passos
   

    if n % 2 ==0:
        passos += 1
        print('\nPassos = ', passos)
        collatz(n/2)
    else:
        passos += 1
        print('\nPassos = ', passos)
        collatz((n*3)+1)

'''
Lembre-se que, se temos a lista
lst = [4, 0, 9, -10, -2, 7]

Então a expressão
lst[1:]

É uma lista contendo só do índice 1 em diante de lst, isto é, a lista [0, 9, -10, -2, 7]

'''

'''
EXERCÍCIO 3

Escreva uma função que recebe uma lista e retorna seu menor elemento.
Sua função deve se chamar minimo e tem que ser recursiva.

Não use o comando "max" ou "min" do Python sobre lista.
'''

def minimo(lista):
    pass # trocar essa linha pelo código da função

'''
EXERCÍCIO 4

Escreva uma função, chamada minmax, que recebe uma lista e retorna uma TUPLA
contendo o elemento mínimo e o elemento máximo da lista.
Sua função deve ser recursiva.

Não use o comando "max" ou "min" do Python sobre lista.

EXEMPLOS:
minmax([1,2,3]) = (1, 3)
minmax([49, 1, 6, 10]) = (1, 49)

'''

def minmax(lista):
    pass


'''
EXERCÍCIO 5

Escreva uma função recursiva que recebe uma lista e um elemento alvo, e retorna
True, se o elemento está na lista; e False, caso contrário.

EXEMPLOS:
busca([1,2,3], 2) --> retorna True
busca([], 49) --> retorna False

Não use comando do tipo "x in lista" do Python.
'''

def busca(lista, alvo):
    pass

'''
EXERCÍCIO 6

Escreva uma função recursiva que recebe uma lista lst e retorna uma nova lista
que é lst com todos os seus elementos DOBRADOS.

EXEMPLOS:
dobra([1,2,3]) --> retorna [2, 4, 6]
dobra(['a', 'b']) --> retorna ['aa', 'bb'])
'''

def dobra(lista):
    pass

'''
EXERCÍCIO 7

Escreva uma função recursiva que recebe uma lista ORDENADA e um elemento alvo,
e realiza a busca binária para encontrar esse alvo.
Sua função retorna True, se encontrar o alvo; False, caso contrário.

Sua função recebe também os índices de início e fim da lista.
Na primeira chamada de todas, esses parâmetros serão 0 e len(lista)-1.

'''

def busca_binaria(lista, alvo, inicio, fim):
    pass

# FIM DA AC. O código abaixo é para os testes automatizados.
# --------------------------------------------------------------------------
import unittest
import sys
import inspect
import hashlib

import io
from contextlib import redirect_stdout

def pega_saida(funcao, entrada):
    f = io.StringIO()
    with redirect_stdout(f):
        funcao(*entrada)
    return f.getvalue()

class TestStringMethods(unittest.TestCase):
    
    def test_01_intervalo(self):
        self.assertEqual(pega_saida(intervalo, (10, 14)), '10\n11\n12\n13\n14\n')
        self.assertEqual(pega_saida(intervalo, (15, 10)), '')
        self.assertEqual(pega_saida(intervalo, (1, 1)), '1\n')
        sys.setrecursionlimit(100)
        
    def test_02_collatz(self):
        self.assertEqual(collatz(1), 0)
        self.assertEqual(collatz(3), 7)
        self.assertEqual(collatz(7), 16)
        self.assertEqual(collatz(10), 6)
        self.assertEqual(collatz(1024), 10)
        self.assertEqual(collatz(65536), 16)

    def test_03_minimo(self):
        self.assertEqual(minimo([1]), 1)
        self.assertEqual(minimo([3, 2, 1]), 1)
        self.assertEqual(minimo([1, 2, 3]), 1)
        self.assertEqual(minimo(list(range(1000, 0, -2))), 2)

    def test_04_minmax(self):
        self.assertEqual(minmax([1]), (1, 1))
        self.assertEqual(minmax([3, 2, 1]), (1, 3))
        self.assertEqual(minmax([1, 2, 3]), (1, 3))
        self.assertEqual(minmax(list(range(1000, 0, -2))), (2, 1000))

    def test_05_busca(self):
        self.assertTrue(busca([1], 1))
        self.assertFalse(busca([1], 0))
        self.assertTrue(busca([3, 2, 1], 3))
        self.assertTrue(busca([3, 2, 1], 1))
        self.assertFalse(busca([3, 2, 1], 0))
        lista = list(range(1000, 0, -2))
        self.assertTrue(busca(lista, 1000))
        self.assertTrue(busca(lista, 2))
        self.assertFalse(busca(lista, 0))

    def test_06_dobra(self):
        self.assertEqual(dobra([0]), [0])
        self.assertEqual(dobra([1]), [2])
        self.assertEqual(dobra([3, 2, 1]), [6, 4, 2])
        self.assertEqual(dobra(list(range(1000, 0, -2))), list(range(2000, 0, -4)))

    def test_07_busca_binaria(self):
        self.assertTrue(busca_binaria([1], 1, 0, 0))
        self.assertFalse(busca_binaria([1], 0, 0, 0))
        self.assertTrue(busca_binaria([1, 2, 3], 1, 0, 2))
        self.assertTrue(busca_binaria([1, 2, 3], 2, 0, 2))
        self.assertTrue(busca_binaria([1, 2, 3], 3, 0, 2))
        self.assertFalse(busca_binaria([1, 2, 3], 0, 0, 2))
        lista = list(range(0, 1000, 3))
        self.assertTrue(busca_binaria(lista, 81, 0, len(lista)-1))
        self.assertTrue(busca_binaria(lista, 729, 0, len(lista)-1))
        self.assertFalse(busca_binaria(lista, 400, 0, len(lista)-1))


def runTests(rapido=False):
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=rapido).run(suite)


#---------------------------------------------------------------------------
# para SEMPRE rodar os testes, descomentar uma das linhas de  código abaixo:

# roda TODOS os testes:
#runTests()

# roda só até a primeira falha:
runTests(rapido = True)