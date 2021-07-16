from os import system
from modulo_sup import cabecalho, menu_alimentos, menu_acougue, menu_bebidas
from pacote.sup_alimentos import lista_alimentos
from pacote.sup_bebidas import lista_bebidas
from pacote.sup_acougue import lista_carnes

# Criar espaço entre as opções (=)

def espaco():
    print('=' * 65)

# Menu principal 

while True:

    cabecalho('MENU INICIAL')
    print('Escolha uma das opções abaixo:')
    print('[1] - Alimentos em geral')
    print('[2] - Açougue')
    print('[3] - Bebidas')
    espaco()

    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        system('cls')
        cabecalho('MENU ALIMENTOS')
        print(lista_alimentos)
        espaco()
        menu_alimentos()

    elif opcao == 2:
        system('cls')
        cabecalho('MENU AÇOUGUE')
        print(lista_carnes)
        espaco()
        menu_acougue()

    elif opcao == 3:
        system('cls')
        cabecalho('MENU BEBIDAS')
        print(lista_bebidas)
        espaco()
        menu_bebidas()
        



    
    
    
        
        

        
        
        









    