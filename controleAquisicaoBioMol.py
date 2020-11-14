import operacoesCompra as op
print('-' * 100)
print('Digite -1 Para Sair. Escreva os valores Separados por "," \n'
      'Obs: Coloque na ordem "produto,valor,quantidade\n'
      'Coloque um produto por vez" ')
print('-' * 100)
compras = {}
xxx = input('Digite suas Groceries: ')
while xxx != "-1":
    l = xxx.split(',')
    compras.setdefault(str(l[0]), ( float(l[1]), int(l[2]) ) )
    xxx = input('Digite a Proxima entrada: ')
    l = []
op.prod(compras)
print('-'*100)
op.qtd(compras)
print('-'*100)
op.total(compras)
