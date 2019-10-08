

import jogadores
import herois
import itens
import itens_do_heroi
from jogadores import JogadorNaoExisteException
from herois import HeroiNaoExisteException
from itens import ItemNaoExisteException
from itens_do_heroi import ItensNaoExisteException

'''
1) Examine o banco de dados no site https://sqliteonline.com/.
O arquivo é rpg.original.db, e você pode subir ele ao site
usando file > opendb
Depois pode fazer varias consultas

2) Examine as funcoes do arquivo jogador.py, que ilustra como
podemos usar o sql no python com sqlite.

3) Sobre o sqlite:
    Voce deve manipular e consultar apenas o arquivo rpg.db
    Jamais manipule o arquivo rpg.original.db no seu programa,
    pois ele serve para termos um ponto de partida confiavel
    para os testes

    Voce nao deve enviar os arquivos sqlite ao submeter sua AC

4) Sobre os arquivos .py
    O arquivo model.py é o arquivo principal. Nesse arquivo,
    nao é permitido usar o sqlite ou escrever codigo sql

    O sql e o sqlite devem ser usados em:

        herois.py
        itens_do_heroi.py
        itens.py
        jogadores.py

    A idéia é que o models implemente a lógica do modelo (por exemplo,
    o que é um heroi Overpower?) e os demais implementem as leituras
    e escritas no banco de dados.

'''


'''
Nesse arquivo, crie uma função jogador_por_email, que consulta
o banco de dados e devolve o jogador que tem um 
determinado email, dando JogadorNaoExisteException
se nenhum jogador tiver esse email. Lembre-se que
o sqlite deve ser usado no jogador.py, e esse arquivo
deve acessar o jogador.py
'''

def jogador_por_email(email):
    return jogadores.consultar_jogador_por_email(email)

'''
crie e importe um arquivo herois.py
que contem uma funcao consultar_heroi.
ela recebe uma id de heroi e retorna 
um dicionario com todos os dados do heroi
(por exemplo, a chave 'nome' conterá o valor
da coluna 'nome' associada a essa id).

se receber uma id invalida, a funcao levanta 
uma HeroiNaoExisteException (que voce deverá
criar)
'''

'''
crie e importe um arquivo itens.py
que contem uma funcao consultar_item.
ela recebe uma id de item e retorna 
um dicionario com todos os dados do item
(por exemplo, a chave 'nome' conterá o valor
da coluna 'nome' associada a essa id).

se receber uma id invalida, a funcao levanta 
uma ItemNaoExisteException (que voce deverá
criar)
'''

'''
Crie e importe um arquivo itens_do_heroi
com uma funcao consulta_itens_por_heroi, que recebe 
uma id de heroi e retorna uma lista de todas as linhas
da tabela ItemDoHeroi em que a id do heroi é igual à 
recebida.

A assinatura da funcao deve ser a seguinte:
def consulta_itens_por_heroi(idHeroi):

O retorno deve ser uma lista, com as linhas da tabela ItemDoHeroi,
cada uma das linhas representada por um dicionario, com as chaves
id, idHeroi e idItem

'''

'''
Nesse arquivo, crie uma função lista_itens_do_heroi, que recebe uma id
de heroi e devolve uma lista com os dicionarios representando
os itens que pertencem a esse heroi.

A assinatura da funçao:
def lista_itens_do_heroi(idHeroi):

O retorno é uma lista com varios dicionarios, um para cada item. Cada
dicionario tem os dados do item, como ja fizemos antes
'''
'''
Agora, criemos uma nova função, que lista apenas os itens em uso.

Um item está em uso quando o valor da coluna emUso é 1.
Se for 0, o heroi tem o item mas não está usando.

A assinatura da função será:
def lista_itens_em_uso_do_heroi(idHeroi):
'''

'''
Crie uma funcao heroi_pronto_por_nome, que recebe um nome de heroi
e retorna um dicionario com os dados desse heroi.
'''

'''
Melhore sua função heroi_pronto_por_nome: agora, os dados do dicionario
incluem os itens em uso. Se o heroi está usando um item que aumenta
suas habilidades, as habilidades que aparecem no dicionario serão
as do heroi, aumentadas de acordo com o item

Por exemplo, considere um heroi com agilidade 2 e um item de agilidade 3
para ele, o dicionario devera reportar agilidade 5 (desde que o item
esteja em uso. Itens que pertencem ao heroi mais não estão em uso
não afetam as estatisticas).
'''

