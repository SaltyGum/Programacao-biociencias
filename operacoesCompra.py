def prod(xxx):
    for blob in xxx:
        print(blob)


def qtd(xxx):
    for blob in xxx:
        print(blob, ' ', xxx[blob][1])


def total(xxx):
    tot = 0
    for blob in xxx:
        print(blob, ' ', xxx[blob][1], 'X', xxx[blob][0], '=', xxx[blob][0]*xxx[blob][1])
        tot += xxx[blob][0]*xxx[blob][1]
    print('Total=',tot)
