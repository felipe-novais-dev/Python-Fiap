valortotal = int(input('Valor Total:'))
formadepagamento = (input('Dinheiro ou Cartão:'))

#Se o valor da compra for maior ou igual a 100 e o pagamento for em dinheiro → aplicar 10% de desconto
#Se o valor da compra for maior ou igual a 100 e o pagamento for em cartão → aplicar 5% de desconto
#Se o valor da compra for menor que 100 → não há desconto
    
if (valortotal>= 100 and formadepagamento == 'dinheiro'):
    desconto = valortotal * 0.10
    print(f'{valortotal - desconto } Valor:')
elif (valortotal>= 100 and formadepagamento == 'cartão'):    
    desconto = valortotal * 0.05
    print(f'{valortotal - desconto} Valor:')
elif (valortotal < 100):
    print('Não Há desconto, Seu valor é:')
else :
    print('forma inválida:')    
   
    
