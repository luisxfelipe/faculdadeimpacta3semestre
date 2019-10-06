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

class BaseDeDados:

    ###
    #   METODO CONSTRUTOR DA CLASSE
    ###
    
    def __init__(self, ocorreciasSemProcessar: Ocorrencia, ocorreciasProcessadas: Ocorrencia, multas: Multa, regras: RegraMulta) -> None:
        self._ocorreciasSemProcessar = ocorreciasSemProcessar
        self._ocorreciasProcessadas = ocorreciasProcessadas
        self._multas = multas
        self._regras = regras

    ###
    #   METODOS DE ACESSO
    ###

    def getOcorreciasSemProcessar(self) -> Ocorrencia:
        return self._ocorreciasSemProcessar

    def getOcorreciasProcessadas(self) -> Ocorrencia:
        return self._ocorreciasProcessadas

    def getMultas(self) -> Multa:
        return self._multas

    def getRegras(self) -> RegraMulta:
        return self._regras

    ###
    #   OUTROS METODOS DA CLASSE
    ###        

    def processar(self):
        pass

    def inicializaRegras(self):
        pass

class RegraMulta:

    ###
    #   METODO CONSTRUTOR DA CLASSE
    ###
    
    def __init__(self, valorMultaMedia: float, valorMultaGrave: float, valorMultaLeve: float) -> None:
        self._valorMultaMedia = valorMultaMedia
        self._valorMultaGrave = valorMultaGrave
        self._valorMultaLeve = valorMultaLeve

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

class RegraVelocidade:

    ###
    #   METODO CONSTRUTOR DA CLASSE
    ###
    
    def __init__(self, velocidadeMaxima: int, nomeLogradouro: str, porcentagemMultaMedia: float, porcentagemMultaGrave: float) -> None:
        self._velocidadeMaxima = velocidadeMaxima
        self._nomeLogradouro = nomeLogradouro
        self._porcentagemMultaMedia = porcentagemMultaMedia
        self._porcentagemMultaGrave = porcentagemMultaGrave

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

    ###
    #   OUTROS METODOS DA CLASSE
    ###

    def verificaNivelMulta(self, o) -> int:
        pass

    def obterDescricaoMulta(self) -> str:
        pass

    def regraVelocidade(self, velMax, logr):
        pass

class RegraRodizio:

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

class RegraCorredorOnibus:

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