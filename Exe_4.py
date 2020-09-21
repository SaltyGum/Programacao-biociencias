#importando todas as bibliotecas
import xlrd
import pandas as pd
import numpy as np
#Abrindo o arquivo
arq = pd.read_excel(r"C:\Users\Jefferson\Desktop\UFRJ\prog\PROG 2\Exercicio\WHO POP TB some.xls")
#Pegando lista Crescente
df = arq.sort_values('TB deaths')
df['TB deaths'] = df['TB deaths'].astype(int)
# Declarando variaveis
x = 0
media = 0
mediana = 0
num=0
#Pegando tamanho da lista
y = len(arq['TB deaths'])
if y % 2 == 0:
    #Pegando posição central da lista crescente
    z = y//2
    #Jogando na variavel
    num = df.iloc[[z][-1]]
    #Pegando segunda posição central
    z = z - 1
    num += df.iloc[[z][-1]]
    #Colocando em uma variavel do tipo int
    valor = num[-1]
elif y % 2 == 1:
    #Pegando posição central da lista crescente
    z = y//2
    #Jogando na variavel
    mediana = df.iloc[[z], [-1]]
#Rodando a lista somando os valores
while x < y:
    media += arq.loc[x,'TB deaths']
    x += 1
#calculando mediana
mediana = valor / 2
#Calculando media
media = media/12
#Printando Resposta
print('Media de mortos:',media,'\nMediana de mortos:',mediana)
