#Questão 2 do Caderno de Atividade Prática Uninter
#Desenvolvido por GCNF

from time import sleep

print('Bem Vindo a Pizzaria do Guilherme Cerqueira Nunes de França RU:4159028')

print('-' * 24, 'Cardápio', '-' * 24)
print('''
| Código | Descrição	| Pizza Média  	| Pizza Grande |
| 21	 | Napolitana	| R$ 20,00	| R$ 26,00     |
| 22	 | Margherita	| R$ 20,00	| R$ 26,00     |
| 23	 | Calabresa	| R$ 25,00	| R$ 32,50     |
| 24	 | Toscana	| R$ 30,00	| R$ 39,00     |
| 25	 | Portuguesa	| R$ 30,00	| R$ 39,00     |
''')
print('-' * 58)

valor_total = 0

while True:
    tamanho = input('Entre com o tamanho da pizza (M/G): ').upper()

    if tamanho == 'M':
        tamanho = 'M'
        
    elif tamanho == 'G':
        tamanho = 'G'
    
    else:
        print('Valor Inválido!')
        sleep(1)
        print('Digite novamente!')
        sleep(1)
        continue

    while True:
        valor = 0 
        sabor = input('Entre com código do sabor desejado: ')
        
        if sabor == '21':
            print('Você pediu uma pizza de Napolitana! ')
            valor += 20
            
        elif sabor == '22':
            print('Você pediu uma pizza de Margherita!')
            valor += 20
            
        elif sabor == '23':
            print('Você pediu uma pizza de Calabresa!')
            valor += 25
            
        elif sabor == '24':
            print('Você pediu uma pizza de Toscana!')
            valor += 30
            
        elif sabor == '25':
            print('Você pediu uma pizza de Portuguesa!')
            valor += 30
            
        else:
            print('Código Inválido!')
            sleep(1)
            print('Digite Novamente!')
            continue
        
        if tamanho == 'G':
            valor = valor + (valor * 30/100)
            
        else:
            pass
        
        valor_total += valor
        
        while True:
            con = input('''Deseja pedir mais alguma coisa? 
                    1- Sim
                    2- Não
                    --> ''')
        
            if con == '1':
                break
            
            elif con == '2':
                print(f'O total a ser pago é: R${valor_total:.2f}')
                sleep(1)
                quit()
            
            else:
                print('Digite valor válido!')
                sleep(1)
                
        if con == '1':
            break
