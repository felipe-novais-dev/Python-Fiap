#match → variável que você quer analisar
#🔹 case → cada valor possível
#🔹 _ → tipo um else (qualquer outro valor)

#💡 Resumindo: é um jeito mais organizado de fazer vários if/elif.



n = (input('Número: '))

match n:   #if
    case 1 | 2 | 3: #elif
        print('opçao 1')
    case 4 | 5:
        print('opçao 2')
    case 6:
        print('opçao 3')
    case _:   #Como se fosse else
        print('Nenhuma das anteriores')  