# IMPORTAÇÕES
import csv

# COLUNAS EM covid19_ma.csv : epidemiological_week,date,order_for_place,state,city,city_ibge_code,place_type,last_available_confirmed,last_available_confirmed_per_100k_inhabitants,new_confirmed,last_available_deaths,new_deaths,last_available_death_rate,estimated_population_2019,is_last,is_repeated


# QUESTÃO 1 #
def Questao1():
    arquivo = open('.\storage\covid19_ma.csv', encoding="utf8")
    linhas = csv.reader(arquivo)
    numMaior100MilHabitantes = 0
    next(linhas)
    for linha in linhas:
        if(not(linha[8] == '')):
            parser = int(float(linha[8]))
            if(parser > numMaior100MilHabitantes):
                numMaior100MilHabitantes = parser
                cidadeMaisCasos = linha[4]
    print(cidadeMaisCasos + ' com aproximadamente ' + str(numMaior100MilHabitantes) + ' casos confirmados por 100 mil habitantes')

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

# QUESTÃO 5 #


def Questao5():
    print('Olá mundo')
# FIM DA QUESTÃO #

# QUESTÃO 6 #


def Questao6():
    print('Olá mundo')
# FIM DA QUESTÃO 6 #

# QUESTÃO 7 #


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
