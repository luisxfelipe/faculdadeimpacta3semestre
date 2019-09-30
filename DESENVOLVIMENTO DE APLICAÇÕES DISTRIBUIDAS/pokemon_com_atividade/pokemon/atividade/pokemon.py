from requests import api
from dataclasses import dataclass

"""
Instruções para TODOS os exercícios/funções abaixo:
1. Veja as instruções de como instalar e executar o PokeAPI, o treinador e os testes no documento entregue junto com este arquivo.
2. Se um determinado parâmetro de uma função deve ser inteiro, então esta função deve rejeitar valores não-numéricos ou numerais não-inteiros nesse parâmetro.
3. Da mesma forma, se um parâmetro de uma função deve ser uma string, então esta função deve rejeitar valores que não sejam do tipo string nesse parâmetro.
4. Strings em branco são sempre consideradas inválidas.
5. Se algum dos parâmetros ser inválido, uma ValueError deve ser lançada. Recomenda-se usar as funções check_int e check_str acima para ajudar na validação.
6. Se algum parâmetro puder ser determinado como inválido antes que alguma chamada a um servidor externo seja realizada, então ele deve ser detectado como tal sem que o servidor seja contactado, mesmo se ele estiver off-line.
7. Em todos os casos onde procura-se algum tipo de pokémon pelo nome ou pelo número e o mesmo não existir, uma exceção PokemonNaoExisteException deve ser lançada.
8. Em todos os casos onde procura-se algum treinador cadastrado e o mesmo não existir, uma exceção TreinadorNaoCadastradoException deve ser lançada.
9. Em todos os casos onde procura-se algum pokémon cadastrado e o mesmo não existir, uma exceção PokemonNaoCadastradoException deve ser lançada.
10. Em todos os casos onde tenta-se cadastrar um pokémon e o mesmo já exista, uma exceção PokemonJaCadastradoException deve ser lançada.
11. Todos os nomes de pokémons que aparecerem como parâmetros devem ser aceitos em minúsculas, MAIÚSCULAS ou até mesmo MiStUrAdO. Lembre-se dos métodos lower() e upper() da classe string.
12. Todos os nomes de pokémons, cores, jogos, movimentos, etc. recebidos e devolvidos pela PokeAPI estão em letras minúsculas e assim devem ser mantidas.
13. Não faça conexões com as URLs externas (https://pokeapi.co). O motivo disso é que eles irão bloquear IPs que fizerem um número muito grande de requisições.

Alguns exemplos de URLs que podem servir de inspiração:
http://localhost:8000/api/v2/
http://localhost:8000/api/v2/pokemon/39/
http://localhost:8000/api/v2/pokemon/jigglypuff/
http://localhost:8000/api/v2/pokemon-species/39/
http://localhost:8000/api/v2/pokemon-species/jigglypuff/
http://localhost:8000/api/v2/evolution-chain/11/
http://localhost:8000/api/v2/growth-rate/1/
http://localhost:8000/api/v2/pokemon-color/2/
"""

"""
Não altere estas URLs. Elas são utilizadas para conectar no treinador e no PokeAPI, respectivamente.
"""
url_treinador = site_treinador = "http://127.0.0.1:9000"
url_pokeapi = site_pokeapi = "http://127.0.0.1:8000"

"""
Vamos precisar destas quatro exceções personalizadas.
"""
class PokemonNaoExisteException(Exception):
    pass

class PokemonNaoCadastradoException(Exception):
    pass

class TreinadorNaoCadastradoException(Exception):
    pass

class PokemonJaCadastradoException(Exception):
    pass

"""
Esta função certifica-se de que seu parâmetro é um número inteiro e lança uma ValueError se não for.
"""
def check_int(a):
    if type(a) is not int:
        raise ValueError()

"""
Esta função certifica-se de que seu parâmetro é uma string e que não está vazia e lança uma ValueError se não for.
"""
def check_str(a):
    if type(a) is not str or a == "":
        raise ValueError()

