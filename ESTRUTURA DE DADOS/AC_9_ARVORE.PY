# Nome e R.A. da pessoa 1
# Nome e R.A. da pessoa 2 (se feito em dupla)

'''
Uma árvore é uma estrutura recursiva.

Cada elemento em uma árvore é um NÓ (NODE).
Cada nó pode ter filhos (outros nós) e exatamente um pai. Existe sempre um nó
que não é filho de ninguém (isto é, não tem pai). Esse nó é chamado de RAIZ.

Podemos dizer que cada filho de um determinado nó é a raiz de sua própria
"sub-árvore".

______________________________________________________________________

Estamos, nesse contexto, usando a árvore como uma estrutura de dados.
Portanto, cada nó irá armazenar um dado. Esse dado pode ser o que bem
desejarmos: um inteiro, um float, uma string, uma lista...

______________________________________________________________________

Nesta atividade iremos trabalhar primariamente com ÁRVORES BINÁRIAS.
Em uma árvore binária, a cada nó é permitido ter NO MÁXIMO DOIS FILHOS.

Costumamos chamar esses dois filhos de "filho esquerdo" e "filho direito".


Na implementação de árvore que você encontra abaixo, cada objeto da classe
representa um NÓ, e contém:

    - Um atributo "dado", que é o dado armazenado nesse nó

    - Um atributo "filhoEsq", que é o filho esquerdo do nó.
    Essa variável tem valor None caso o nó não tenha filho esquerdo.
    
    - Um atributo "filhoDir", que é o filho direito do nó.
    Essa variável tem valor None caso o nó não tenha filho direito.

'''

class Arvore:
    # construtor recebe o dado a ser armazenado e, opcionalmente, filhos
    # esquerdo e direito do nó.
    def __init__(self, dado, esquerdo=None, direito=None):
        self.filhoEsq = esquerdo
        self.filhoDir = direito
        self.dado = dado

    def altera_dado(self, novo_dado):
        self.dado = novo_dado

    def folha(self):
        if self.filhoEsq == None and self.filhoDir == None:
            return True
        else:
            return False

    def mostra_in_ordem(self):
        print(self.dado)
        if (self.filhoEsq is not None):
            self.filhoEsq.mostra_in_ordem()
        if (self.filhoDir is not None):
            self.filhoDir.mostra_in_ordem()

    def mostra_pre_ordem(self):
               
        if (self.filhoEsq is not None):
            self.filhoEsq.mostra_pre_ordem()
        
        print(self.dado)
        
        if (self.filhoDir is not None):
            self.filhoDir.mostra_pre_ordem()
        
        
        
'''
Exercício 1:
    Faça com que a variável "arvore1" abaixo receba uma nova instância da
    classe Árvore. O dado deve ser 'teste' e o nó não deve ter filho
    esquerdo nem filho direito.

    Faça com que a variável "arvore2" abaixo receba uma nova instância da
    classe Árvore. O dado deve ser 'raiz' e o nó deve ter arvore1 como
    filho esquerdo e nenhum filho direito.
'''

arvore1 = Arvore('teste')
arvore2 = Arvore('raiz', arvore1)

'''
Exercício 2:
    Veja a seguinte representação de uma árvore:
                        5
                    2       9
                  1   3   7

    Onde a raiz tem o dado 5;
    Seu filho esquerdo tem o dado 2 e seu filho direito tem dado 9;
    O filho com dado 2 tem filhos com dados 1 e 3;
    O filho com dado 9 tem filho esquerdo com dado 7.

    Faça a série de instanciações necessárias para que a variável "BST"
    abaixo represente essa árvore. (A variável BST vai ser a raiz, isto é,
    deverá conter o dado 5 e os filhos são os nós contendo 2 e 9, etc.)

    DICA: você irá escrever várias instanciações e a BST será a última
    variável a ser instanciada.
'''

# insira aqui as várias instanciações...
aarvore1 = Arvore(1)
aarvore2 = Arvore(3)
aarvore3 = Arvore(7)
aarvore4 = Arvore(2, aarvore1, aarvore2)
aarvore5 = Arvore(9, aarvore3)
BST = Arvore(5, aarvore4, aarvore5)


'''
Exercício 3:
    Lembre-se do conceito de FOLHA: é um nó que não tem filhos.

    Crie na classe Árvore um método chamado "folha".

    Uma chamada do tipo
    x.folha()
    deve retornar True, se x é uma folha, e False, caso contrário.
'''

# o exercício 3 é um método a ser escrito na classe Árvore.

