#Escreva um programa que leia um dia da semana, e verifique se
#se é fim de semana (sabado e domingo) ou dia comercial para os demais dias

dias = input('Dia da semana:')
 
match dias:
  case 'Segunda'|'Terça'|'Quarta'|'Quinta'|'Sexta':
      print(f'{dias}- Dia Útil')
  case  'Sábado' | 'Domingo':
      print(f'{dias}- Fim de semana!')  