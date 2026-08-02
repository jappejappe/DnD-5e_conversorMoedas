DEFAULT = ("\x1b[0m")
WHITE = ("\033[37m")
RED = ("\033[31m")
GREEN = ("\033[32m")
YELLOW = ("\033[33m")
BLUE = ("\033[34m")
BOLD = ("\033[1m")
contagem = ('')

print(f'{RED}Bem vindo ao conversor de moedas de D&D 5E!{DEFAULT}\nFunciona de forma simples e rápida.\n')

while contagem.upper() != ('N'):

    print(f'{YELLOW}(0){DEFAULT} Sair\n{YELLOW}(1){DEFAULT} Peças de cobre\n{YELLOW}(2){DEFAULT} Peças de prata\n{YELLOW}(3){DEFAULT} Peças de Electro\n{YELLOW}(4){DEFAULT} Peças de ouro\n{YELLOW}(5){DEFAULT} Peças de platina')
    
    while True:
        try:
            tipo = int(input(f'\n{YELLOW}Moeda que você tem: {DEFAULT}'))
            quantidade = int(input(f'{YELLOW}Quantidade de moedas: {DEFAULT}'))
            moedaDesejada = int(input(f'{YELLOW}Moeda desejada: {DEFAULT}'))
            break

        except:
            print('Insira um valor válido')

    if tipo <= 0 or quantidade <= 0 or moedaDesejada <= 0:
        break
    if tipo >= 6  or moedaDesejada >= 6:
        print('Escolha uma moeda válida, tente novamente\n\n')



    if moedaDesejada == 1:
        material = ('cobre')

    elif moedaDesejada == 2:
        material = ('prata')

    elif moedaDesejada == 3:
        material = ('electro')

    elif moedaDesejada == 4:
        material = ('ouro')

    elif moedaDesejada == 5:
        material = ('platina')


    if tipo == moedaDesejada:
        print('Você não pode converter uma moeda para ela mesma, tente novamente\n\n')


    if tipo > moedaDesejada:

        # conversão para moedas menores

        if tipo == 5 and moedaDesejada == 4:
            x = quantidade * 10
            print('\nVocê tem um total de', x, 'moedas de', material)

        elif tipo == 5 and moedaDesejada == 3:
            x = quantidade * 20
            print('\nVocê tem um total de', x, 'moedas de', material)

        elif tipo == 5 and moedaDesejada == 2:
            x = quantidade * 100
            print('\nVocê tem um total de', x, 'moedas de', material)

        elif tipo == 5 and moedaDesejada == 1:
            x = quantidade * 1000
            print('\nVocê tem um total de', x, 'moedas de', material)

        elif tipo == 4 and moedaDesejada == 3:
            x = quantidade * 2
            print('\nVocê tem um total de', x, 'moedas de', material)

        elif tipo == 4 and moedaDesejada == 2:
            x = quantidade * 10
            print('\nVocê tem um total de', x, 'moedas de', material)

        elif tipo == 4 and moedaDesejada == 1:
            x = quantidade * 100
            print('\nVocê tem um total de', x, 'moedas de', material)

        elif tipo == 3 and moedaDesejada == 2:
            x = quantidade * 5
            print('\nVocê tem um total de', x, 'moedas de', material)

        elif tipo == 3 and moedaDesejada == 1:
            x = quantidade * 50
            print('\nVocê tem um total de', x, 'moedas de', material)

        elif tipo == 2 and moedaDesejada == 1:
            x = quantidade * 10
            print('\nVocê tem um total de', x, 'moedas de', material)



    else:
        # conversão para moedas maiores

        if tipo == 1 and moedaDesejada == 2:
            numero = 10
            x = quantidade // numero
            y = quantidade % numero
            if y != 0:
                print('\nVocê tem um total de', x, 'moedas de', material, 'e restam', y, )
            else: print('\nVocê tem um total de', x, 'moedas de', material)

        elif tipo == 1 and moedaDesejada == 3:
            numero = 50
            x = quantidade // numero
            y = quantidade % numero
            if y != 0:
                print('\nVocê tem um total de', x, 'moedas de', material, 'e restam', y, )
            else: print('\nVocê tem um total de', x, 'moedas de', material)

        elif tipo == 1 and moedaDesejada == 4:
            numero = 100
            x = quantidade // numero
            y = quantidade % numero
            if y != 0:
                print('\nVocê tem um total de', x, 'moedas de', material, 'e restam', y, )
            else: print('\nVocê tem um total de', x, 'moedas de', material)

        elif tipo == 1 and moedaDesejada == 5:
            numero = 1000
            x = quantidade // numero
            y = quantidade % numero
            if y != 0:
                print('\nVocê tem um total de', x, 'moedas de', material, 'e restam', y, )
            else: print('\nVocê tem um total de', x, 'moedas de', material)

        elif tipo == 2 and moedaDesejada == 3:
            numero = 5
            x = quantidade // numero
            y = quantidade % numero
            if y != 0:
                print('\nVocê tem um total de', x, 'moedas de', material, 'e restam', y, )
            else: print('\nVocê tem um total de', x, 'moedas de', material)

        elif tipo == 2 and moedaDesejada == 4:
            numero = 10
            x = quantidade // numero
            y = quantidade % numero
            if y != 0:
                print('\nVocê tem um total de', x, 'moedas de', material, 'e restam', y, )
            else: print('\nVocê tem um total de', x, 'moedas de', material)

        elif tipo == 2 and moedaDesejada == 5:
            numero = 100
            x = quantidade // numero
            y = quantidade % numero
            if y != 0:
                print('\nVocê tem um total de', x, 'moedas de', material, 'e restam', y, )
            else: print('\nVocê tem um total de', x, 'moedas de', material)

        elif tipo == 3 and moedaDesejada == 4:
            numero = 2
            x = quantidade // numero
            y = quantidade % numero
            if y != 0:
                print('\nVocê tem um total de', x, 'moedas de', material, 'e restam', y, )
            else: print('\nVocê tem um total de', x, 'moedas de', material)

        elif tipo == 3 and moedaDesejada == 5:
            numero = 20
            x = quantidade // numero
            y = quantidade % numero
            if y != 0:
                print('\nVocê tem um total de', x, 'moedas de', material, 'e restam', y, )
            else: print('\nVocê tem um total de', x, 'moedas de', material)

        elif tipo == 4 and moedaDesejada == 5:
            numero = 10
            x = quantidade // numero
            y = quantidade % numero
            if y != 0:
                print('\nVocê tem um total de', x, 'moedas de', material, 'e restam', y, )
            else: print('\nVocê tem um total de', x, 'moedas de', material)
        
    contagem = input('Deseja fazer outra conversão? (y/n) ')
print(f'{BLUE}Volte sempre!{DEFAULT}')
input('\npressione Enter para sair')