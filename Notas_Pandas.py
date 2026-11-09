#Pandas
#https://pandas.pydata.org/docs/getting_started/index.html
from email.utils import decode_rfc2231

import Notas
import pandas as pd
import numpy as np
from numpy.random import randn
'''
#-----------------------------------------------------------------------------------
#Séries
#1 - pd.Series é uma função que formata e nomeia os dados.
#Resultado:
#a    1
#b    2
#c    3
#dtype: int64

#1 - Listas
etiqueta = ['a', 'b', 'c']
dados = [1, 2 , 3]

serie_1 = pd.Series(data=dados, index=etiqueta)
print(serie_1)

#2 - Dicionários
d = {'a' : 10, 'b': 20, 'c': 30}
serie_2 = pd.Series(data=d)
print(serie_2)

#-----------------------------------------------------------------------------------
#Medalhas em Série

#1 - Ele vai somar de acordo com as indexação, independente da ordem.


ser1 = pd.Series(data = [1,2,3,4], index = ['EUA', 'Alemanha', 'Itália', 'Japão'])
ser2 = pd.Series(data = [4,3,2,1], index = ['EUA', 'Alemanha', 'Itália', 'Japão'])

#Operações Matemáticas - Conseguimos somar e fazer qualquer equação matematica.
ser3 = ser1 * 2 + ser2
#Acesso ao Conteúdo
print(ser3)
print(ser3['EUA'])

#Referência pelo Índice - Ele manda coretamente para o index correto, independente da ordem.
ser4 = pd.Series(data = [4,3,2,1], index = ['Japão', 'Alemanha', 'Itália', 'EUA'])
print(ser3 + ser4)

#Índice que só existe de um lado - Ele ignora os que ele não conhece ou o que não assimila assimila.
ser5 = pd.Series(data = [1,2,3], index = ['Alemanha', 'Itália', 'Brasil'])
print(ser1 + ser5)

#-----------------------------------------------------------------------------------

#Data Frame
np.random. seed(101)
df = pd. DataFrame(randn(5,4),
    ['A', 'B', 'C', 'D', 'E'],
    ['W', 'X', 'Y', 'Z'])


print(df)

#1 Linhas - Listas com Listas por frequência
base = [['João', 54, 'M'],
        ['Maria', 54, 'F'],
        ['Thiago', 54, 'M'],
        ['Cordélia', 54, 'F']]
df_pessoas = pd. DataFrame(data= base, columns=['Nome', 'Idade', 'Sexo' ])
print(df_pessoas)

#2 Dicionários - Cada valor será uma lista com todos os registros
base_dic = {'Nome' : ['João', 'Maria', 'Thiago', 'Cordelia'],
            'Idade': [50, 45, 15, 25],
            'Sexo' : ['M', 'F' , 'M', 'F']}

df_pessoas = pd.DataFrame(data=base_dic)
print(df_pessoas)

#-----------------------------------------------------------------------------------
#Acesso ao conteúdo - Métodos de printar.
print('--------------------------')
print(df['W'])
print('--------------------------')
print(df[['W', 'X']])
#Acesso as Linhas
print('--------------------------')
print(df.loc['A'])
print('--------------------------')
print(df.iloc[0])

#Acesso a valores únicos - Um valor só.
valor = (df. loc['B' , 'X'])
print (valor)
valor_2 = df.iloc[1,1]
print(valor_2)

#Partes de valores - Apenas os valos que você quer.
parte_1 = df. loc[ ['A' , 'B'], ['X' , 'Y' ]]
print(parte_1)

#Intervalo - Só uma parte da tabela.
print(df.loc['A':'C'])
print(df.iloc[0:3])

#Novos dados
df ['Nova' ] = df['W'].astype(str) + df['X'].astype(str) #String
df['Nova_2'] = df['W'] + df['X']
print(df)


#Remover Colunas
df.drop('Nova', axis=1, inplace=True)
print(df)

#Remover linhas
df. drop( 'E', axis=0, inplace=True)
print(df)

#Seleção Condicionada
selec_condionada = df [ 'W' ] > 0
print(selec_condionada)
selec_condicionada_2 = df[df['W'] > 0]
print(selec_condicionada_2)


#Seleção Condicionada
selec_condionada = df [ 'W'] > 0
print(selec_condionada)
selec_condicionada_2 = df[df['W'] > 0]
print(selec_condicionada_2)

#-----------------------------------------------------------------------------------
#Colunas interligadas
coluna_z_coluna_x_maior_que_0 = df['Z'] [df['X' ] > 0]
print(coluna_z_coluna_x_maior_que_0)

#Colunas interligadas com logica E
coluna_z_coluna_w_e_x_maiores_que_0 = df['Z'][(df['W'] >0) & (df['X'] >0)]
print(coluna_z_coluna_w_e_x_maiores_que_0)

#Lógica OU e Não
print(df[(df['W'] > 0) | (df['X'] > 0)]) # (|) É inserido para o (Ou)
print(df[~(df['W'] > 0)]) # O (~) é inserido para colocar a lógica (Não)

#isin # Filtrar apenas as pessoas que quero
print(df_pessoas[df_pessoas['Nome'].isin(['João', 'Maria'])]) 

#Dados Faltantes
d = {'A' : [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}
df_nan = pd.DataFrame (data=d)

print(df_nan) #DataFrame com alguns vazios
print(df_nan.isnull()) #
print(df_nan.isnull().sum())
print(df_nan.isnull().mean())

#Linha Vazia
print(df_nan. dropna())
#Coluna Vazia
print(df_nan.dropna(axis=1))
print(df_nan.dropna(axis=1, thresh=2))
print(df_nan.fillna(value=0))
print(df_nan. fillna(value=df_nan[ 'A']. mean())|
print(df_nan['A'].fillna(value=df_nan['A'].median())))

#-----------------------------------------------------------------------------------
'''
#Importação de dados
df = pd.read_excel('Base Aula 002 - Exemplo.xlsx')
print(df.head())

