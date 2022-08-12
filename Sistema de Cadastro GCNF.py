#Desenvolvido por GCNF

from time import sleep
from random import choice
from random import randint

#Banco de Dados
banco_dados     = dict()
banco_usu       = dict()
banco_prin      = dict()
banco_email     = dict()
registro_email  = list()
contas          = dict()

#Funções do programa
def cadastro():
    global nome

    def usuario():
        global usu
        global key_dic_usu
        
        while True:
            while True:
                usu = input('\033[1;33mDigite um nome de usuário: \033[m').strip()

                if usu in contas:
                    print('\033[1;31mEsse nome de usuário já existe\033[m')
                    sleep(1)
                    print('\033[1;31mTente outro!\033[m')
                    print('\033[1;34m-=-\033[m' *30)

                elif len(usu) == 0:
                    print('\033[1;31mNão deixe em branco!\033[m')
                    sleep(1)

                else:
                    break

            while True:
                confirm_usu = input('\033[1;33mConfirma esse usuário? [S/N] \033[m').upper()
            
                if confirm_usu == 'S':
                    print(f'\033[1;32mOk, seu usuario será {usu}\033[m')
                    sleep(1)
                    print('\033[1;34m-=-\033[m' * 30)
                    break

                elif confirm_usu == 'N':
                    print('\033[1;33mOk, vamos refazer seu usuário!\033[m')
                    return(usuario())

                else:
                    print('\033[1;31mValor Inválido!\033[m')

            if confirm_usu == 'S':
                criar_email()

                while True:
                    print('-=-' *30)
                    senha = input('\033[1;34mCrie uma senha: \033[m').strip()

                    if len(senha) < 8:
                        print('\033[1;31mA senha deve ser no minímo 8 caracteres\033[m')
                        sleep(1)
                        continue

                    senhacon = input('\033[1;34mConfirme a senha: \033[m').strip()
  
                    if senha != senhacon:
                        print('\033[1;31mDigite a senha novamente!\033[m')
                        sleep(1)

                    else:
                        banco_usu['Usuario'] = usu
                        banco_usu['Senha'] = senha

                        key_dic_usu = usu
                        banco_prin['Usu']   = banco_usu.copy()
                        banco_prin['Dados'] = banco_dados.copy()

                        contas[key_dic_usu] = banco_prin.copy() 
                        banco_email['Email'] = email_cadastro
                        banco_email['Senha'] = senha
                        registro_email.append(email_cadastro)
                        contas[key_dic_usu]['Gmail'] = banco_email.copy()

                        banco_dados.clear()
                        banco_usu.clear()
                        banco_prin.clear()
                        banco_email.clear()

                        print('\033[1;31mSeu cada\033[1;33mstro foi\033[1;32m criado c\033[1;34mom sucesso!\033[m')
                        sleep(1)
                        print('\033[1;31mFaça log\033[1;33min ou cri\033[1;32me outro c\033[1;34madastro!\033[m')
                        sleep(1)
                        break
                break
            break
    #Cadastro: Entrada de Dados
    while True:
        try:
            nome = str(input('\033[1;32mInforme seu nome: ')).capitalize().strip()
            if len(nome) == 0:
                print('\033[1;31mNão deixe em branco!\033[m')
                continue

            idade = int(input('Informe sua idade: '))

            if idade < 18:
                print('\033[1;31mInfelizmente você não pode cadastrar! Espere ficar de maior!\033[m')
                sleep(1)
                print('\033[1;34m-=-\033[m' *30)
                break

            peso  = float(input('Informe seu peso: '))

        except:
            print('\033[1;31mPreencha os dados corretamente!\033[m')
            sleep(1)
            continue

        while True:
            try:
                cpf = input('\033[1;32mInforme seu CPF: ')

                if cpf.isnumeric() == True:
                    vericpf = len(cpf)

                else:
                    print('\033[1;31mValor Inválido\033[m')
                    sleep(1)
                    continue

            except (TypeError, ValueError):
                print('\033[1;31mERRO! O tipo de dados incorreto!\033[m')
                sleep(1)
                continue
            
            if vericpf < 11 or vericpf > 11:
                print('\033[1;33mCPF Inválido!\033[m')
                sleep(1)
                continue
            
            else:
                banco_dados['CPF'] = cpf
                break
            
        print('-=-' * 30)
        print(f'''\033[1;36mConfira seus dados:
        Nome: {nome}
        Idade:{idade}
        Peso: {peso}
        CPF:  {cpf}\033[m''')
        print('\033[1;34m-=-\033[m' * 30)

        while True:
            #Confirmação Dados
            con = input('''\033[1;32mSeus dados estão corretos?
            1- Sim
            2- Não
            3- Cancelar Cadastro
            ---> \033[m''')

            if con == '1':
                banco_dados['Nome']  = nome
                banco_dados['Idade'] = idade
                banco_dados['Peso']  = peso
                banco_dados['CPF']   = cpf

                sleep(1)
                break

            elif con == '2':
                print('\033[1;33mOk, vamos refazer os dados!\033[m')
                sleep(1)
                break
            
            elif con =='3':
                print('\033[1;33mCancelando Cadastro\033[m')
                sleep(1)

            else:
                print('\033[1;31mValor inválido!\033[m')
                sleep(1)

        if con == '1':
            print(f'\033[1;34mOk {nome}, vamos criar seu  usuário\033[m')
            sleep(1)
            print('\033[1;34m-=-\033[m' * 30)
            return usuario()

        elif con == '3':
            break