"""
Esta classe será utilizada no exercício 12 abaixo.
"""
@dataclass()
class Pokemon:
    nome_treinador: str
    apelido: str
    tipo: str
    experiencia: int
    nivel: int = 0 
    cor: str = 'azul'
    evoluiu_de: str = 'ninguem'
    evolui_para: list = ''

"""
1. Dado o número de um pokémon, qual é o nome dele?
"""
def nome_do_pokemon(numero):
    check_int(numero)
    if numero <=0 or numero >=808:
        raise PokemonNaoExisteException
    url='http://localhost:8000/api/v2/pokemon/'+str(numero)
    dic_pokemon= api.get(url).json()
    return dic_pokemon['name']

"""
2. Dado o nome de um pokémon, qual é o número dele?
"""
def numero_do_pokemon(nome):
    check_str(nome)
    nome=nome.lower()
    url='http://localhost:8000/api/v2/pokemon/'+str(nome)
    dic_pokemon= api.get(url).json()

    if 'detail' in dic_pokemon:
        raise PokemonNaoExisteException
    return dic_pokemon['id']

"""
3. Dado o nome ou número de um pokémon, qual é o nome da cor (em inglês) predominante dele?
"""
def color_of_pokemon(nome):
    check_str(nome)
    nome=nome.lower()
    url='http://localhost:8000/api/v2/pokemon-species/'+str(nome)
    dic_pokemon= api.get(url).json()
    if 'detail' in dic_pokemon:
        raise PokemonNaoExisteException
    return dic_pokemon['color']['name']

"""
4. Dado o nome ou número de um pokémon, qual é o nome da cor (em português) predominante dele?
Os nomes de cores possíveis em português são "marrom", "amarelo", "azul", "rosa", "cinza", "roxo", "vermelho", "branco", "verde" e "preto".
No entanto, a pokeapi ainda não foi traduzida para o português! Como você pode dar um jeito nisso?
"""
def cor_do_pokemon(nome):
    check_str(nome)
    nome=nome.lower()
    url='http://localhost:8000/api/v2/pokemon-species/'+str(nome)
    dic_pokemon= api.get(url).json()
    if 'detail' in dic_pokemon:
        raise PokemonNaoExisteException
    cor = dic_pokemon['color']['name'] 
    
    cores = {"brown": "marrom","yellow":"amarelo","blue":"azul","pink":"rosa","gray":"cinza","purple":"roxo","red":"vermelho","white":"branco","green":"verde","black":"preto"}
   

    return cores[cor]

"""
5. Dado o nome de um pokémon, quais são os tipos no qual ele se enquadra?
Os nomes dos tipos de pokémons em português são "normal", "lutador", "voador", "veneno", "terra", "pedra", "inseto", "fantasma", "aço", "fogo", "água", "grama", "elétrico", "psíquico", "gelo", "dragão", "noturno" e "fada".
Todo pokémon pode pertencer a um ou a dois tipos diferentes. Retorne uma lista contendo os tipos, mesmo que haja somente um.
Se houver dois tipos, a ordem não é importante.
"""
def tipos_do_pokemon(nome):
    check_str(nome)
    nome=nome.lower()
    url='http://localhost:8000/api/v2/pokemon/'+str(nome)
    #print('\n',url)
    dic_pokemon= api.get(url).json()
    tipos = {"normal": "normal","fighting":"lutador","flying":"voador","poison":"veneno","ground":"terra","rock":"pedra","bug":"inseto","ghost":"fantasma","steel":"aço","fire":"fogo","water":"água","grass":"grama", "electric":"elétrico", "psychic":"psíquico","ice":"gelo", "dragon":"dragão", "dark":"noturno", "fairy":"fada"}
    tipos_traduzidos = []

    if 'detail' in dic_pokemon:
        raise PokemonNaoExisteException
    

    tipo_pokemon = dic_pokemon['types']

    for i in tipo_pokemon:  
        tipos_traduzidos.append(tipos[i['type']['name']])
    return tipos_traduzidos

