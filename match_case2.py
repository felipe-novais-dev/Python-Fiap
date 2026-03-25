nome = input('Nome:')

match nome:
    case 'Jose'|'JOSÉ'|'josé':
        print(f'{nome}- Nome válido')
    case 'Maria'|'maria'|'MARIA':   
         print(f'{nome}- Nome válido')
    case 'Pedro'|'PEDRO'|'pedro':
          print(f'{nome}- Nome válido')
    case _:
          print(f'{nome}- Nome Inválido')
                