def criar_email():
    global email_cadastro

    def email_sugestao():
        global gmail_color

        print('\033[1;31mSuges\033[1;33mtões \033[1;32mde em\033[1;34mail: \033[m') 
        gmail_color = '\033[1;31m@gm\033[1;33mai\033[1;32ml.\033[1;34mcom\033[m'
        cont = 0

        while cont <3:
            num = [0]
            num_ale = randint(1, 70)

            if num_ale in num:
                continue

            num.append(num_ale)
            su = f'\033[1;32m{nome.lower()}{num_ale}{gmail_color}'
            if su in contas:
                continue

            print(su)
            cont += 1

    #Criação do Email
    email_sugestao()
    while True:
        email_cadastro = input(f'\033[1;31mEscolh\033[1;33ma um end\033[1;32mereço d\033[1;34me email \n[{gmail_color} \033[1;32mjá adicionado]:  \033[m')

        if len(email_cadastro) == 0:
            print('\033[1;31mNão deixe em branco\033[m')
            continue

        elif '@gmail.com' in email_cadastro: #Essa condição não está funcioando
            email_cadastro.replace(gmail_color, ' ')
            email_cadastro = f'\033[1;32m{email_cadastro}\033[m{gmail_color}'

        elif '@gmail.com' not in email_cadastro:
            email_cadastro = f'\033[1;32m{email_cadastro}\033[m{gmail_color}'

        try:
            
            if email_cadastro in registro_email:
                print('\033[1;31mEsse endereço de email já existe!\033[m')
                sleep(1)
                print('\033[1;33mTente outro!\033[m')
                sleep(1)
                continue
            
        except:
            pass

        print(f'{email_cadastro}')
        while True:
            print('\033[1;34m-=-\033[m' *30)
            confirm_email = input('\033[1;31mConf\033[1;33mirma\033[1;32m esse\033[1;34m email? [S/N] --> \033[m').upper()

            if confirm_email == 'S':
                break

            elif confirm_email == 'N':
                print('\033[1;33mVamos refazer!\033[m')
                sleep(1)
                break

            else:
                print('\033[1;31mValor Inválido!\033[m')
                sleep(1)

        if confirm_email == 'S':
            break


def area_login():
    def login():
        while True:
            usuaces = input('\033[1;32mInforme seu usuário: ').strip()
            senhaaces = input('Informe sua senha:\033[m').strip()

            if usuaces not in contas or senhaaces != contas[usuaces]['Usu']['Senha']:
                print('\033[1;31m-=-' * 30)
                print('Senha ou Usuário foi digitado errado!\033[m')
                sleep(1)

            #Sistema de logar com email ainda não foi colocado

            else:
                print('\033[1;31m-=-\033[m' * 30)
                print('\033[1;31mBem Vi\033[1;33mndo a p\033[1;32mlataf\033[1;34morma!\033[m')
                print('\033[1;34m-=-\033[m' * 30)

                while True:
                    op = input(f'''\033[1;34m1- Ver seus dados de cadastro
                    2- Ver usuário e senha
                    3- Ver Email cadastrado
                    4- Área de Jogos
                    5- Sair da conta
                    ---> \033[m''')

                    if op == '1':
                        for k, v in contas[usuaces]['Dados'].items():
                            print(f'\033[1;36m{k}: {v}\033[m')

                    elif op == '2':
                        mostrar_usu = contas[usuaces]['Usu']['Usuario']
                        mostrar_senha = contas[usuaces]['Usu']['Senha']

                        print(f'\033[1;32mSeu Usuario:\033[1;34m {mostrar_usu}\033[m')
                        print(f'\033[1;32mSua senha:\033[1;34m {mostrar_senha}\033[m')

                    elif op == '3':
                        mostrar_email = contas[usuaces]['Gmail']['Email']
                        print(f'\033[1;33mEmail cadastrado:\033[m {mostrar_email}')

                    elif op == '4':
                        jogos()

                    elif op == '5':
                        print(f'\033[1;32mObrigado {usuaces} por usar nossa plataforma, até mais!\033[m')
                        sleep(1)
                        break

                    else:
                        print('\033[1;31mValor Invalido !\033[m')
            
            break

    #Área de Login
    while True:
        print('-=-' * 30)
        login_con = input(f'''\033[1;36mDeseja logar em sua conta?
        1- Sim 
        2- Não(Fechar Programa)
        3- Voltar Inicio
        ---> \033[m''')

        print('\033[1;34m-=-\033[m' * 30)

        if login_con == '1':
            print('\033[1;33mOk vamos fazer Login!\033[m')
            sleep(1)
            login()

        elif login_con == '2':
            print('\033[1;33mok, vamos encerrar o programa!\033[m')
            sleep(1)
            print(f'\033[1;37mObrigado por testar esse humilde programinha\033[m')
            quit()

        elif login_con == '3':
            print('\033[1;33mVoltando...\033[m')
            sleep(1)
            break

        else:
            print('\033[1;31mValor Inválido!\033[m')
            sleep(1)


