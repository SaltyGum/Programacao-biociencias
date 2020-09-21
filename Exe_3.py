#importando todas as bibliotecas
import xlrd
import pandas as pd
import numpy as np
#Abrindo o arquivo
arq = pd.read_excel(r"C:\Users\Jefferson\Desktop\UFRJ\prog\PROG 2\Exercicio\WHO POP TB some.xls")
#Pegando lista Crescente
x = arq.sort_values('TB deaths')
#Pegando Numero de valores da lista e retirando 1 por conta do python começar em 0
y = len(x['TB deaths']) - 1
#Retirando Primeiro e Ultimo valor
Maior = x.iloc[[y],[-1]]
Menor = x.iloc[[0],[-1]]
#Printando valores
print('Maior numero:%s\nMenor numero:%s ' %(Maior,Menor))
