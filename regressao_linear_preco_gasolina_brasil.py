# -*- coding: utf-8 -*-
"""AF_Regressao Linear.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vVDhODkM_B1KwIZcvskSb2FIeNtgW5YP
"""

from google.colab import drive
drive.mount('/content/drive')

# bibliotecas

import numpy as np

from matplotlib import pyplot as plt

import seaborn as sns

import pandas as pd

import statsmodels.api as sm
import statistics

#dados
df_combustivel = pd.read_csv('/content/drive/MyDrive/Facens/S2A2022/Analise Preditiva/AF - Regressão Linear - Preço Gasolina Comum/dados/preco-medio-semanal-gasolinaComum-05-2004-a-11-2022.csv')

df_combustivel

# info dados
df_combustivel.info()

df_combustivel.describe()

# correlação
df_combustivel.corr()

# ordenando correlação dos dados maior para menor
df_combustivel.corr()["PRECO MEDIO REVENDA"].abs().sort_values(ascending = False)

#Correlação
sns.pairplot(df_combustivel.iloc[: , list(np.arange(10))])

#plot preço vs tempo
plt.scatter( df_combustivel['N SEQ SEMANA'], df_combustivel['PRECO MEDIO REVENDA'])

# selecionando colunas para regressão
x = pd.DataFrame(df_combustivel["N SEQ SEMANA"])
y = pd.DataFrame(df_combustivel["PRECO MEDIO REVENDA"])


# gerando metodo ols - minimos quadrado
X = sm.add_constant(x)
model = sm.OLS(y, X).fit()
model.summary()

# gerando array com np Y e X

y = np.array(df_combustivel["PRECO MEDIO REVENDA"])
x = np.array([i+1 for i in range(len(df_combustivel["N SEQ SEMANA"]))])

# gerando modelo de regressão conforme ols

X = sm.add_constant(x)
model_regressao = sm.OLS(y, X).fit()
pred = model_regressao.predict(X)

# plot regressão

plt.figure(figsize=(20,10))
plt.title('PRECO MEDIO DO LITRO GASOLINA COMUM 05/2004 a 11/2022')
plt.xlabel('ORDEM SEQUENCIAL DE SEMANAS')
plt.ylabel('PRECO MEDIO LITRO GASOLINA COMUM R$')
sns.scatterplot(x=x, y=y)
sns.lineplot(x=x, y=pred, color="green")

# Previsao para a próxima semana

semana_956 = x.max() + 1

# valor previsto

print(f"Preço Médio de Revenda Gasolina Comum Litro - Previsto Semana 956 => 27/11/2022 a 30/11/2022: R${model_regressao.predict(np.array([1, semana_956]))}")

# erro de Y e o pred

y = np.array( y )
pred = np.array ( pred )

erro = ( y - pred )
#print(erro)

# Calculando media de erro

n = 955
meanError = erro.sum() / n
meanError



plt.figure(figsize=(18,9))
sns.scatterplot(x="N SEQ SEMANA", y="PRECO MEDIO REVENDA", data=df_combustivel)
plt.title('PRECO MEDIO GASOLINA COMUM 05/2004 a 11/2022')
plt.xlabel('Nº DE SEMANA')
plt.ylabel('PRECO MEDIO GASOLINA COMUM')
plt.plot(predictions, 'green', )
plt.show()

