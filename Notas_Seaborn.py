#https://seaborn.pydata.org/examples/index.html
import matplotlib.pyplot as plt
import seaborn as sns
#import matplotlib pyplot as plt
#import numpy as np
#import pandas as pd

gorjeta = sns.load_dataset ( 'tips')
#gorjeta = pd.read_excel( ' . .... ')
'''
#Análise exploratória
#print(gorjeta.head())
#print(gorjeta.info())
#print(gorjeta.describe().round(2))


#Plotagens univariada
sns.histplot(gorjeta['total_bill'])
plt.show() # É o print do Seaborn

#Rugplot - cada traço é uma observação
sns.rugplot(gorjeta['total_bill'])
plt. show()

#KDE

sns. kdeplot(data = gorjeta, x = 'total_bill')
plt. show()

#ECDF - "Que % está abaixo de x"
sns. ecdfplot (data = gorjeta, x = 'total_bill')
plt. show()

#Plotagem Comparada
sns.scatterplot(data = gorjeta, x = 'total_bill', y ='tip')
plt.show()

sns.jointplot(x = 'total_bill', y = 'tip', data = gorjeta)
plt.show()

sns.jointplot(x = 'total_bill', y = 'tip', data = gorjeta, kind ='hex', color='gray')
plt.show()

sns.jointplot(x = 'total_bill', y = 'tip', data = gorjeta, kind ='reg')
plt.show()

#Regrassão separada por categoria
sns.lmplot(data=gorjeta, x= 'total_bill', y ='tip', hue ='smoker')
plt.show()

#Gráficos comparativos para todas as variáveis numéricas
sns.pairplot(gorjeta, hue='sex')
plt.show()

#Plotagens categóricas
sns.barplot (x = 'sex' , y = 'total_bill', data = gorjeta)
plt.show()

#Gráfico de contagem
sns.countplot (x = 'sex' , data = gorjeta)
plt.show()

#Diagrama de caixa

sns.boxplot(x = 'day', y = 'total_bill', data = gorjeta)
plt.show()
#Diagrama de caixa - Comparando com fumantes
sns.boxplot(x = 'day', y = 'total_bill', data = gorjeta, hue ='someker')
plt.show()

#Diagrama de caixa
sns.boxplot (x = 'day', y = 'total_bill', data = gorjeta)
plt. show()

#Diagrama de caixa - Comparando com fumantes
sns.boxplot(x = 'day', y = 'total_bill', data = gorjeta, hue ='smoker')
plt.show()

#Diagrama de Violino
sns. violinplot(x = 'day', y = 'total_bill', data = gorjeta, hue ='sex' , split=True)
plt.show()

#Stripplot
sns.stripplot(x = 'day', y = 'total_bill', data=gorjeta, jitter=True, hue= 'sex' )
plt.show()

#Gráfico de Enxame
sns. swarmplot (x = 'day', y = 'total_bill', data=gorjeta)
plt.show()

sns.pointplot (x = 'day', y = 'total_bill', data=gorjeta)
plt.show()

#Codigo em que voce coloca o tipo no final
sns.catplot(x = 'day', y = 'total_bill', data=gorjeta, kind='bar')
plt.show()

'''
'''
voos = sns.load_dataset('flights')
#Grafico em linha com pontos
sns.lineplot(data = voos, x = 'year', y = 'passengers', marker = 'o')
plt.show()

#plotagem de matriz
vp = voos.pivot_table(index='month', columns='year', values='passengers')

#Mapa de calor
sns.heatmap(vp)
plt.show()

#Mapa de Cluster
sns.clustermap(vp, standart_scaler=1)
plt.show()

#Salvar figuras
sns.histplot(data=gorjeta, x = 'total_bill', bins=30)
plt.title('A conta tipica fica entre 10 e 20')
plt.tight_layout()
plt.savefig('Histograma.png', dpi = 200)
plt.show()
'''


# Carregar datasets
voos = sns.load_dataset('flights')
gorjeta = sns.load_dataset('tips')  # Adicionado para corrigir o último gráfico

# Gráfico em linha com pontos
sns.lineplot(data=voos, x='year', y='passengers', marker='o')
plt.show()

# Plotagem de matriz
vp = voos.pivot_table(index='month', columns='year', values='passengers')

# Mapa de calor
sns.heatmap(vp)
plt.show()

# Mapa de Cluster (Correção: standard_scale)
sns.clustermap(vp, standard_scale=1)
plt.show()

# Salvar figuras (Agora a variável 'gorjeta' existe)
sns.histplot(data=gorjeta, x='total_bill', bins=30)
plt.title('A conta tipica fica entre 10 e 20')
plt.tight_layout()
plt.savefig('Histograma.png', dpi=200)
plt.show()










