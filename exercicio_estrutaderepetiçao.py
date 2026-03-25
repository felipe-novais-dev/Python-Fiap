'''
Escreva um programa que leia um valor inicial e um valor final
O programa deve imrpimir todos os numeros compreendidos entre 
o valor inicial e o valor final

'''

inicio = int(input('Inicio: '))
final = int(input('Fim:'))

while inicio<= final:
    print(inicio)
    inicio = inicio + 1