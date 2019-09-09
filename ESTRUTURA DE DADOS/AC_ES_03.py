
'''Nome e R.A. da pessoa 1'''
#Gustavo Luiz Silva Lima RA:1801471
'''Nome e R.A. da pessoa 2 (se feito em dupla)'''
#Luíz Felipe RA:

'''

    BUSCAS

Já discutimos um pouco no início do semestre sobre o problema de buscar um
dado elemento (digamos, nosso "alvo") dentro de uma lista.

Se o elemento ocorre na lista, queremos um índice em que ele ocorre.
(Por que não "o" índice? Alguém sabe?)
Mas, se o elemento não está na lista, queremos obter algo como False.

EXEMPLO:
    lista = [ 29, 14, 63, 47, 91, 12, 36, 101, 46, 52, 68, 127, 31, 77 ]
    alvo = 47, está na lista? Sim, na posição 3
    alvo = 100, está na lista? Não (False).

'''

'''
EXERCÍCIO 1

Retomando o exemplo, vamos usar a mesma lista e a ideia de perguntar
sobre diferentes alvos. Para cada uma das variáveis a seguir, apague
o None e preencha seu valor adequadamente segundo o exemplo:

    posicao_47 = 3
    posicao_14 = 1
    posicao_100 = None

'''

# trocar None pelos índices adequados, se existirem
# se não existir, deixar o None (não trocar para False ou qualquer outro valor)
posicao_36 = 6
posicao_111 = None
posicao_127 = 11

'''
Lembre-se que, para acessar uma determinada posição da lista, usamos a
seguinte sintaxe:
        NOME_DA_LISTA[índice]

Onde o índice (posição) começa em 0 (zero) para a primeira posição e assim
por diante.

Exemplos:

    > lista = [100, 102, 104, 106, 108, 110, 112, 114, 116, 118]
    > lista[0]
    100
    > lista[1]
    102
    > lista[3]
    106
'''

'''
EXERCÍCIO 2

Escreva uma função na_posicao que recebe uma lista e um índice, e retorna o
valor que está armazenado nessa posição da lista.

Por exemplo: a chamada na_posicao([20, 41, 33], 2) deve retornar 33.

'''

def na_posicao(lista, indice):
    
    return lista[indice]


'''
Veja o código a seguir.
Trata-se de uma função que recebe uma lista e percorre-a toda. Para cada
índice válido da lista. Isto é, desde o índice 0 até o len(lista) - 1.

Para cada índice, a função imprime na tela qual o conteúdo da lista naquele
determinado índice, com uma mensagem do tipo
"na posicao i, temos o numero j"

def imprime_conteudo(lista):
    for i in range(len(lista)):
        print ('na posicao', i, 'temos o numero', lista[i])

'''

'''
EXERCÍCIO 3

Escreva uma função que recebe uma lista e um elemento alvo, e percorrendo
a lista índice por índice, busca o alvo na lista.

A função deve retornar True, se o elemento foi encontrado, e False caso
contrário.
'''

def busca_linear(lista, alvo):
    i=0
    
    for i in range(0, len(lista)):
        
        fotografa(i,lista[i])
        if alvo == lista[i]:
            return True
        
        i += 1
        
    
        
    return False

'''
EXERCÍCIO 4

Faça um upgrade na função busca_linear.
(Você irá alterar o código da função já feita, não escrever uma nova.)

Nesse upgrade, a cada vez que você consultar um índice da lista,
tire uma "fotografia" do índice visitado (isto é, a posição) e de qual é
o elemento encontrado naquela posição.

Lembre-se que "fotografar" significa fazer uma chamada à função "fotografia",
implementada mais abaixo no próprio corpo desse código.

A chamada receberá dois parâmetros: o índice e o elemento presente no
índice. Algo assim:
    fotografa(i, <ELEMENTO NA POSIÇÃO i DA LISTA>)

'''



'''
Para a próxima parte, vamos lembrar como obter a média aritmética entre dois
números.

    Se temos os valores:
        x = 10
        y = 6
    a média entre esses dois será 8.

    Se temos
        x = 12
        y = 18
    a média aritmética entre eles será 15.

Qual o cálculo que encontra esse valor?
Nós somamos os valores e dividimos por 2.
'''