'''
Exercício 4:

    Existem várias formas de exibir na tela todo o conteúdo de uma árvore de
    forma sequencial.

    Note que, na classe fornecida Árvore, existe um método "mostra_in_ordem".
    Esse método imprime o conteúdo da árvore inteira seguindo os seguintes
    passos:

    1) Imprime o dado da raiz;
    2) Imprime recursivamente a sub-árvore à esquerda;
    3) Imprime recursivamente a sub-árvore à direita.

    Para a seguinte árvore:
            10
        9        6


    Esse método iria imprimir o conteúdo assim:
    10
    9
    6

    Para a árvore BST do exercício 2, esse método iria imprimir
    o conteúdo assim:
    5
    2
    1
    3
    9
    7

    ________________________

    Existe outro modo de imprimir o conteúdo de uma árvore: o método
    PRÉ-ORDEM (existe ainda o pós-ordem, que não veremos).

    No MÉTODO PRÉ-ORDEM, exibimos o conteúdo assim:

    1) Imprime a sub-árvore esquerda (recursivamente);
    2) Imprime o dado da raiz;
    3) Imprime a sub-árvore direita (recursivamente).

    Ou seja, é igual ao in-ordem, porém trocando o passo 1 e 2 de ordem.
    Escreva NA CLASSE um método "mostra_pre_ordem", que implementa esse método
    de exibição da árvore.
'''

# o exercício 4 é um método a ser escrito na classe Árvore.

'''
Exercício 5:
    Vamos usar agora o conceito de BST -- Binary Search Tree.
    (Ou ABB -- Árvore Binária de Busca)

    Lembre que uma BST (ABB) é uma árvore com as seguintes regras:
        1) Para todo nó, sua sub-árvore esquerda (se existir) tem que ter dados MENORES.
        2) Para todo nó, sua sub-árvore direita (se existir) tem que ter dado MAIORES.

    O que acontece quando mostramos uma BST pelo método pré-ordem decrito
    no exercício anterior?
    
    Mostre, em forma de lista, em qual ordem são mostrados os nós da árvore
    BST que você criou no Exercício 2.
'''

saida_BST_pre_ordem = [1,2,3,5,7,9]

'''
EXPLICAÇÃO
    Vimos em aula que existe uma correspondência entre uma lista ordenada
    e uma BST (também chamada ABB -- árvore binária de busca).

    Quando nossa ávore é uma BST, podemos realizar nela uma busca que equivale
    à busca binária em uma lista ordenada. Assim, realizamos a busca examinando
    apenas um número pequeno de nós (assim como a busca binária examina poucos
    itens da lista).
'''

'''
Exercício 6:
    Imagine que vamos realizar uma busca binária na árvore que você montou
    no exercício 2 com alvo igual a 4.

    Mostre, na lista, abaixo, quais nós são visitados por essa busca.
    Você deve respeitar a ordem! Portanto, o primeiro visitado será a raiz, etc...
'''

visitados_BST_alvo_4 = [5,2,3]

'''
EXPLICAÇÃO:

    A função abaixo recebe como parâmetro uma lista ordenada e retorna
    a BST correspondente.

    Ou seja, a função realiza a correspondência entre lista ordenada e
    BST de forma concreta.
'''


#------------------------------------------------------------------------------
# A função abaixo recebe uma lista ordenada e retorna a BST correspondente.

def para_BST(lista):
    def paraBSTrec(lista, ini, fim):

        # se a lista é vazia, a árvore é vazia
        if (ini > fim):
            return None
        meio = (ini + fim)//2
        dado_raiz = lista[meio]                 # o dado da raiz é o elemento que está no meio da lista
        fesq = paraBSTrec(lista, ini, meio-1)   # cria recursivamente a subárvore esquerda
        fdir = paraBSTrec(lista, meio+1, fim)   # cria recursivamente a subárvore direita

        return Arvore(dado_raiz, fesq, fdir)    # cria e retorna a raiz
    
    ini = 0
    fim = len(lista) - 1

    return paraBSTrec(lista, ini, fim)
#------------------------------------------------------------------------------

'''
Exercício 7:
    Uma chamada 

    para_BST([1, 2, 3])

    gera a árvore com raiz 2, filho esquerdo 1 e filho direito 3:
            2
        1       3

    Mostre qual lista gera uma árvore igual à BST abaixo:
             8
        5        10
      1   6    9    15
'''

gera_BST = [1,5,6,8,9,10,15]

'''
Exercício 8:
    Escreva uma função busca_na_BST, que recebe a raiz de uma BST e um alvo,
    retornando True, se o elemento existe na árvore, e False caso contrário.
'''

