#importando biblioteca
import csv
#Abrindo arquivo
with open(r"C:\Users\Jefferson\Desktop\UFRJ\prog\Tac-1-2\species.csv") as arq:
#facilitando acesso ao leitor
    leitor = csv.reader(arq)
#For para rodar a lista
    for lista in leitor:
        #Argumento de decisão para busca
        if lista[3].upper().rstrip() == "BIRD":
            #Print do resultado
            print("%s\t%s\t%s\t%s" % (lista[0], lista[1], lista[2], lista[3].rstrip()))