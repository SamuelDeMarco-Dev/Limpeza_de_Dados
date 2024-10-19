import pandas as pd #importando Biblioteca pandas
import numpy as np #importando biblioteca numpy

file_path = 'C:/Users/Chimba04/Documents/Mineração de Dados/limpeza_de_dados/Dados/base_logistica.csv' #importando arquivo .csv da base de dados que será tratada
lendo_logistica = pd.read_csv(file_path) #lendo arquivo utilizando a Biblioteca pandas
print(lendo_logistica.head(20)) #printando os 20 valores iniciais da base

lendo_logistica.info() #tipos e valores ausentes 

lendo_logistica.describe() #estatisticas descritivas

lendo_logistica['UF'].value_counts() #quantidade de valores distintos do atributo

lendo_logistica['UF'] = lendo_logistica['UF'].str.upper() #metodo para padronizar tudo maiusculo upper
lendo_logistica['UF'].value_counts()

lendo_logistica['Marca'] = lendo_logistica['Marca'].str.upper()
lendo_logistica['Marca'].value_counts()

# *************************************************** IMPUTAÇÃO DE VALORES - MÉTODOS PARA PREENCHER ATRIBUTOS AUSENTES *************************************************** #

lendo_logistica['Valor do Frete Líquido'].fillna(round(lendo_logistica['Valor do Frete Líquido'].mean()), inplace=True) #função fillna utilizando a média mean para preencher os valores nulos
lendo_logistica['Valor do Frete Líquido'].value_counts()

lendo_logistica['Tipo Veículo'].fillna(method="bfill",inplace=True) #função fillna utilizando o próximo valor bfill para preencher os valores nulos
lendo_logistica['Tipo Veículo'].value_counts()

lendo_logistica['Km'].fillna(lendo_logistica['Km'].mean(), inplace=True)
lendo_logistica['Km'].value_counts()

lendo_logistica['Tipo Veículo'].fillna(method="bfill", inplace=True)
lendo_logistica['Tipo Veículo'].value_counts()

lendo_logistica['Data Pedido'].fillna(method="ffill", inplace=True) #função fillna utilizanddo o anterior valor ffill para preencher os valores nulos
lendo_logistica['Data Pedido'].value_counts()
lendo_logistica['Data Pedido'].fillna(method="bfill", inplace=True)
lendo_logistica['Data Pedido'].value_counts()

lendo_logistica.info()
lendo_logistica.head(len(lendo_logistica)) 

print(lendo_logistica.head(10))

# *************************************************** REDUÇÃO DE VALORES - MÉTODOS PARA REALIZAR A ANÁLISE *************************************************** #

lendo_logistica_reduced = lendo_logistica.drop(['Marca', 'Viagem'], axis=1) #função drop para remover alguns dados da base(Análise para ver se faz sentido na Mineração)
print(lendo_logistica_reduced.head(10))

lendo_logistica_sample = lendo_logistica.sample(frac=0.7) #reduzindo o numero de dados, Amostra de 70% das linhas de lendo_logistica
print(len(lendo_logistica_sample)) #Verificar quantas linhas foram extraídas
print(lendo_logistica_sample.head()) #exibe amostra
