#importando todas as bibliotecas
import xlrd
import pandas as pd
import numpy as np
#Abrindo o arquivo
arq = pd.read_excel(r"C:\Users\Jefferson\Desktop\UFRJ\prog\PROG 2\Exercicio\WHO POP TB some.xls")
#Ordenando lista de forma crescente e printando concomitantemente
print(arq.sort_values('TB deaths'))