'''
EXERCÍCIO 5(A)

As três variáveis abaixo deverão conter o valor de uma média aritmética
entre dois valores. Estes valores são indicados pelos seus nomes e
nos comentários.

Preencha corretamente as três variáveis.
'''

media_4_6 = None    # preencher com a média exata entre 4 e 6
media_1220_8 = None # preencher com a média exata entre 1220 e 8
media_7_20 = None   # preencher com a média exata entre 7 e 20

'''
Após somar os números, a divisão exata por 2 nos dá a média aritmética
entre os dois.

Em alguns casos, porém, queremos obter a média arredondada para baixo.
Por exemplo, a média entre 3 e 8 é 5.5, mas arredondando para baixo obtemos
o número 5.

Em Python, a divisão arredondada para baixo é obtida com a operação '//',
que difere da divisão comum '/'.

Exemplos que você pode testar no IDLE:
    > (12+20)//2
    16
    > (12+19)/2
    15.5
    > (12+19)//2
    15

'''

'''
EXERCÍCIO 5(B)

Escreva uma função que recebe dois números e calcula a média entre eles,
arredondada para baixo. Isto é, queremos sempre resultado inteiro.
'''

def media(a, b):
    pass # colocar seu código no lugar desse pass

'''
EXERCÍCIO 6

Escreva uma função que recebe uma lista e dois índices, 'ini' e 'fim',
indicando o início e fim da região desejada da lista.

Sua função retorna o valor armazenado na posição central da região desejada
da lista. Isto é, na posição que é a média entre ini e fim.
'''

def no_centro(lista, ini, fim):
    pass # colocar seu código no lugar desse pass



'''
Lembra da busca binária?

Se temos uma lista ORDENADA, e queremos saber se um número está lá,
podemos fazer o seguinte: 

1) Pegamos o numero do meio da lista.
2) Se achamos nosso numero, retornamos True
3) Caso o numero do meio seja maior, so precisamos procurar na parte de
trás da lista (à esquerda do meio)
4) Caso o numero do meio seja menor, so precisamos procurar na parte da
frente da lista (à direita do meio)

-----------
 
Veja o seguinte exemplo:
    - Estou procurando o número 10
    - No meio da lista, encontrei o 30
    - O que faço? Continuo procurando à ESQUERDA
    - Na parte da esquerda, o meio da lista contém 9
    - O que faço? Continuo procurando à DIREITA
    - Agora, encontrei no meio o número 12
    - O que faço? Continuo procurando à ESQUERDA
    - Agora, encontrei no meio o número 10
    - O que faço? Retorno True. Já encontrei o elemento alvo.
'''

'''
EXERCÍCIO 7

Nesse exercício, vamos preencher algumas variáveis com uma simulação
conceitual da busca binária.

Preencha cada variável com a string
'esquerda'
ou
'direita'
conforme for o próximo passo adequado na simulação.

    testar em 3 variaveis, prox_lado1, prox_lado2, prox_lado3
    que terao os valores 'esquerda' ou 'direita'
'''

# Estou buscando o número 50. No meio da lista encontrei 30.
prox_lado1 = None   # preencher com string 'esquerda' ou 'direita'

# Agora no meio da lista encontrei o 71. (Estou buscando 50)
prox_lado2 = None   # preencher com string 'esquerda' ou 'direita'

# Agora no meio da lista encontrei o 44. (Estou buscando 50)
prox_lado3 = None   # preencher com string 'esquerda' ou 'direita'

'''
EXERCÍCIO 8

Escreva uma funcao busca_binaria(lista,procurado)

Implementamos a ideia descrita acima da seguinte forma:
    Comecamos com duas variaveis, ini = 0 e fim = len(lista)-1
    Definimos o meio como (ini + fim)//2
    A cada passo:
        verificamos se lista[meio] é o numero que queremos.
        Se for, ja achamos 
        Se nao for, e o meio for maior, entao podemos pegar um novo fim: meio-1
        Se nao for, e o meio for menor, entao podemos pegar um novo comeco
'''
def busca_binaria(lista, alvo):
    return False