'''
Melhore sua funcao heroi_pronto_por_nome. Agora, o dicionario também
incluirá o a chave vida. O valor da vida de um heroi é inicializado
com seu fisico multiplicado por 10
'''

'''
Chegou a hora de fazer um ataque!

A função atacar_com fisico recebe dois dicionarios, de dois herois. 
(esses dicionarios sao os gerados pela funcao heroi_pronto_por_nome)

O primeiro heroi é o atacado e o segundo é o defensor

O defensor perde vida. A perda é igual ao atributo fisico do atacante.

O retorno não importa, o que importa é alterar o dicionario do defensor

Se você quiser, pode usar a funcao mensagem de ataque fisico para
dar uns prints simpaticos avisando quanto de dano o defensor tomou.

Essa função já está definida, mais abaixo, mas você pode trocar as
mensagens de ataque por coisas mais interessantes, se quiser.

Esses prints nao serão corrigidos, é só pela diversão mesmo
'''

'''
A função atacar_com_magia faz o mesmo, mas agora o dano do
defensor é o atributo magia do atacante.

Repare que a vida nunca pode ficar negativa. O mínimo é 0.
'''

'''
Façamos um upgrade nas nossas funções de ataque: se o atacante
for muito mais rápido que o defensor, poderá atacar duas vezes

Para isso, divida agilidade do atacante pela agilidade do defensor,
arredondando para baixo.

Se der algum número maior que 1, esse é o número de ataques
que o atacante vai conseguir fazer.

Se der 1 ou menos, o atacante conseguirá fazer exatamente 1 ataque.

Fazer um ataque 2 vezes significa dar duas vezes o dano:
Se harry tem 7 de magia e vai atacar 2 vezes, dará 14 de dano
'''

'''
Nesse arquivo, faça uma funcao criar heroi, que recebe
o nome e os atributos:

def criar_heroi(nome,fisico,agilidade,magia):

Ela deve criar um heroi no banco de dados, com os atributos
dados.

Para isso, ela deve chamar uma funcao no arquivo heroi.py
que usará o sqlite.
'''

'''
Façamos um upgrade em criar_heroi. Se o heroi for poderoso
demais (a soma dos 3 atributos for maior que 20) nossa funcao
criar_heroi devera lançar uma OverpowerException
'''

'''
No arquivo itens.py crie uma funcao nome_para_id_item, que recebe
um nome de item e devolve a id numerica correspondente
'''

'''
no arquivo itens.py, crie uma funcao criar_item, que recebe os atributos
do item e cria um item novo no banco de dados.

Ou seja, uma funcao com a seguinte assinatura:
criar_item(tipo, nome,fisico,agilidade,magia)

repare: omitimos um dos atributos do item, o emUso. Esse atributo
será inicializado sempre com 0, para representar False
'''

'''
Crie uma funcao dar_item_para_heroi, que faz com que o heroi se
torne o dono (ou dona) do item.

Para isso, ela deve chamar uma funcao no arquivo itens_do_heroi,
que você também deverá criar. Lembre-se de manter o
codigo sql apenas no arquivo itens_do_heroi

Alem dessa funcao, para passar o teste relevante, voce precisara
tambem da funcao seguinte (colocar_item_em_uso)
'''

'''
Crie uma funcao colocar_item_em_uso, que recebe o dicionario do
heroi e o dicionario do item, e faz com que o item fique emUso

Para isso, voce deve criar uma funcao no arquivo itens para a manipulacao
do SQL
'''

'''
Façamos um upgrade em colocar_item_em_uso: um item só pode ficar em 
uso se o heroi nao está usando outro item do mesmo tipo

Se tentarmos colocar_item_em_uso em um chapeu quando o heroi já
tem um chapeu em uso, a funcao deve lancar 
o erro HeroiJaUsaEsseTipoDeItemException
'''

'''
O uso das funcoes a seguir é opcional
'''
import random
def mensagem_de_ataque_fisico(dano,nome_atacante,nome_defensor):
    msgs = [f'{nome_atacante} dá um soco em {nome_defensor}, causando {dano} de dano',
          f'{nome_atacante} dá um chute em {nome_defensor}, causando {dano} de dano',
          f'{nome_atacante} ataca {nome_defensor} covardemente, causando {dano} de dano']
    msg = msgs[random.randrange(0,len(msgs)-1)]
    print(msg)

def mensagem_de_ataque_magico(dano,nome_atacante,nome_defensor):
    msgs = [f'{nome_atacante} solta raios contra {nome_defensor}, causando {dano} de dano',
          f'{nome_atacante} congela {nome_defensor}, causando {dano} de dano',
          f'{nome_atacante} transforma {nome_defensor} em um flamingo, causando {dano} de dano']
    msg = msgs[random.randrange(0,len(msgs)-1)]
    print(msg)
