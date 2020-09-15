#Abrindo o arquivo texto
arq = open(r"C:\Users\Jefferson\Desktop\UFRJ\prog\Tac-1-2\TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta")
#Pedindo o usuario pelo nome do arquivo especifico.
gene = input("Digite o gene para busca:")
l = ''
# for para procurar pelo arquivo pedido.
for linha in arq:
    if gene in linha:
# Se o arquivo é encontrado pegamos o nome e tiramos o resto após o | .
        nome = linha.split("|")
# Printamos o cabeçalho
        print("Cabeçalho:", nome[0])
#For usado para concatenar as strings tirando tabulação e quebra de linha.
        for linha2 in arq:
            # Ao encontrar o inicio da proxima proteina fechamos o for com um break usando if.
            if '>' in linha2:
                break
            l = l + linha2.replace('\n','')
#apos a concatenação e o break printamos na tela a sequencia.
        print("Sequencia:", l)
#Por fim fechamos o arquivo texto.
arq.close()