'''
EXERCÍCIO 9:

Dê um upgrade na função escrita acima.
Esse upgrade consiste do seguinte: a cada vez que você visitar um novo
"meio" da lista, tire uma fotografia. Os parâmetros dessa fotografia são
o índice do meio e o elemento que nele se encontra. Exemplo:

fotografa(indice_meio, lista[indice_meio])

Essas fotografias são para garantir que seu algoritmo está passando pelas
posições corretas da lista na busca pelo alvo.
'''

'''
EXERCÍCIO 10:

Escreva uma função busca_binaria_conta_passos, que é exatamente como a função
que você já fez, porém ela retorna uma tupla com duas poisções.
A primeira posição da tupla é exatamente como a da busca binária normal.
A segunda posição informa o número de passos que a busca demorou para terminar.

O número de passos é contado da seguinte forma: cada vez que visitamos um
"meio da lista" para comparar com o alvo, isso conta como um passo.

Exemplo: buscar 3 na lista [3, 5, 9].
Primeiro passo: visita 5, decide ir para esquerda.
Segundo passo: visita 3, elemento foi encontrado!

Retorna a tupla (True, 2), pois foram feitos 2 passos de busca.

Obs.: não é preciso tirar fotografias nessa função.

'''

def busca_binaria_conta_passos(lista, alvo):
    pass

# FIM DA AC. O código abaixo é para os testes automatizados, além da
# implementação da função "fotografa".
# --------------------------------------------------------------------------
import unittest
import sys
import inspect
import hashlib


class TestStringMethods(unittest.TestCase):
    
    def test_001_var_posicao(self):
        self.compara_hash(posicao_36, 6)
        self.compara_hash(posicao_111, None)
        self.compara_hash(posicao_127, 11)

    def test_002_na_posicao(self):
        self.assertEqual(na_posicao([20, 41, 33], 2), 33)
        self.assertEqual(na_posicao([20, 41, 33], 0), 20)
        lista = list(range(0, 100))
        self.assertEqual(na_posicao(lista, 22), 22)
        self.assertEqual(na_posicao(lista, 50), 50)
        self.assertEqual(na_posicao(lista, 99), 99)

    def test_003_busca_linear(self):
        lista = list(range(0, 100))
        self.assertEqual(busca_linear(lista, 10), True)
        self.assertEqual(busca_linear(lista, 70), True)
        self.assertEqual(busca_linear(lista, 99), True)
        self.assertEqual(busca_linear(lista, -1), False)
        self.assertEqual(busca_linear(lista, 100), False)
   
    def test_004_busca_linear_fotografias(self): 
        reseta_fotos()
        lista = list(range(10, 0, -1))
        busca_linear(lista, 8)

        album_correto = [(0, 10), (1, 9), (2, 8)]
        album_fornecido = fotografias

        if (album_correto != album_fornecido):
            print('Sua função passou nos testes, mas as fotografias não!')
            print('Passei a lista [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]')
            print('Estou procurando o elemento 8.')
            explica_erro(album_fornecido, album_correto)
            self.fail('erro nas fotografias.')

    def test_005a_var_medias(self):
        self.compara_hash(media_4_6, 5.0)
        self.compara_hash(media_1220_8, 614.0)
        self.compara_hash(media_7_20, 13.5)

    def test_005b_media(self):
        self.assertEqual(media(1, 3), 2)
        self.assertEqual(media(1, 2), 1)
        self.assertEqual(media(1, -1), 0)
        self.assertEqual(media(1040, 2001), 1520)

    def test_006_no_centro(self):
        self.assertEqual(no_centro([30, 12, 9], 0, 2), 12)
        self.assertEqual(no_centro([30, 12, 9], 2, 2), 9)
        self.assertEqual(no_centro([30, 12, 9], 0, 1), 30)
        lista = list(range(0, 100))
        self.assertEqual(no_centro(lista, 40, 60), 50)
        self.assertEqual(no_centro(lista, 86, 89), 87)

    def test_007_var_prox_lado(self):
        _esq = 'esquerda'
        _dir = 'direita'
        self.compara_hash(prox_lado1, _dir)
        self.compara_hash(prox_lado2, _esq)
        self.compara_hash(prox_lado3, _dir)


    def test_008_busca_funciona(self):
        self.assertEqual(busca_binaria([0,1,2,3,4],2), True)
        self.assertEqual(busca_binaria([0,1,2,3,4],4), True)
        self.assertEqual(busca_binaria([0,1,2,3,4],5), False)
        self.assertEqual(busca_binaria([0,1,2,4,5,6,7,8],2), True)
        self.assertEqual(busca_binaria([0,1,2,4,5,6,7,8],3), False)
        self.assertEqual(busca_binaria([0,1,2,3,4,5,6],4), True)
        self.assertEqual(busca_binaria([0, 1, 2, 3, 4, 9, 10, 11, 12, 25, 32, 54, 56, 67, 72, 76, 87, 89, 100, 112, 400],5),False)

    def test_009_busca_binaria_fotos(self):
        reseta_fotos()
        lista = [ 33, 47, 50, 68, 81, 99, 112 ]
        busca_binaria(lista, 81)

        album_correto = [(3, 68), (5, 99), (4, 81)]
        album_fornecido = fotografias

        if (album_correto != album_fornecido):
            print('Sua função passou nos testes, mas as fotografias não!')
            print('Passei a lista [ 33, 47, 50, 68, 81, 99, 112 ]')
            print('Estou procurando o elemento 81.')
            explica_erro(album_fornecido, album_correto)
            self.fail('erro nas fotografias.')

    def test_010_busca_binaria_conta_passos(self):
        lista = [ 33, 47, 50, 68, 81, 99, 112 ]
        busca = busca_binaria_conta_passos
        self.assertEqual(busca(lista, 81), (True, 3))
        self.assertEqual(busca(lista, 80), (False, 3))
        self.assertEqual(busca(lista, 33), (True, 3))
        self.assertEqual(busca(lista, 47), (True, 2))
        lista = list(range(1000))
        self.assertEqual(busca(lista, 1000), (False, 10))

    def compara_hash(self, elemento1, elemento2):
        codigo1 = hashlib.sha224(str(elemento1).encode('utf-8')).hexdigest()
        codigo2 = hashlib.sha224(str(elemento2).encode('utf-8')).hexdigest()
        self.assertEqual(codigo1, codigo2)
        

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