'''
Fim das funcoes de uso opcional

Inicio dos testes
'''

import unittest
import hashlib
class TestStringMethods(unittest.TestCase):
    def test_01_jogador_por_email(self):
        self.assertEqual(jogador_por_email('lucas.goncalves@faculdadeimpacta.com.br')['nome'],'lucas goncalves')
        self.assertEqual(jogador_por_email('victor.silva@faculdadeimpacta.com.br')['nome'],'victor')
        self.assertRaises(JogadorNaoExisteException,jogador_por_email,'john@doe')

    def test_02_pega_heroi(self):
        self.assertEqual(herois.consultar_heroi(1)['nome'],'conan')
        self.assertEqual(herois.consultar_heroi(2)['nome'],'merlin')
        self.assertEqual(herois.consultar_heroi(3)['nome'],'harry')
        self.assertRaises(HeroiNaoExisteException,herois.consultar_heroi,50329)

    def test_03_pega_item(self):
        self.assertEqual(itens.consultar_item(1)['nome'],'forca do gigante')
        self.assertEqual(itens.consultar_item(1)['tipo'],'cinto')
        self.assertEqual(itens.consultar_item(2)['nome'],'de alladin')
        self.assertEqual(itens.consultar_item(2)['tipo'],'lampada')
        self.assertRaises(ItemNaoExisteException,itens.consultar_item,329)

    def test_04a_itens_do_heroi(self):
        self.assertEqual(len(itens_do_heroi.consulta_itens_por_heroi(1)),2)
        self.assertEqual(len(itens_do_heroi.consulta_itens_por_heroi(3)),1)
        self.assertEqual(len(itens_do_heroi.consulta_itens_por_heroi(2)),0)
        #self.assertRaises(HeroiNaoExisteException,lista_itens_do_heroi,9999)
        l3=itens_do_heroi.consulta_itens_por_heroi(3)
        item_do_3 = itens.consultar_item(l3[0]['idItem'])
        self.assertEqual(item_do_3['tipo'],'varinha')

    def test_04b_itens_do_heroi(self):
        self.assertEqual(len(lista_itens_do_heroi(1)),2)
        self.assertEqual(len(lista_itens_do_heroi(3)),1)
        self.assertEqual(len(lista_itens_do_heroi(2)),0)
        self.assertRaises(HeroiNaoExisteException,lista_itens_do_heroi,9999)
        l1 = lista_itens_do_heroi(1)
        lista_tipos = [l1[0]['tipo'],l1[1]['tipo']]
        self.assertIn('cinto',lista_tipos)
        self.assertIn('lampada',lista_tipos)

    def test_05_itens_que_heroi_esta_usando(self):
        self.assertEqual(len(lista_itens_em_uso_do_heroi(1)),0)
        self.assertEqual(len(lista_itens_em_uso_do_heroi(3)),1)
        self.assertEqual(len(lista_itens_em_uso_do_heroi(2)),0)
        self.assertRaises(HeroiNaoExisteException,lista_itens_do_heroi,9999)
        l3=lista_itens_em_uso_do_heroi(3)
        item_do_3 = l3[0]
        self.assertEqual(item_do_3['tipo'],'varinha')

    def test_06_status_do_heroi(self):
        self.assertEqual(heroi_pronto_por_nome('conan')['fisico'],3)
        self.assertEqual(heroi_pronto_por_nome('conan')['magia'],2)
        self.assertEqual(heroi_pronto_por_nome('conan')['agilidade'],5)
    
    def test_07_status_alterado_por_itens(self):
        self.assertEqual(heroi_pronto_por_nome('conan')['fisico'],3)
        self.assertEqual(heroi_pronto_por_nome('conan')['magia'],2)
        self.assertEqual(heroi_pronto_por_nome('conan')['agilidade'],5)
        self.assertEqual(heroi_pronto_por_nome('harry')['fisico'],2)
        self.assertEqual(heroi_pronto_por_nome('harry')['agilidade'],4)
        self.assertEqual(heroi_pronto_por_nome('harry')['magia'],7)

    def test_08_vida_do_heroi(self):
        self.assertEqual(heroi_pronto_por_nome('conan')['vida'],30)
        self.assertEqual(heroi_pronto_por_nome('harry')['vida'],20)
    
    def test_09_ataque_fisico(self):
        conan = heroi_pronto_por_nome('conan')
        harry = heroi_pronto_por_nome('harry')
        self.assertEqual(harry['vida'],20)
        atacar_com_fisico(atacante=conan,defensor=harry)
        self.assertEqual(harry['vida'],17)
        atacar_com_fisico(atacante=conan,defensor=harry)
        self.assertEqual(harry['vida'],14)
        atacar_com_fisico(defensor=conan,atacante=harry)
        self.assertEqual(conan['vida'],28)

    def test_10_ataque_magico(self):
        merlin = heroi_pronto_por_nome('merlin')
        harry = heroi_pronto_por_nome('harry')
        self.assertEqual(harry['vida'],20)
        atacar_com_magia(atacante=merlin,defensor=harry)
        self.assertEqual(harry['vida'],12)
        atacar_com_magia(atacante=merlin,defensor=harry)
        self.assertEqual(harry['vida'],4)
        atacar_com_magia(atacante=merlin,defensor=harry)
        self.assertEqual(harry['vida'],0)

    def test_10_ataque_repetido(self):
        merlin = heroi_pronto_por_nome('merlin')
        harry = heroi_pronto_por_nome('harry')
        self.assertEqual(merlin['vida'],30)
        atacar_com_magia(atacante=harry,defensor=merlin)
        self.assertEqual(merlin['vida'],2)
        atacar_com_magia(atacante=harry,defensor=merlin)
        self.assertEqual(merlin['vida'],0)

    def test_11_criar_heroi(self):
        criar_heroi('van damma',fisico=7,agilidade=5,magia=0)
        dama = heroi_pronto_por_nome('van damma')
        self.assertEqual(dama['agilidade'],5)
        self.assertEqual(dama['fisico'],7)
        harry = heroi_pronto_por_nome('harry')
        atacar_com_magia(atacante=harry,defensor=dama)
        self.assertEqual(dama['vida'],63)


    def test_12_criar_overpower(self):
        self.assertRaises(OverpowerException,criar_heroi,'freeza',10,10,10)

    def test_13a_nome_para_id_item(self):
        idDuelo = itens.nome_para_id_item('de duelo')
        duelo = itens.consultar_item(idDuelo)
        self.assertEqual(duelo['nome'],'de duelo')
        idConfortavel = itens.nome_para_id_item('confortavel')
        confortavel = itens.consultar_item(idConfortavel)
        self.assertEqual(confortavel['nome'],'confortavel')


    def test_13_criar_item(self):
        itens.criar_item(tipo='varinha', nome='mestra',fisico=0,agilidade=0,magia=8)
        idMestra = itens.nome_para_id_item('mestra')
        mestra = itens.consultar_item(idMestra)
        self.assertEqual(mestra['nome'],'mestra')
        self.assertEqual(mestra['id'],idMestra)
        self.assertEqual(mestra['magia'],8)

    def test_14_dar_item_para_heroi(self):
        itens.criar_item(tipo='espada', nome='celestial',
                          fisico=3,agilidade=3,magia=3)
        dama = heroi_pronto_por_nome('van damma')
        idCelestial = itens.nome_para_id_item('celestial')
        celestial = itens.consultar_item(idCelestial)
        dar_item_para_heroi(heroi=dama,item=celestial)
        dama = heroi_pronto_por_nome('van damma')
        self.assertEqual(dama['agilidade'],5) #agilidade ainda nao mudou
        colocar_item_em_uso(dama,celestial)
        self.assertEqual(dama['agilidade'],5) #agilidade ainda nao mudou,
        #pois ainda nao fizemos uma nova consulta
        dama = heroi_pronto_por_nome('van damma')
        self.assertEqual(dama['agilidade'],8) #agilidade mudou
        #dama está usando o item e tb fizemos a nova consulta
        print('hey')

    def test_15_heroi_nao_pode_usar_dois_itens_do_mesmo_tipo(self):
        itens.criar_item(tipo='espada', nome='vorpal',
                          fisico=10,agilidade=2,magia=0)
        dama = heroi_pronto_por_nome('van damma')
        idVorpal = itens.nome_para_id_item('vorpal')
        vorpal = itens.consultar_item(idVorpal)
        dar_item_para_heroi(heroi=dama,item=vorpal) #roda sem problemas
        #o que nao pode eh ela usar o item, porque ela ja tem outra varinha
        self.assertRaises(HeroiJaUsaEsseTipoDeItemException,colocar_item_em_uso,dama,vorpal)




import shutil
def runTests():
        shutil.copyfile('rpg.original.db','rpg.db')
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

runTests()
