'''Solicitar o nome do aluno
- Solicitar o número de faltas
- Adicionar a condiçao do aluno realizar o exame
- Aprovaçao - media>=6 e numero de faltas <= 18
- Reprovado - numero de faltas <= 18
Examente - se a mediai for <= 6 e numero >=18
-Obter uma nova nota 
- Calcular uma nova media
-Verificaçao se aprovado ou reprovado'''

print('---Nome do Aluno---')
nome = str(input('Nome do Aluno:'))
print('---Número de Faltas---')
faltas = int(input('Número de Faltas:'))
print('---Calculando a Média---')
n1 = float(input('Nota 1: ')) 
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
media = (n1+n2+n3)/3

print('Media: ', media)
if (faltas> 18):
 print ('Reprovado!')
elif  (media >= 6):   
   print('Aprovado!')
else :
  print('Recuperaçao')
  n4 = float(input('Nota 4: '))
  media2 = (n1+n2+n3+n4)/4
  if (media2>= 6):
    print('Aprovado')
  else :
    print('Reprovado')