"""
6. Dado o nome de um pokémon, liste de qual pokémon ele evoluiu.
Por exemplo, evolucao_anterior('venusaur') == 'ivysaur'
Retorne None se o pokémon não tem evolução anterior. Por exemplo, evolucao_anterior('bulbasaur') == None
"""
def evolucao_anterior(nome):
    check_str(nome)
    nome=nome.lower()
    url='http://localhost:8000/api/v2/pokemon-species/'+str(nome)
    #print('\n',url)
    dic_pokemon= api.get(url).json()

    if 'detail' in dic_pokemon:
        raise PokemonNaoExisteException

    if dic_pokemon['evolves_from_species'] == None:
        return None
    else:
        print('\nEvolucao anterior: ', dic_pokemon['evolves_from_species']['name'])
        return dic_pokemon['evolves_from_species']['name']

"""
7. Dado o nome de um pokémon, liste para quais pokémons ele pode evoluiur.
Por exemplo, evolucoes_proximas('ivysaur') == ['venusaur'].
A maioria dos pokémons que podem evoluir, só podem evoluir para um único tipo de pokémon próximo. No entanto, há alguns que podem evoluir para dois ou mais tipos diferentes de pokémons.
Se houver múltiplas possibilidades de evoluções, a ordem delas não importa. Por exemplo:
evolucoes_proximas('poliwhirl') == ['poliwrath', 'politoed']
Note que esta função dá como resultado somente o próximo passo evoluitivo. Assim sendo, evolucoes_proximas('poliwag') == ['poliwhirl']
Se o pokémon não evolui, retorne uma lista vazia. Por exemplo, evolucoes_proximas('celebi') == []
"""
def evolucoes_proximas(nome):

    check_str(nome)
    nome=nome.lower()

    url_pokemon='http://localhost:8000/api/v2/pokemon/'+str(nome)
    print('\n')
    print('\nURL Pokemon: ',url_pokemon)
    dic_pokemon = api.get(url_pokemon).json()

    print('\nEvolução anterior: ', evolucao_anterior(nome))

    url_pokemon_species = dic_pokemon['species']['url']
    print('\nURL Species: ', url_pokemon_species)
    dic_pokemon_species = api.get(url_pokemon_species).json()
    
    url_pokemon_evolution_chain = dic_pokemon_species['evolution_chain']['url']
    print('\nURL Evolution Chain: ', url_pokemon_evolution_chain)
    dic_pokemon_evolution_chain = api.get(url_pokemon_evolution_chain).json()

    evolucoes = []


    #VERIFICA EXISTENCIA DO POKEMON

    #NÃO EXISTE
    if 'detail' in dic_pokemon:
        raise PokemonNaoExisteException

    #EXISTE
    else:

        #SE NÃO TIVER EVOLUÇÃO SIMPLES
        if len(dic_pokemon_evolution_chain['chain']['evolves_to']) != 0:
            
            if 'evolves_to' in dic_pokemon_evolution_chain['chain']:

                tamanho = len(dic_pokemon_evolution_chain['chain']['evolves_to'][0]['evolves_to'])
                print('\nTamanho: ', tamanho)

                if tamanho == 0 and evolucao_anterior(nome) == None:
                                        
                    print('\nentrei em tamanho 0')
                    evolves_to = dic_pokemon_evolution_chain['chain']['evolves_to']

                    for i in evolves_to:
                        evolucoes.append(i['species']['name'])
                elif tamanho == 2:

                    if evolucao_anterior(nome) == None:
                    
                        print('\nentrei em tamanho 2')
                        evolves_to = dic_pokemon_evolution_chain['chain']['evolves_to']

                        for i in evolves_to:
                            print('\nentrei no for')
                            evolucoes.append(i['species']['name'])

                    else:

                        if evolucao_anterior(evolucao_anterior(nome)) == None:
                            evolves_to = dic_pokemon_evolution_chain['chain']['evolves_to'][0]['evolves_to']

                            for i in evolves_to:
                                print('\nentrei no for')
                                evolucoes.append(i['species']['name'])

                elif tamanho == 1:

                    #SE NÃO TIVER EVOLUÇÃO ANTERIOR
                    if evolucao_anterior(nome) == None:
                        print('\nnão tem evolucao anterior')

                        if tamanho == 1:
                            evolucoes.append(dic_pokemon_evolution_chain['chain']['evolves_to'][0]['species']['name'])
                            print('\nadicionando: ',dic_pokemon_evolution_chain['chain']['evolves_to'][0]['species']['name'])                              
                            
                    #CASO TENHA EVOLUCAO ANTERIOR
                    else:
                        print('\nTem evolucao anterior')

                        if evolucao_anterior(evolucao_anterior(nome)) == None:

                            evolucoes.append(dic_pokemon_evolution_chain['chain']['evolves_to'][0]['evolves_to'][0]['species']['name'])
                            print('\nadicionando: ',dic_pokemon_evolution_chain['chain']['evolves_to'][0]['evolves_to'][0]['species']['name'])
                
                #elif tamanho == 2:
               


        print('\nEvoluções', evolucoes)
        
        return evolucoes

