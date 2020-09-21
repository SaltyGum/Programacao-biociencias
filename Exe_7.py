#importando todas as bibliotecas
import xlrd
import pandas as pd
import numpy as np
#Abrindo o arquivo
arq = pd.read_excel(r"C:\Users\Jefferson\Desktop\UFRJ\prog\PROG 2\Exercicio\WHO POP TB some.xls")
# Declarando variaveis
brics = ["RUSSIAN FEDERATION","INDIA","CHINA","SOUTH AFRICA","BRAZIL"]
x = 0
TotMort = 0
#Pegando tamanho da lista
y = len(arq['Country'])
#Rodando a lista somando os valores
while x < y:
    p = arq.loc[x,'Country']
    if p.upper() in brics:
        TotMort += arq.loc[x,'TB deaths']
    x += 1
#Printando total de mortes no BRICS
print('Total de mortos no BRICS:',TotMort)
#Calculando media de mortes no BRICS
media = TotMort/5
#Printando media de mortes no BRICS
print('Media de mortes no BRICS:',media)