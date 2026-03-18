'Exercicio 1:'
'escreva um programa para calcular o valor de uma conta de energia eletrica de um consumidor com base no consumo em kwh'
"Consumo <150kwh  - 0,75"
" 150 >=consumo < 500kwh -0,95!"
"consumo >= 500     1,20"
"Valor minimo 45,00"
"O programa deve imprimir o consumo em Kwh"

print('---Calculando a conta de energia---')
consumo  = float(input('Consumo(kwh):'))
valor_minimo = 45.90


if consumo<150:
    preco_kwh =   consumo *0.75 

elif consumo>150:
   preco_kwh = consumo *0.95
else :
   preco_kwh = consumo *0.95

valor_conta = (consumo * preco_kwh) + valor_minimo
print(f'{valor_conta} Valor da conta:')
