# importando todas as bibliotecas
import sys
import xlrd
import pandas as pd
import numpy as np
#Pegando entrada
entrada = sys.argv[1::]
arq = entrada[0]
b = float(entrada[1])
m = float(entrada[2])
# Copiando arquivo
df = pd.read_excel(arq).copy()
# Passando colunas selecionadas
df_q = df[['Target_Name', 'Stage']].copy()
# Criando coluna
df_q["Quantity"] = 10 ** ((df[('CT')].copy() - b) / m)
#Juntando colunas
df_final = pd.merge(df.copy(),df_q.copy())
#Criando arquivo .xlsx Final
saida = pd.ExcelWriter(r"FINAL.xlsx")
df_final.to_excel(saida, 'Aba')
#Salvando arquivo
saida.save()
#Printando Lista final
print(df_final)
