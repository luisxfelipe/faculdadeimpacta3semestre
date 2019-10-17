
#BaseDados.inicializaRegras()

class BaseDeDados:

    ###
    #   METODO CONSTRUTOR DA CLASSE
    ###
    #, 
    def __init__(self, ocorreciasSemProcessar, ocorreciasProcessadas) -> None:
        self._ocorreciasSemProcessar = []
        self._ocorreciasProcessadas = []
        self._multas = []
        self._regras = []

    ###
    #   METODOS DE ACESSO
    ###

    def contaOcorenciasSemProcessar(self):
        return len(self._ocorreciasSemProcessar)

    def getOcorreciasSemProcessar(self):
        return self._ocorreciasSemProcessar

    def setOcorrenciaSemProcessar(self, ocorrencia):
        self._ocorreciasSemProcessar.append(ocorrencia)

    def getOcorreciasProcessadas(self):
        return self._ocorreciasProcessadas

    def getMultas(self):
        return self._multas

    def getRegras(self) -> []:
        return self._regras

    def cadastraRegra(self, regra):
        self._regras.append(regra)

    ###
    #   OUTROS METODOS DA CLASSE
    ###        

    def processar(self):
        pass

    def inicializaRegras(self):

        print('\nInicializando Regras...\n')
        
        self._regras.append(RegraVelocidade(60, "Avenida Brasil"))
        self._regras.append(RegraVelocidade(70, "Avenida França"))
        self._regras.append(RegraVelocidade(80, "Avenida Canada"))
        self._regras.append(RegraVelocidade(90, "Rodovia Alemanha"))
        self._regras.append(RegraVelocidade(120, "Rodovia Castelo Branco"))
        self._regras.append(RegraVelocidade(60, "Avenida Presidente Vargas"))
        self._regras.append(RegraVelocidade(70, "Avenida das Nações"))
        self._regras.append(RegraVelocidade(80, "Avenida Santa Maria"))
        self._regras.append(RegraVelocidade(90, "Rodovia Castelo Preto"))
        self._regras.append(RegraVelocidade(120, "Rodovia Leste"))
        

        self._regras.append(RegraRodizio(0, {"Rodovia Amarela", "Rodovia Verde"}, 1, 1))
        self._regras.append(RegraRodizio(1, {"Rodovia Roza", "Rodovia Azul"}, 2, 2))
        self._regras.append(RegraRodizio(2, {"Rodovia Amarela", "Rodovia Verde"}, 3, 1))
        self._regras.append(RegraRodizio(3, {"Rodovia Roza", "Rodovia Azul"}, 4, 2))
        self._regras.append(RegraRodizio(4, {"Rodovia Amarela", "Rodovia Verde"}, 5, 1))
        self._regras.append(RegraRodizio(5, {"Rodovia Roza", "Rodovia Azul"}, 1, 2))
        self._regras.append(RegraRodizio(6, {"Rodovia Amarela", "Rodovia Verde"}, 2, 1))
        self._regras.append(RegraRodizio(7, {"Rodovia Roza", "Rodovia Azul"}, 3, 2))
        self._regras.append(RegraRodizio(8, {"Rodovia Amarela", "Rodovia Verde"}, 4, 1))
        self._regras.append(RegraRodizio(9, {"Rodovia Roza", "Rodovia Azul"}, 5, 2))

        self._regras.append(RegraCorredorOnibus(6, 18, "Corredor 1"))
        self._regras.append(RegraCorredorOnibus(7, 19, "Corredor 2"))
        self._regras.append(RegraCorredorOnibus(8, 20, "Corredor 3"))
        self._regras.append(RegraCorredorOnibus(9, 21, "Corredor 4"))
        self._regras.append(RegraCorredorOnibus(6, 17, "Corredor 5"))
        self._regras.append(RegraCorredorOnibus(8, 14, "Corredor 6"))
        self._regras.append(RegraCorredorOnibus(5, 12, "Corredor 7"))
        self._regras.append(RegraCorredorOnibus(9, 16, "Corredor 8"))
        self._regras.append(RegraCorredorOnibus(8, 15, "Corredor 9"))
        self._regras.append(RegraCorredorOnibus(5, 11, "Corredor 10"))

