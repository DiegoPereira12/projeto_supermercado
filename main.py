from os import system
import modulo_sup
from pacote.sup_alimentos import lista_alimentos
from pacote.sup_bebidas import lista_bebidas
from pacote.sup_acougue import lista_carnes

# Menu principal 

while True:

    modulo_sup.cabecalho('MENU INICIAL')
    print('Escolha uma das opções abaixo:')
    print('[1] - Alimentos em geral')
    print('[2] - Açougue')
    print('[3] - Bebidas')
    modulo_sup.espaco()

    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        system('cls')
        modulo_sup.cabecalho('MENU ALIMENTOS')
        print(lista_alimentos)
        modulo_sup.espaco()
        modulo_sup.menu_alimentos()

    elif opcao == 2:
        system('cls')
        modulo_sup.cabecalho('MENU AÇOUGUE')
        print(lista_carnes)
        modulo_sup.espaco()
        modulo_sup.menu_acougue()

    elif opcao == 3:
        system('cls')
        modulo_sup.cabecalho('MENU BEBIDAS')
        print(lista_bebidas)
        modulo_sup.espaco()
        modulo_sup.menu_bebidas()
        



    
    
    
        
        

        
        
        









    