df_web = pd.read_html('https://www.fdic.gov/bank-failures/failed-bank-list')
#print(df_web[0].head())

'''
#Estística
print(df.head()) # puxa os dados para o python
print('-------------------------------------------------------------------')
print(df.tail()) # puxa as ultimas 5 linhas
print('-------------------------------------------------------------------')
print(df.info()) # Traz um lista com todas as colunas e informações
print('-------------------------------------------------------------------')
print(df.describe()) # Me da a descrição
print('-------------------------------------------------------------------')
print(df['Quantidade'].mean()) # Média
print('-------------------------------------------------------------------')
print(df['Quantidade'].median()) # Mediana
print('-------------------------------------------------------------------')
print(df['Quantidade'].mode()) # Moda
print('-------------------------------------------------------------------')
print(df['Quantidade'].std()) # Desvio padrão
print('-------------------------------------------------------------------')
print(df['Quantidade'].var()) #Variança
print('-------------------------------------------------------------------')
print(df['Quantidade'].max()) # Máximo
print('-------------------------------------------------------------------')
print(df['Quantidade'].min())
print('-------------------------------------------------------------------')
print(df['Quantidade'].quantile(0.25))
print('-------------------------------------------------------------------')
print(df['Quantidade'].quantile(0.75))
print('-------------------------------------------------------------------')
print(df['Quantidade'].value_counts())
print('-------------------------------------------------------------------')
print(df['Produto'].unique())
print('-------------------------------------------------------------------')
print(df['Produto'].nunique())
print('-------------------------------------------------------------------')
print(df[['Quantidade', 'Total']].cov())
print('-------------------------------------------------------------------')
print(df[['Quantidade', 'Total']].corr())
print('-------------------------------------------------------------------')
print(df[['Total', 'Vendedor' ]].sort_values('Total', ascending=False))
print('-------------------------------------------------------------------')
print(df.nlargest(3 , 'Total'))
print('-------------------------------------------------------------------')

#-----------------------------------------------------------------------------------
#Exportação
df['comissao'] = df['Total'] * 0.50
df.to_excel('Nova_planilha.xlsx')

'''
#Agrupamento
print(df[['Vendedor', 'Total' ]].groupby('Vendedor' ). sum() )
print(df[['Vendedor', 'Total', 'Produto' , 'Quantidade' ]]. groupby (['Vendedor', 'Produto' ]).sum())

print(df.groupby('Loja') ['Total'].mean())
print(df.groupby('Loja')['Total'].count())

#Mais de uma função
print(df.groupby('Loja') ['Total'].agg(['sum', 'mean', 'count']))




































