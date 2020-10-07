import sys

from app import Questoes


def menuPrincipal():
    print('--'*26)
    print(' ####- MENU PRINCIPAL -#### ')
    print('--'*26)
    print('Entre com o número de uma ospção abaixo: ')
    while True:
        print('1 - Qual cidade maranhense teve o maior número de casos por 100 mil habitantes?')
        print('2 - Qual foi o dia com maior número de novos casos?')
        print('3 - Quantos anos possuía a pessoa mais jovem a morrer de Covid-19 no estado do Maranhão?')
        print('4 - Quantos anos possuía a pessoa mais velha a morrer de Covid-19 no estado do Maranhão?')
        print('5 - Qual a média de casos confirmados de Covid-19 nas três cidades do estado do Maranhão que apresentaram maior volume de contaminação?')
        print('6 - Em qual mês foi registrado a maior quantidade de casos confirmados de Covid-19 nas cidades do estado do Maranhão e qual o valor encontrado?')
        print('7 - Qual o percentual de pessoas acima de 60 anos que foram levadas a óbito pelo Covid-19 no Maranhão em relação à não idosas no mês obtido na segunda questão?')
        print('8 - Quantos dias após o primeiro contágio confirmado em Alto Alegre do Pindaré, houve o primeiro óbito na cidade? E qual era a situação dos casos confirmados?')
        print('9 - O vale do Pindaré é uma das 32 regiões administrativas do estado do Maranhão, formado pelas cidades de Alto Alegre do Pindaré, Bela Vista do Maranhão, Bom Jardim, Bom Jesus das Selvas, Buriticupu, Igarapé do Meio, Monção, Pindaré-Mirim, Santa Inês, Santa Luzia, São João do Carú e Tufilândia. Aonde ocorreu o primeiro caso na região do vale do Pindaré? E qual foi a data?')
        print('10 - Tendo os dados sobre o primeiro caso confirmado em cada cidade maranhense. Liste, em quais delas o primeiro óbito ocorreu 14 dias antes do primeiro caso confirmado na cidade')
        print('S - Sair do sistema')
        opcao = input('Opção n°: ')
        if opcao == '1':
            Questoes.Questao1()
            break
        if opcao == '2':
            Questoes.Questao2()
            break
        if opcao == '3':
            Questoes.Questao3()
            break
        if opcao == '4':
            Questoes.Questao4()
            break
        if opcao == '5':
            Questoes.Questao6()
            break
        if opcao == '6':
            Questoes.Questao9()
            break
        if opcao == '7':
            Questoes.Questao7()
            break
        if opcao == '8':
            Questoes.Questao8()
            break
        if opcao == '9':
            Questoes.Questao9()
            break
        if opcao == '10':
            Questoes.Questao10()
            break
        elif opcao == 'S' or opcao == 's':
            sys.exit()
        else:
            print("Erro!!! você digitou algo fora do sistema!")