fotografias = []
def reseta_fotos():
    global fotografias
    fotografias = []

def fotografa(indice, elemento):
    fotografias.append((indice, elemento))

def explica_erro(album1, album2):
    print()

    if len(album1) == 0 and len(album2) > 0:
        print('Você não tirou nenhuma fotografia')
        print('Primeira fotografia esperada:')
        print(album2[0])
        return

    
    tam_do_menor = min(len(album1),len(album2))
    diferentes = [i for i in range(tam_do_menor) if album1[i] != album2[i]]
    if len(diferentes) > 0:
        menor_diferente = min(diferentes)
        print('Suas primeiras ' + str(menor_diferente) + ' fotografias estao certas')
        print('Suas fotografias corretas:')
        for j in range(menor_diferente):
            print(album1[j])
        print('Sua primeira fotografia errada:')
        print(album1[menor_diferente])
        print('Era esperado:')
        print(album2[menor_diferente])
        return

    if len(album1) < len(album2):
        print('Você tirou fotografias a menos')
        print('Voce tirou '+str(len(album1))+ ' fotografias, mas era pra tirar ' + str(len(album2)))
        menor_diferente = len(album1)
        print('Suas primeiras ' + str(menor_diferente) + ' fotografias estao certas')
        print('Suas fotografias corretas:')
        for j in range(menor_diferente):
            print(album1[j])
        print('A primeira fotografia que faltou:')
        print(album2[menor_diferente])

    if len(album1) > len(album2):
        print('Você tirou fotografias a mais')
        print('Voce tirou '+str(len(album1))+ ' fotografias, mas era pra tirar ' + str(len(album2)))
        menor_diferente = len(album2)
        print('Suas primeiras ' + str(menor_diferente) + ' fotografias estao certas')
        print('Suas fotografias corretas:')
        for j in range(menor_diferente):
            print(album1[j])
        print('A primeira fotografia que sobrou:')
        print(album1[menor_diferente])


#---------------------------------------------------------------------------
# para SEMPRE rodar os testes, descomentar linha abaixo:

runTests()


# se você quiser sempre rodar TODOS os testes (não só até primeira falha), usar
# a seguinte chamada:

# runTests(rapido=False)
