import pandas as pd
import numpy as np
import colorama as color


#declarando os dados
atendimento = pd.read_csv('dados/atendimento.csv')
vendas = pd.read_csv('dados/vendas.csv')

#criação das funções
def valor_total():
    print(f'\nValor total de vendas: {color.Fore.LIGHTGREEN_EX}{vendas['valor_venda'].sum()}{color.Fore.RESET}\n')

def maior_compras():
    maior = vendas.loc[vendas['valor_venda'].idxmax()]
    print(f'Cliente com maior numero de vendas')
    print(f'ID do Cliente: {maior['id_cliente']}')
    print(f'ID da Venda: {maior['id_venda']}')
    print(f'Valor da venda: {maior['valor_venda']}')

def atendimentos_realizados():
    print(f'\nHouveram {atendimento['data_atendimento'].count()} atendimentos nos ultimos 30 dias.')

def motivo_comum():
    print(f'\nO motivo mais comum nos atendimentos foi justamente o {atendimento['motivo'].mode()[0]}.')

def linha():
    print('---------' * 8)

print(f'{color.Fore.LIGHTGREEN_EX}Vendas'.center(55))
print(f'{vendas}{color.Fore.RESET}')
linha()

#valor total de vendas realizadas
valor_total()
#cliente com o maior numero de compras
maior_compras()
linha()

print(f'{color.Fore.LIGHTCYAN_EX}Atendimentos'.center(55))
print(f'{atendimento}{color.Fore.RESET}')
linha()

#Quantos atendimentos foram realizados nos últimos 30 dias?
atendimentos_realizados()

#Qual é o motivo mais comum nos atendimentos?
motivo_comum()


