# IMPORTAÇÕES
import csv
from datetime import datetime

# COLUNAS EM covid19_ma.csv : epidemiological_week,date,order_for_place,state,city,city_ibge_code,place_type,last_available_confirmed,last_available_confirmed_per_100k_inhabitants,new_confirmed,last_available_deaths,new_deaths,last_available_death_rate,estimated_population_2019,is_last,is_repeated


# QUESTÃO 1: Qual foi o dia com maior número de novos casos? #

def Questao1():
    arquivo = open('.\storage\covid19_ma.csv', encoding="utf8")
    linhas = csv.reader(arquivo)
    next(linhas)
    numMaior100MilHabitantes = 0
    for linha in linhas:
        if(not(linha[8] == '')):
            parser = int(float(linha[8]))
            if(parser > numMaior100MilHabitantes):
                numMaior100MilHabitantes = parser
                cidadeMaisCasos = linha[4]
    print(cidadeMaisCasos + ' com aproximadamente ' +
          str(numMaior100MilHabitantes) + ' casos confirmados por 100 mil habitantes')


# FIM DA QUESTÃO #

# QUESTÃO 2 #


def Questao2():
    print('Olá mundo')
# FIM DA QUESTÃO #

# QUESTÃO 3 #


def Questao3():
    print('Olá mundo')
# FIM DA QUESTÃO 3 #

# QUESTÃO 4 #


def Questao4():
    print('Olá mundo')
# FIM DA QUESTÃO 4 #

# QUESTÃO 5: Qual a média de casos confirmados de Covid-19 nas três cidades do estado do Maranhão que apresentaram maior volume de contaminação? #


def Questao5():
    # LEITURA DO(S) ARQUIVO(S) NECESSÁRIO(S)
    arquivoCsv = open('.\storage\covid19_ma.csv', encoding="utf8")
    objArquivoCsv = csv.reader(arquivoCsv)
    next(objArquivoCsv)

    # criação da lista que conterá os dados do arquivo
    linhas = []
    for linhaCsv in objArquivoCsv:
        linhas.append(linhaCsv)

    # 1º - Cria um dicionário relacionando o nome da cidade com o valor iniciador de quantidade de contaminados, dia do primeiro e do último  caso confirmado da COVID 19 na cidade
    cidades = {}
    for linha in linhas:
        if(linha[4] not in cidades.keys()):
            primeiroLoopDataUltimoCaso = linha[1]
        cidades[linha[4]] = [0, linha[1], primeiroLoopDataUltimoCaso]

    # 2º Soma a quantidade de contaminados de cada cidade
    for linha in linhas:
        cidades[linha[4]][0] = cidades[linha[4]][0] + int(linha[9])
    # 3º Descobrir as três cidades que possuem mais casos de contaminação e realizar média diária.
    cidadesComContamindadosDec = sorted(
        cidades.items(), key=lambda x: x[1], reverse=True)
    podio = [0, 1, 2]
    for posicao in podio:
        posicaoPodioStr = str(posicao + 1)
        nomeCidade = cidadesComContamindadosDec[posicao][0]
        primeiroCasoData = datetime.strptime(
            cidadesComContamindadosDec[posicao][1][1], '%Y-%m-%d')
        ultimoCasoData = datetime.strptime(
            cidadesComContamindadosDec[posicao][1][2], '%Y-%m-%d')
        quantidadeDias = abs((primeiroCasoData - ultimoCasoData).days)
        media = str(
            round(cidadesComContamindadosDec[posicao][1][0] / quantidadeDias, 2))
        print(posicaoPodioStr + "º lugar: " + nomeCidade +
              ", com média de " + media + " casos/dia.")


# FIM DA QUESTÃO 5 #

# QUESTÃO 6 : Em qual mês foi registrado a maior quantidade de casos confirmados de Covid-19 nas cidades do estado do Maranhão e qual o valor encontrado?#


def Questao6():
    # LEITURA DO(S) ARQUIVO(S) NECESSÁRIO(S)
    arquivoCsv = open('.\storage\covid19_ma.csv', encoding="utf8")
    objArquivoCsv = csv.reader(arquivoCsv)
    next(objArquivoCsv)

    # criação da lista que conterá os dados do arquivo
    linhas = []
    for linhaCsv in objArquivoCsv:
        linhas.append(linhaCsv)

    # 1º Cria um dicionário para guardar a quantidade de casos confirmados em cada mês
    mesQuantidadeCasosConfirmados = {}
    for linha in linhas:
        mesQuantidadeCasosConfirmados[linha[1][5:7]] = 0

    # 2º Alimenta o dicionário com a quantidade de casos confirmados em cada mês
    for linha in linhas:
        mesQuantidadeCasosConfirmados[linha[1][5:7]] = int(
            mesQuantidadeCasosConfirmados[linha[1][5:7]]) + int(linha[9])

    # 3º Ordena o dicionario em ordem decrescente
    mesesQuantidadeContaminadosDesc = sorted(
        mesQuantidadeCasosConfirmados.items(), key=lambda x: x[1], reverse=True)

    # 4º Exibe o mes com maior quantidade de afetados
    mesComMaiorQuantidadeContaminados = str(
        mesesQuantidadeContaminadosDesc[0][0][1:2])
    quantidadeMesComMaiorQuantidadeContaminados = str(
        mesesQuantidadeContaminadosDesc[0][1])
    print("O " + mesComMaiorQuantidadeContaminados + "º mês possui a maior quantidade de casos confirmados de Covid 19 com " +
          quantidadeMesComMaiorQuantidadeContaminados + " casos registrados.")
# FIM DA QUESTÃO 6 #

# QUESTÃO 7 : Qual o percentual de pessoas acima de 60 anos que foram levadas a óbito pelo Covid-19 no Maranhão em relação à não idosas no mês onde foi registrado a maior quantidade de casos?#


def Questao7():
    print('Olá mundo')
# FIM DA QUESTÃO 7 #

# QUESTÃO 8 #


def Questao8():
    print('Olá mundo')
# FIM DA QUESTÃO 8 #

# QUESTÃO  #


def Questao():
    print('Olá mundo')
# FIM DA QUESTÃO #

# QUESTÃO 9 #


def Questao():
    print('Olá mundo')
# FIM DA QUESTÃO #

# QUESTÃO  #


def Questao9():
    print('Olá mundo')
# FIM DA QUESTÃO 9 #

# QUESTÃO 10 #


def Questao10():
    print('Olá mundo')
# FIM DA QUESTÃO 10 #
