'''preciso criar um programa que realize cadastro de empresas e ONG's, onde empresas e ONGs se cadastram As ONGs anunciam campanhas e ações q elas vão fazer, as empresas encontram qual campanha elas querem patrocina.
É um intermediador entre os dois, pra q as empresas não precisem sair pesquisando por aí, e as ONGs aparecem pra mais empresas'''

#Função para printar um separador decorativo
def separador(n, cor):
    cores = {
        1: {'azul': '\033[36m', 'limpa' : '\033[0m'},
        2: {'verde': '\033[32m', 'limpa' : '\033[0m'},
        3: {'roxo' : '\033[95m' , 'limpa' : '\033[0m'},
        4: {'amarelo': '\033[33m', 'limpa': '\033[0m'},
        5: {'vermelho': '\033[31m', 'limpa': '\033[0m'}
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
    elif cor == 5:
        mensagem = print(f'{cores[5]["vermelho"]}-={cores[5]["limpa"]}' * n)
    else:
        mensagem = print(f'{cores[4]["amarelo"]}-={cores[4]["limpa"]}' * n)
    return mensagem

#cada opção selecionada no menu há uma cor para indicar em qual "seção" está. Essa função serve para escolher a cor do separador 
def cor_separador(cor):
    if cor == '1':
        separador(35, 2)
    elif cor == '2':
        separador(35, 3)
    elif cor == '3':
        separador(35, 4)

#Função de validação para respostas de "s" ou "n"
def validacao_s_n(val, mensagem, m):
    while val != "s" and val != "n":
        separador(35, 5)
        print(f'\n{cor["vermelho"]}Opção inválida!{cor["limpa"]}')
        val = input(mensagem).lower().strip()
        separador(35, 5)
    return val

#Função utilizada para escolher a opção de cadastro
def validacao_oe():
    separador(50, 1)
    val = input("Bem vindo à nossa plataforma!\nAqui efetuamos um cadastro no qual encontraremos a melhor opção para sua empresa ou ONG!\nNossos serviços também possibilitam a doação de dinheiro através de pix!\nDigite a opção correspondente para seu cadastro ↓\n1- ONG\n2- Empresa\n3- Doação\n")
    while val != '1' and val != '2' and val != '3':
        separador(50, 1)
        val = input('Opção inválida\n1- ONG\n2- Empresa\n3- Doação\n').strip()
        separador(50, 1)
    separador(50, 1)
    return val

def cpf_or_cnpj(m, nome, email, senha, celular, proposta, cpf_cnpj):
    if m == '1':
        print(f'1- ONG: {nome}')
    elif m == '2':
        print(f'1- Nome da empresa: {nome}')
    else:
        print(f'1- Nome:{nome}')
    
    if m == '1' or m == '2':
        print(f"2- Email: {email}\n3- Senha: {senha}\n4- Celular: {celular}\n5- CNPJ: {cpf_cnpj}\n6- Proposta: {proposta}")
    else:
        print(f"2- Email: {email}\n3- Senha: {senha}\n4- Celular: {celular}\n5- CPF: {cpf_cnpj}")
    return m

def troca(m):
    mudanca = validacao_s_n(input("Deseja trocar alguma informação? [S/N]"), "Deseja trocar alguma informação? [S/N]", m).lower().strip()
    return mudanca

def validacao_escolha(m, nome, email, senha, celular, proposta, cpf_cnpj):
    cpf_or_cnpj(m, nome, email, senha, celular, proposta, cpf_cnpj)
    esc = input('Qual item a cima deseja trocar?').strip().lower()
    while esc != '1' and esc !='2' and esc != '3' and esc != '4' and esc != '5' and esc != '6':
        separador(35, 5)
        print(f'{cor["vermelho"]}Opção inválida!{cor["limpa"]}')
        cpf_or_cnpj(m, nome, email, senha, celular, proposta, cpf_cnpj)
        esc = input('Qual item a cima deseja trocar? ').strip().lower()
        separador(35, 5)
    return esc

#Programa principal
option = 1
cor = {'vermelho': '\033[31m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'azul':'\033[36m', 'roxo' : '\033[35', 'limpa' : '\033[0m'}
ong = ['FomeZero', 'Saciar Vidas', 'Prato Cheio', 'Pão e Compaixão', 'Alimentando Sonhos']
empresa = ['Innovia', 'Elixir Industries', 'Apex Innovations', 'Zephyr Enterprises', 'PulseTech']
cadastro = []

#Menu pra selecionar o tipo de cadastro desejado
ong_or_empresa = validacao_oe()

mudanca = 0

while mudanca != 'n':

    cor_separador(ong_or_empresa)

    email = input('Email: ').strip()
    senha = input('Senha: ')
    cell = input('Celular: ').strip()
    cadastro.append([email, senha, cell])

    match ong_or_empresa:
        case '1':
            nome = input('Nome da ONG: ').strip()
            cnpj_cpf = input('CNPJ: ').strip()
            proposta = input('Escreva um pouco sobre a sua proposta para seus futuros patrocinadores↓\n').strip()
            cadastro.append([nome, proposta, cnpj_cpf])
        case '2':
            nome = input('Nome da empresa: ').strip()
            cnpj_cpf = input('CNPJ: ').strip()
            proposta = input('Descreva sua empresa e seus objetivos em poucas palavras↓\n').strip()
            cadastro.append([nome, proposta, cnpj_cpf])
        case '3':
            nome = input('Nome: ').strip()
            cnpj_cpf = input('CPF: ').strip()
            proposta = ''
            cadastro.append([nome, proposta, cnpj_cpf])
        case _:
            print('Opção inválida')
    
    cor_separador(ong_or_empresa)

    mudanca = troca(ong_or_empresa)

    if mudanca == 's':
        escolha = validacao_escolha(ong_or_empresa, nome, email, senha, cell, proposta, cnpj_cpf)

    # cadastro = [['gabrielrodri333@gmail.com', 'Gabriel910', '(11)993680593'], ['FomeZero', 'aa', '6516540001-98']]
    '''1- ONG: FomeZero
        2- Email:
        3- Senha:
        4- Celular:
        5- CNPJ:
        6- Proposta:'''
    if escolha == '1':
        match ong_or_empresa:
            case '1':
                nome = input('Nome da ONG: ').strip()
                cadastro[1][0] = nome
            case '2':
                nome = input('Nome da empresa: ').strip()
                cadastro[1][0] = nome
            case '3':
                nome = input('Nome: ').strip()
                cadastro[1][0] = nome
            case _:
                print('Opção inválida!')

    elif escolha == '2':
        email = input("Email: ").strip()
        cadastro[0][0] = email

    elif escolha == '3':
        senha = input('Senha: ')
        cadastro[0][1] = senha

    elif escolha == '4':
        cell = input('Celular: ').strip()
        cadastro[0][2] = cell


    


print(cadastro)