def busca_na_BST(arvore, alvo):

    '''
    print('\nNova arvore visitada')
    print('\nDado e alvo: ',arvore.dado, ', ', alvo)
    '''

    if arvore.dado == alvo:
        '''
        print('\nAchei o alvo: ', alvo)
        '''
        return True
    
    else:
        '''
        print('\nDado não é o alvo')
    
        print('\nfolha: ', arvore.folha)
        '''
        if arvore.filhoEsq is None and arvore.filhoDir is None:
            '''
            print('\nNão achei o alvo: ', alvo)
            '''
            return False
        
        else:
            '''
            print('\nArvore não é folha')
            '''

            if arvore.filhoEsq is None and arvore.filhoDir is not None or arvore.filhoDir is None and arvore.filhoEsq is not None:
                '''
                print('\nArvore contem apenas 1 filho')
                '''

            f_filho_esquerdo = arvore.filhoEsq

            f_filho_direito = arvore.filhoDir

            resporta = None

            if arvore.dado < alvo:
                '''
                print('\nFilho direito visitado')
                print('\nDado do filho: ',f_filho_direito.dado)
                '''
                resporta = busca_na_BST(f_filho_direito, alvo)

            else:
                '''
                print('\nFilho esquerdo visitado')
                print('\nDado do filho: ',f_filho_esquerdo.dado)
                '''
                resporta = busca_na_BST(f_filho_esquerdo, alvo)

            if resporta == True:
                    return True
            else:
                return False

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

def arvores_iguais(T1, T2):
    if (T1 is None or T2 is None):
        return (T1 is None and T2 is None)
    if (T1.dado != T2.dado):
        return False
    return arvores_iguais(T1.filhoEsq, T2.filhoEsq) and arvores_iguais(T1.filhoDir, T2.filhoDir)

class TestStringMethods(unittest.TestCase):

    def verifica_conteudo(self, resposta_dada, codigo_correto):
        codigo_resposta = hashlib.sha224(str(resposta_dada).encode('utf-8')).hexdigest()
        self.assertEqual(codigo_resposta, codigo_correto)
 

    def test_01_arvore1_e_arvore2(self):
        self.assertTrue(type(arvore1) is Arvore)
        self.assertTrue(type(arvore2) is Arvore)
        self.assertEqual(arvore1.dado, 'teste')
        self.assertEqual(arvore2.dado, 'raiz')
        self.assertTrue(arvore1.filhoEsq is None)
        self.assertTrue(arvore1.filhoDir is None)
        self.assertEqual(arvore2.filhoEsq, arvore1)
        self.assertTrue(arvore2.filhoDir is None)

    def test_02_var_BST(self):
        ref = para_BST([1,2,3,5,7,9,10])
        ref.filhoDir.filhoDir = None
        self.assertTrue(arvores_iguais(BST, ref))

    def test_03_folha(self):
        f = Arvore(1)
        self.assertTrue(f.folha())
        self.assertFalse(Arvore(2, f, None).folha())

    def test_04_mostra_pre_ordem(self):
        T1 = para_BST([3, 2, 1])
        s1 = pega_saida(Arvore.mostra_pre_ordem, T1)
        self.assertEqual(s1.split(), ['3', '2', '1'])
        T2 = para_BST(list(range(10)))
        s2 = pega_saida(Arvore.mostra_pre_ordem, T2)
        self.assertEqual(s2.split(), list(map(str,list(range(10)))))
    
    def test_05_saida_pre_ordem(self):
        self.verifica_conteudo(saida_BST_pre_ordem, '48fd1313b91cb1556adee68e73310fd33eafceff3e6477c7ca308698')
    
    def test_06_visitados_BST(self):
        self.verifica_conteudo(visitados_BST_alvo_4, 'ce5a85cd2d03c2f3180c799ad4834dac8f45eef65a127f0243dd8602')
    
    def test_07_gera_BST(self):
        self.verifica_conteudo(gera_BST, 'f407785808e6ee23573ba843f348a33b45d0e51cfd8b88e5dc77e59f')

    def test_08_busca_na_BST(self):
        T1 = para_BST([1, 2, 3, 4, 5, 6, 7])
        self.assertTrue(busca_na_BST(T1, 4))
        self.assertTrue(busca_na_BST(T1, 7))
        self.assertFalse(busca_na_BST(T1, 0))
        T2 = para_BST(list(range(1000)))
        self.assertTrue(busca_na_BST(T2, 400))
        self.assertTrue(busca_na_BST(T2, 999))
        self.assertFalse(busca_na_BST(T2, 1000))



def runTests(rapido = False):
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=rapido).run(suite)


#---------------------------------------------------------------------------
# para SEMPRE rodar os testes, descomentar uma das linhas de  código abaixo:

# roda TODOS os testes:
#runTests()

# roda só até a primeira falha:
runTests(rapido = True)