def jogos():
    def jokenpo():
        ia = ['Pedra', 'Papel', 'Tesoura']
        opçao = ['Pedra', 'Papel', 'Tesoura']

        frase = ('JO', 'KEN', 'PÔ')
        while True:

            jogador = str(input('''\033[1;34mEscolha: 
        1- Pedra
        2- Papel
        3- Tesoura
        --->\033[m''')).upper()

            if jogador == '1':
                jogador = 'Pedra'
                
            elif jogador == '2':
                jogador = 'Papel'
                
            elif jogador == '3':
                jogador = 'Tesoura'
                
            else:
                print('\033[1;31mValor invalido!\033[m')
                sleep(1)
                print('-=-' *30)
                continue
            
            escolha_ia = choice(ia)

            for pos in frase:
                sleep(0.5)
                print(f'\n \033[1;36m{pos}\033[m', end='')
                

            print('-=-' * 30)
            print(f'\033[1;34mSUA ESCOLHA FOI: {jogador}\033[m')
            

            if jogador == 'Pedra' and escolha_ia == 'Tesoura':
                print(f'\033[1;32mParabéns voce ganhou! {jogador} mata {escolha_ia}\033[m' )

            elif jogador == 'Papel' and escolha_ia ==  'Pedra':
                print(f'\033[1;32mParabéns voce ganhou! {jogador} mata {escolha_ia}\033[m' )

            elif jogador == 'Tesoura' and escolha_ia == 'Papel':
                print(f'\033[1;32mParabéns voce ganhou! {jogador} mata {escolha_ia}\033[m' )

            elif jogador == escolha_ia:
                print(f'\033[1;33m{jogador} contra {escolha_ia} ! DEU EMPATE!\033[m')

            else:
                print(f'\033[1;31mHAHA VOCÊ PERDEU!!! {escolha_ia} mata {jogador}\033[m')

            while True:
                print('-=-' *30)
                con = input('\033[1;36mDeseja jogar mais uma partida? [S/N] --> \033[m').upper()

                if con == 'S':
                    print('\033[1;32mVamos jogar mais uma partida!\033[m')
                    sleep(1)
                    print('-=-' *30)
                    break

                elif con == 'N':
                    print('\033[1;33mSaindo de Jokenpô!\033[m')
                    sleep(1)
                    print('\033[1;34m-=-\033[m' *30)
                    break

                else:
                    print('\033[1;31mValor Inválido!\033[m')
                    sleep(1)
            if con == 'N':
                break


    def confirm_jogos(): #Função ta inútil, ainda não usada
        while True:       
            con = input('Deseja jogar outra partida? [S/N] --> ').upper()
            if con == 'S':
                print('Ok vamos jogar outra partida!')
                sleep(1)
                print('~~~~' * 30)
                break

            elif con == 'N':
                print('Ok, até mais !')
                break

            else:
                print('Digite um valor válido!')

    #Escolher Jogos
    while True:
        opçao_jogo = input('''\033[1;36mEscolha seu jogo:
        [1]- Jokenpo
        [sair]- Sair da área de jogos
        ---> \033[m''').upper().strip()
        
        if opçao_jogo == '1':
            jokenpo()

        elif opçao_jogo == 'SAIR':
            break

        else:
            print('\033[1;31mValor Inválido!\033[m')
            

#Programa Principal

while True:
    op = input('''\033[1;34m1- Fazer cadastro
2- Login
3- Fechar Programa
--> \033[m''')

    if op == '1':
        cadastro()

    elif op == '2':
        area_login()

    elif op == '3':
        print('\033[1;34mFechando programa\033[m')
        sleep(1)
        print(f'\033[1;37mObrigado por testar esse humilde programinha\033[m')
        print('\033[1;44;32mDev GCNF\033[m')
        quit()

    else:
        print('\033[1;31mValor Inválido!\033[m')

#Desenvolvido por GCNF
