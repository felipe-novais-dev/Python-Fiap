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


'''Solicitar o nome do aluno
- Solicitar o número de faltas
- Adicionar a condiçao do aluno realizar o exame
- Aprovaçao - media>=6 e numero de faltas <= 18
- Reprovado - numero de faltas <= 18
Examente - se a mediai for <= 6 e numero >=18
-Obter uma nova nota 
- Calcular uma nova media
-Verificaçao se aprovado ou reprovado'''