"""
8. A medida que ganham pontos de experiência, os pokémons sobem de nível.
É possível determinar o nível (1 a 100) em que um pokémon se encontra com base na quantidade de pontos de experiência que ele tem.
Entretanto, cada tipo de pokémon adota uma curva de level-up diferente (na verdade, existem apenas 6 curvas de level-up diferentes).
Assim sendo, dado um nome de pokémon e uma quantidade de pontos de experiência, retorne o nível em que este pokémon está.
Valores negativos de experiência devem ser considerados inválidos.
"""
def nivel_do_pokemon(nome, experiencia):
    pass

"""
9. Dado um nome de treinador, cadastre-o na API de treinador.
Retorne True se um treinador com esse nome foi criado e False em caso contrário (já existia).

Para passar esse teste, também vai ser necessário a função detalhar_treinador,
que conecta ao servidor e verifica se o treinador com o nome dado existe.

Essa funcao esta definida mais abaixo, nao precisa se preocupar com ela ainda
"""
def cadastrar_treinador(nome):
    pass

"""
10. Imagine que você capturou dois pokémons do mesmo tipo. Para diferenciá-los, você dá nomes diferentes (apelidos) para eles.
Logo, um treinador pode ter mais do que um pokémon de um determinado tipo, mas não pode ter dois pokémons diferentes com o mesmo apelido.
Assim sendo, dado um nome de treinador, um apelido de pokémon, um tipo de pokémon e uma quantidade de experiência, cadastre o pokémon com o tipo correspondente ao treinador dado na API do treinador.
Certifique-se de que todos os dados são válidos.
"""
def cadastrar_pokemon(nome_treinador, apelido_pokemon, tipo_pokemon, experiencia):
    pass

"""
11. Dado um nome de treinador, um apelido de pokémon e uma quantidade de experiência, localize esse pokémon e acrescente-lhe a experiência ganha.
"""
def ganhar_experiencia(nome_treinador, apelido_pokemon, experiencia):
   pass 

"""
12. Dado um nome de treinador e um apelido de pokémon, localize esse pokémon na API do treinador e retorne um objeto da classe Pokemon mostrando:
Qual é a sua espécie, a sua quantidade de experiência, o nome do seu treinador e o seu apelido (outros atributos da classe Pokemon serão preenchidos em um teste mais pra frente, que vai retomar essa função).
"""
def localizar_pokemon(nome_treinador, apelido_pokemon):
    pass

"""
13. Dado o nome de um treinador, localize-o na API do treinador e retorne um dicionário contendo como chaves, os apelidos de seus pokémons e como valores os tipos deles.
"""
def detalhar_treinador(nome):
    resp = api.get(url_treinador+'/treinador/'+nome)
    if resp.status_code == 404:
        raise TreinadorNaoCadastradoException
    return {}

"""
14. Dado o nome de um treinador, localize-o na API do treinador e exclua-o, juntamente com todos os seus pokémons.
"""
def excluir_treinador(nome_treinador):
    pass

"""
15. Dado o nome de um treinador e o apelido de um de seus pokémons, localize o pokémon na API do treinador e exclua-o.
"""
def excluir_pokemon(nome_treinador, apelido_pokemon):
    pass