class Multa:

    ###
    #   METODO CONSTRUTOR DA CLASSE
    ###

    def __init__(self, valor: float, motivo: str, data: str, placa: str) -> None:
        self._valor = valor
        self._motivo = motivo
        self._data = data
        self._placa = placa

    ###
    #   METODOS DE ACESSO
    ###

    def getValor(self) -> float:
        return self._valor

    def getMotivo(self) -> str:
        return self._motivo
    
    def getData(self) -> str:
        return self._data

    def getplaca(self) -> str:
        return self._placa

class Ocorrencia:

    ###
    #   METODO CONSTRUTOR DA CLASSE
    ###
    
    def __init__(self, placa: str, dataHora: str, nomeLogradouro: str, velocidadeMedia: int, tipoVeiculo: int) -> None:
        self._placa = placa
        self._dataHora = dataHora
        self._nomeLogradouro = nomeLogradouro
        self._velocidadeMedia = velocidadeMedia
        self._tipoVeiculo = tipoVeiculo

    ###
    #   METODOS DE ACESSO
    ###

    def getplaca(self) -> str:
        return self._placa

    def getDataHora(self) -> str:
        return self._dataHora

    def getNomeLogradouro(self) -> str:
        return self._nomeLogradouro

    def getVelocidadeMedia(self) -> int:
        return self._velocidadeMedia

    def getTipoVeiculo(self) -> int:
        return self._tipoVeiculo

class RegraMulta:

    ###
    #   METODO CONSTRUTOR DA CLASSE
    ###
    #valorMultaMedia: float, valorMultaGrave: float, valorMultaLeve: float
    def __init__(self) -> None:
        self._valorMultaMedia = float(100)
        self._valorMultaGrave = float(200)
        self._valorMultaLeve = float(float(50))

    ###
    #   METODOS DE ACESSO
    ###

    def getValorMultaMedia(self) -> float:
        return self._valorMultaMedia

    def getValorMultaGrave(self) -> float:
        return self._valorMultaGrave

    def getValorMultaLeve(self) -> float:
        return self._valorMultaLeve

    ###
    #   OUTROS METODOS DA CLASSE 
    ###

    def calcularMulta(self, o) -> Multa:
        pass

    def verificaNivelMulta(self, o) -> int:
        pass

    def obterDescricaoMulta(self) -> str:
        pass

class RegraVelocidade(RegraMulta):

    ###
    #   METODO CONSTRUTOR DA CLASSE
    ###
    
    def __init__(self, velocidadeMaxima: int, nomeLogradouro: str) -> None:
        self._velocidadeMaxima = velocidadeMaxima
        self._nomeLogradouro = nomeLogradouro
        self._porcentagemMultaMedia = float(0.1)
        self._porcentagemMultaGrave = float(0.4)

        

    ###
    #   METODOS DE ACESSO
    ###

    def getVelocidadeMaxima(self) -> int:
        return self._velocidadeMaxima

    def getNomeLogradouro(self) -> str:
        return self._nomeLogradouro

    def getPorcentagemMultaMedia(self) -> float:
        return self._porcentagemMultaMedia

    def getPorcentagemMultaGrave(self) -> float:
        return self._porcentagemMultaGrave

    def setVelocidadeMaxima(self, velocidadeMaxima):
        self._velocidadeMaxima = velocidadeMaxima

    def setNomeLogradouro(self, nomeLogradouro):
        self._nomeLogradouro = nomeLogradouro

    ###
    #   OUTROS METODOS DA CLASSE
    ###

    def verificaNivelMulta(self, o) -> int:
        pass

    def obterDescricaoMulta(self) -> str:
        pass

    def regraVelocidade(self, velMax, logr):
        pass

class RegraRodizio(RegraMulta):

    ###
    #   METODO CONSTRUTOR DA CLASSE
    ###

    def __init__(self, finalPlaca: int, logradourosAfetados: str, diaDaSemana: int, tipoVeiculo: int) -> None:
        
        self._finalPlaca = finalPlaca
        self._logradourosAfetados = logradourosAfetados
        self._diaDaSemana = diaDaSemana
        self._tipoVeiculo = tipoVeiculo

    ###
    #   METODOS DE ACESSO
    ###

    def getFinalPlaca(self) -> int:
        return self._finalPlaca

    def getLogradourosAfetados(self) -> str:
        return self._logradourosAfetados

    def getDiaDaSemana(self) -> int:
        return self._diaDaSemana

    def getTipoVeiculo(self) -> int:
        return self._tipoVeiculo

    ###
    #   OUTROS METODOS DA CLASSE
    ###

    def verificaNivelMulta(self, o) -> int:
        pass

    def obterDescricaoMulta(self) -> str:
        pass

    def regraRodizio(self, placa, logr, dia, tipVei):
        pass

