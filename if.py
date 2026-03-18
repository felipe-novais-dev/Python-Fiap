'''
Escreva um programa em Python para calcular a média arimética de um aluno
, considerando 3 notas. O programa deve apresentar a media obtido
'''

print('---Calculando a Média---')
n1 = float(input('Nota 1: ')) 
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))


#Processamento
media = (n1+n2+n3)/3
#Saída de Dados
print('Media: ',)

#Estrturas condicionais
if media >= 6:
    print('Aprovado!')
else:
    print('Não Aprovado!')

