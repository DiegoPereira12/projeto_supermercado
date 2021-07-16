from os import system
from pacote.sup_alimentos import alimento01, alimento02, alimento03
from pacote.sup_bebidas import bebida01, bebida02, bebida03
from pacote.sup_acougue import carne01, carne02, carne03
import pagamento

# Cabeçalho Menus

def cabecalho(msg):
    print('=' * 65)
    print(msg.center(50))
    print('=' * 65)

# Menu dos alimentos do Mercado

carrinho = []

def menu_alimentos():
    
    while True:
        escolha = int(input('Qual produto você deseja comprar?\nDigite [1] Comprar arroz\nDigite [2] Comprar feijão\nDigite [3] Comprar batata\nDigite [4] Realizar pagamento\nDigite [0] Continue comprando...\n=> '))

        if escolha == 0:
            system('cls') 
            break
        elif escolha == 1:    
            carrinho.append(alimento01)
        elif escolha == 2:    
            carrinho.append(alimento02)
        elif escolha == 3:    
            carrinho.append(alimento03)
        elif escolha == 4:
            system('cls')
            pagamento.formas_pagamentos()
            fim_programa()
            
        espaco()
        for produtos in carrinho:
            print(produtos)
        espaco()

def menu_acougue():

    while True:
        
        escolha = int(input('Qual produto você deseja comprar?\nDigite [1] Comprar frango\nDigite [2] Comprar costela\nDigite [3] Comprar maminha\nDigite [4] Realizar pagamento\nDigite [0] Continue comprando...\n=> '))
        
        if escolha == 0:
            system('cls') 
            break
        elif escolha == 1:    
            carrinho.append(carne01)
        elif escolha == 2:    
            carrinho.append(carne02)
        elif escolha == 3:    
            carrinho.append(carne03)
        elif escolha == 4:
            system('cls')
            pagamento.formas_pagamentos()
            fim_programa()
            
        espaco()
        for produtos in carrinho:
            print(produtos)
        espaco()

def menu_bebidas():
    
    while True:
        
        escolha = int(input('Qual produto você deseja comprar?\nDigite [1] Comprar cerveja\nDigite [2] Comprar gin\nDigite [3] Comprar vinho\nDigite [4] Realizar pagamento\nDigite [0] Continue comprando...\n=> '))

        if escolha == 0:
            system('cls') 
            break
        elif escolha == 1:    
            carrinho.append(bebida01)
        elif escolha == 2:    
            carrinho.append(bebida02)
        elif escolha == 3:    
            carrinho.append(bebida03)
        elif escolha == 4:
            system('cls')
            pagamento.formas_pagamentos()
            fim_programa()
    
        espaco()
        for produtos in carrinho:
            print(produtos)
        espaco()

# Encerrar programa

def fim_programa():
    
    espaco()
    print('      Obrigado por comprar conosco!!! VOLTE SEMPRE!!!')   
    espaco()
    exit()

# Criar espaço entre as opções (=)

def espaco():
    print('=' * 65)








    




   

    

    


        



        

        