class RegraCorredorOnibus(RegraMulta):

    ###
    #   METODO CONSTRUTOR DA CLASSE
    ###
    
    def __init__(self, horaInicial: int, horaFinal: int, nomeLogradouro: str) -> None:
        
        self._horaInicial = horaInicial
        self._horaFinal = horaFinal
        self._nomeLogradouro = nomeLogradouro

    ###
    #   METODOS DE ACESSO
    ###

    def getHoraInicial(self) -> int:
        return self._horaInicial

    def getHoraFinal(self) -> int:
        return self._horaFinal

    def getNomeLogradouro(self) -> str:
        return self._nomeLogradouro

    ###
    #   OUTROS METODOS DA CLASSE  
    ###

    def verificaNivelMulta(self, o) -> int:
        pass

    def obterDescricaoMulta(self) -> str:
        pass

    def regraCorredorOnibus(self, ini, fim, logr):
        pass

def ValidaExecucao():
    continua = input('\nDeseja continuar a execução do rograma (s/n)? ')

    print('\nOpção escolhida: ', continua)

    if continua == "s" or continua == "S":
        
        execucao = True
    elif continua == "n" or continua == "N":
        
        execucao = False
    else:
        
        while continua != "s" or continua != "S" or continua != "n" or continua != "N":
            continua = input("Opção inválida você digitou(", continua, "), digite s ou n:")

            if continua == "s" or continua == "S":
                execucao = True
            elif continua == "n" or continua == "N":
                execucao = False

    return execucao


base = BaseDeDados([], [])

base.inicializaRegras()





execucao = True

while execucao == True:
    print('\nEscolha uma das opções.\n')
    print('\n1 - Cadastrar ocorrência.')
    print('\n2 - Pesquisa de multas por data e placa. ')
    print('\n3 - Importar as ocorrências de um arquivo de texto')
    print('\n4 - Cadastrar nova regra.')
    print('\n5 - Sair do programa.')

    opcao = int(input('\nDigite o número da opção desejada: '))

    if opcao == 1:
        print('\nCadastro de ocorrência.\n')

        print('\nNumero de ocorrencias: ', base.contaOcorenciasSemProcessar())

        #placa: str, dataHora: str, nomeLogradouro: str, velocidadeMedia: int, tipoVeiculo: int

        placa = input("\nDigite a placa do veículo: ")

        data = ""

        while len(data) != 14:
            data = input("\nDigite a data da e hora da multa ex: 15/04/2019 20:00 : ")

            if len(data) != 14:
                print("\nFormato da data incorreto o certo é 15/04/2019 20:00")

        print("\nLen da data: ", len(data))
        nomeLogradouro = input("\nDigite o nome do logradouro: ")
        velocidadeMedia = input("\nDigite a velocidade média: ")
        tipoVeiculo = input("\nDigite o tipo do veículo: ")
        ocorrencia = Ocorrencia(placa, data, nomeLogradouro, velocidadeMedia, tipoVeiculo)
        base.setOcorrenciaSemProcessar(ocorrencia)

        print('\nNumero de ocorrencias: ', base.contaOcorenciasSemProcessar())
        print('\nOcorrencia cadastrada com sucesso.\n')

        execucao = ValidaExecucao()


    elif opcao == 2:
        print('\nPesquisa de multas por data e placa.\n')
    elif opcao == 3:
        print('\nImportação de ocorrências.\n')
    elif opcao == 4: 
        print('\nCadastro de regra.\n')

        print('\nEscolha uma das opções.\n')
        print('\n1 - Regra de Velocidade.')
        print('\n2 - Regra de Rodizio. ')
        print('\n3 - Regra de Corredor de onibus.')
        
        opcaoRegra = int(input('\nDigite o número da opção desejada: '))

        if opcaoRegra == 1:
            velocidadeRegra = int(input('\nDigite a velocidade: '))
            logradouroRegra = input('\nDigite o nome do logradouro: ')

            regraParaCadastrar = RegraVelocidade(velocidadeRegra, logradouroRegra)
        elif opcaoRegra == 2:
            pass
        elif opcaoRegra ==3:
            pass

        base.cadastraRegra(regraParaCadastrar)

        print("\nRegra cadastrada com sucesso!")

        execucao = ValidaExecucao()

    elif opcao == 5:
        print('\nPrograma encerrado.\n')
        execucao = False


