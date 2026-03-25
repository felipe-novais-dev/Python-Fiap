dia = (input('dia:'))
placa = int(input('Final da placa:'))
match dia:
    case 'Segunda' : 
          if placa == 1| placa == 2:
            print('Nao pode circular') 
          else :
            print('Pode circular')     
    case 'Terça' : 
          if placa == 3| placa == 4:
            print('Nao pode circular') 
          else :
            print('Pode circular')    
    case 'Quarta' : 
          if placa == 5| placa == 6:
            print('Nao pode circular') 
          else :
            print('Pode circular')
    case 'Quinta' : 
          if placa == 7| placa == 8:
            print('Nao pode circular') 
          else :
            print('Pode circular')  
    case 'Sexta' : 
          if placa == 9| placa == 10:
            print('Nao pode circular') 
          else :
            print('Pode circular')     
    case _: 
          print('Final de semana, Pode Circular')      

  #É atribuição → você está guardando um valor na variável =
  #É comparação → você está perguntando se é igual ==

                                                       