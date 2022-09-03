#Questão 4 do Caderno de Atividade Prática Uninter

#Váriavel de Indentificação do aluno
aluno = 'Guilherme Cerqueira Nunes de França'
ru = 'RU: 4159028'

#Importação da função sleep
from time import sleep

#Funções do Código
#Contra comentarios no codigo

def volumefeijoada(): #Função que vai definir o volume da feijoada
    global valor_volume
    
    print('-=-' * 30)
    print('Menu Volume Feijoada')
    print('-=-' * 30)
    
    try:
        volume = int(input('Entre com a quantidade que deseja(ml): '))
    
    except:
        print('ERRO! Valor digitado é inválido!')
        sleep(1)
        print('Tente Denovo!')
        return volumefeijoada()
        
    else:
        if volume >= 300 and volume <=5000:
            valor_volume = volume * 0.08
            
        else:
            print('Não aceitamos porções menores que 300ml ou maiores que 5L. Tente Novamente!')
            sleep(1)
            return volumefeijoada()
        
    
def opcaofeijoada():
    global valor_opcao
    
    print('-=-' * 30)
    print('Entre com a opção de Feijoada')
    print('-=-' * 30)
    
    opcao = input('''B- Básica (Feijão + Paiol + Costelinha) 
P- Premium (Feijão + Paiol + Costelinha + Partes de Porco)
S- Suprema (Feijão + Paiol + Costelinha + Partes de Porco + Charque + Calabresa + Bacon)
--> ''').upper()
    
    if opcao == 'B':
        valor_opcao = 1.00
        
    elif opcao == 'P':
        valor_opcao = 1.25
        
    elif opcao == 'S':
        valor_opcao = 1.50
        
    else:
        print('Digite uma opção válida!')
        sleep(1)
        return opcaofeijoada()
        
        
def acompanhamentofeijoada():
    global valor_adicional
    valor_adicional = 0
    
    while True:
        print('-=-' * 30)
        print('Deseja mais algum acompanhamento:')
        print('-=-' * 30)
        
        adicional = input('''0- Não desejo mais nenhum acompanhamento
1- 200g de Arroz
2- 150g de farofa especial
3- 100g de couve cozida 
4- 1 laranja descascada ''')
        
        if adicional == '1':
            valor_adicional += 5.00
            
        elif adicional == '2':
            valor_adicional += 6.00
            
        elif adicional == '3':
            valor_adicional += 7.00
            
        elif adicional == '4':
            valor_adicional += 3.00
            
        elif adicional == '0':
            print('Encerrando pedido...')
            sleep(1)
            break
    
        else:
            print('Digite uma opção válida!')

#Programa Principal

volumefeijoada()
opcaofeijoada()
acompanhamentofeijoada()

total = (valor_volume * valor_opcao) + valor_adicional

print(f'O valor a ser pago é (R$): {total:.2f} (Volume = {valor_volume:.2f} * Opção = {valor_opcao:.2f} + Acompanhamento = {valor_adicional:.2f})')

#Desenvolvido por GCNF
