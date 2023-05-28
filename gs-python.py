'''preciso criar um programa que realize cadastro de empresas e ONG's, onde empresas e ONGs se cadastram As ONGs anunciam campanhas e ações q elas vão fazer, as empresas encontram qual campanha elas querem patrocina.
É um intermediador entre os dois, pra q as empresas não precisem sair pesquisando por aí, e as ONGs aparecem pra mais empresas'''

def separador(n, cor):
    cores = {
        1: {'azul': '\033[36m', 'limpa' : '\033[0m'},
        2: {'verde': '\033[32m', 'limpa' : '\033[0m'},
        3: {'roxo' : '\033[95m' , 'limpa' : '\033[0m'},
        4: {'amarelo': '\033[33m', 'limpa': '\033[0m'}
    }
    #separador do meno
    if cor == 1:
        mensagem = print(f'{cores[1]["azul"]}-={cores[1]["limpa"]}' * n)
    #separador do if de ONG
    elif cor == 2:
        mensagem = print(f'{cores[2]["verde"]}-={cores[2]["limpa"]}' * n)
    #separador do if de empresas
    elif cor == 3:
        mensagem = print(f'{cores[3]["roxo"]}-={cores[3]["limpa"]}' * n)
    #separador do if de doação
    else:
        mensagem = print(f'{cores[4]["amarelo"]}-={cores[4]["limpa"]}' * n)
    return mensagem

def validacao_s_n(val, mensagem):
    while val != "s" and val != "n":
        print("Opção inválida!")
        val = print(mensagem)
    return val

def validacao_oe(val):
    while val != '1' and val != '2' and val != '3':
        val = input('Opção inválida\n1- ONG\n2- Empresa\n3- Doação')
    return val
#Programa principal
option = 1
cor = {'vermelho': '\033[31m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'azul':'\033[36m', 'roxo' : '\033[35', 'limpa' : '\033[0m'}
ong = ['FomeZero', 'Saciar Vidas', 'Prato Cheio', 'Pão e Compaixão', 'Alimentando Sonhos']
empresa = ['Innovia', 'Elixir Industries', 'Apex Innovations', 'Zephyr Enterprises', 'PulseTech']

while option != 0:
    separador(50, 1)
    ong_or_empresa = input("Bem vindo à nossa plataforma!\nAqui efetuamos um cadastro no qual encontraremos a melhor opção para sua empresa ou ONG!\nNossos serviços também possibilitam a doação de dinheiro através de pix!\nDigite a opção correspondente para seu cadastro ↓\n1- ONG\n2- Empresa\n3- Doação\n")

    ong_or_empresa = validacao_oe(ong_or_empresa)
    separador(50, 1)

    if ong_or_empresa == 1:

        email = input('Email: ')
        senha = input('Senha: ')
        cell = input('Celular: ')
        nome = input('Nome da ONG: ')
        proposta = input('Escreva um pouco sobre a sua proposta para seus futuros patrocinadores↓\n')
        cnpj = input('CNPJ: ')

