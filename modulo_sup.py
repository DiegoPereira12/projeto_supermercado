from os import system
from pacote.sup_alimentos import alimento01, alimento02, alimento03
from pacote.sup_bebidas import bebida01, bebida02, bebida03
from pacote.sup_acougue import carne01, carne02, carne03

# Cabeçalho

def cabecalho():

    formatCabecalho('MENU INICIAL')
    print('Escolha uma das opções abaixo:')
    print('[1] - Alimentos em geral')
    print('[2] - Açougue')
    print('[3] - Bebidas')
    print('[4] - Pagamento')
    espaco()

# Formatação cabeçalho

def formatCabecalho(msg):
    print('=' * 65)
    print(msg.center(50))
    print('=' * 65)

# Encerrar programa

def fim_programa():
    
    espaco()
    print('      Obrigado por comprar conosco!!! VOLTE SEMPRE!!!')   
    espaco()
    exit()

# Criar espaço entre as opções (=)

def espaco():
    print('=' * 65)

# Menu produtos mercado

carrinho = []

def menu_alimentos():

    while True:

        escolha = input('Qual produto você deseja comprar?\nDigite [1] Comprar arroz\nDigite [2] Comprar feijão\nDigite [3] Comprar batata\nDigite [0] Voltar ao Menu Inicial ...\n=> ')
        system('cls')

        if escolha == '0':
            system('cls') 
            break
        elif escolha == '1':    
            carrinho.append(alimento01)
        elif escolha == '2':    
            carrinho.append(alimento02)
        elif escolha == '3':    
            carrinho.append(alimento03)
        else:
            system('cls')
            espaco()
            print("\033[0;31m----------------- ERRO! DIGITE UMA OPÇÃO VÁLIDA -----------------\033[m")
            
        espaco()
        for produtos in carrinho:
            print(produtos)
        espaco()

def menu_acougue():

    while True:   

        escolha = input('Qual produto você deseja comprar?\nDigite [1] Comprar frango\nDigite [2] Comprar costela\nDigite [3] Comprar maminha\nDigite [0] Voltar ao Menu Inicial ...\n=> ')
        system('cls')

        if escolha == '0':
            system('cls') 
            break
        elif escolha == '1':    
            carrinho.append(carne01)
        elif escolha == '2':    
            carrinho.append(carne02)
        elif escolha == '3':    
            carrinho.append(carne03)
        else:
            system('cls')
            espaco()
            print("\033[0;31m----------------- ERRO! DIGITE UMA OPÇÃO VÁLIDA -----------------\033[m")

        espaco()
        for produtos in carrinho:
            print(produtos)
        espaco()

def menu_bebidas():
    
    while True:

        escolha = input('Qual produto você deseja comprar?\nDigite [1] Comprar cerveja\nDigite [2] Comprar gin\nDigite [3] Comprar vinho\nDigite [0] Voltar ao Menu Inicial ...\n=> ')
        system('cls')

        if escolha == '0':
            system('cls') 
            break
        elif escolha == '1':    
            carrinho.append(bebida01)
        elif escolha == '2':    
            carrinho.append(bebida02)
        elif escolha == '3':    
            carrinho.append(bebida03)
        else:
            system('cls')
            espaco()
            print("\033[0;31m----------------- ERRO! DIGITE UMA OPÇÃO VÁLIDA -----------------\033[m")
            
        espaco()
        for produtos in carrinho:
            print(produtos)
        espaco()