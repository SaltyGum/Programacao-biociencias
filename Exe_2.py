#importando todas as bibliotecas
import xlrd
import pandas as pd
import numpy as np
#Abrindo o arquivo
arq = pd.read_excel(r"C:\Users\Jefferson\Desktop\UFRJ\prog\PROG 2\Exercicio\WHO POP TB some.xls")
# Declarando variaveis
x = 0
TotMort = 0
#Pegando tamanho da lista
y = len(arq['TB deaths'])
#Rodando a lista somando os valores
while x < y:
    TotMort += arq.loc[x,'TB deaths']
    x += 1
#Printando Resposta
print(TotMort)