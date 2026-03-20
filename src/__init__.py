org = {}
contador = 0
def sag():
    print('Bem vindo a área de Atendimento Geral!')
    nome = input('Para continuarmos, digite seu nome: ')
    if nome in org:
        print('Sua senha já foi retirada!')
    else:
        tipo = input('Sua senha é do tipo P - Prioritária ou N - Normal? ')
        if tipo == "P":
            sen = f"{tipo}{contador + 1}"
            org[nome] = sen
            print(org[nome])
            contap = contador + 1
        elif tipo == "N":
            sen = f"{tipo}{contador + 1}"
            org[nome] = sen
            print(org[nome])
            contan = contador + 1
        else:
            print('Resposta inválida, tente novamente!')


def sc():
    print('Bem vindo a área de Caixa!')
    nome = input('Para continuarmos, digite seu nome:')
    if nome in org:
        print('Sua senha já foi retirada!')
    else:
        tipo = input('Sua senha é do tipo P - Prioritária ou N - Normal? ')
        if tipo == "P":
            sen = f"{tipo}{contador + 1}"
            org[nome] = sen
            print(org[nome])
            contcp = contador + 1
        elif tipo == "N":
            sen = f"{tipo}{contador + 1}"
            org[nome] = sen
            print(org[nome])
            contcn = contador + 1
        else:
            print('Resposta inválida, tente novamente!')

def tsen():
    print(len(f"Existem {(org)} senhas registradas no total"))

def menu():
    while True:
        print("Seja bem vindo ao menu de atendimento bancário!")
        print("1.Gerar nova senha")
        print("2.Ver estatisticas")
        print("3.Sair")
        r = input('Digite o numero do serviço que voce deseja escoher: ')
        if r == "1":
            print('1. Acesso a área de Atendimento Geral')
            print('2. Acesso a área de Caixa')
            t = input('Digite o número da área em que deseja utilizar o serviço: ')
            if t == '1':
                sag()
            elif t == '2':
                sc()
            else:
                print('Resposta inválida tente novamente!')
        if r == "2":
            print('1. Visualizar a quantidade total de senhas')
            print('2. Visualizar o total por tipo de atendimento')
            print('3. Visualizar o total por tipo de senha')
            y = input('Digite o número da área em que deseja utilizar o serviço: ')
            if y == '1':
                tsen()
            else:
                print('Resposta inválida, tente novamente!')
        if r == "3":
            print("Saindo...")
            break


