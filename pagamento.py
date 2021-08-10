from os import system
import modulo_sup

def formas_pagamentos():
    
    while True:

        total = 0
        for item in modulo_sup.carrinho:
            for nome, valor in item.items():
                total += valor
            
        modulo_sup.espaco()        
        print('            O valor total de suas compras é {:.2f}'.format (total))
        modulo_sup.espaco()

        print('!!! Desconto de 5% para pagamentos em Dinheiro ou no Débito !!!')
        modulo_sup.espaco()

        pagamento = input('Qual a forma de pagamento?\nDigite [1] Dinheiro\nDigite [2] Débito\nDigite [3] Crédito\n=> ')

        if pagamento == '1':
            total_dinheiro = 0
            total_dinheiro = total - (total * 5 / 100)
            system('cls')
            modulo_sup.espaco()
            print('            O valor a ser pago é de R$ {:.2f}'. format(total_dinheiro))
            break

        elif pagamento == '2':
            total_débito = 0
            total_débito = total - (total * 5 / 100)
            system('cls')
            modulo_sup.espaco()
            print('            O valor a ser pago é de R$ {:.2f}'.format(total_débito))
            break

        elif pagamento == '3':
            system('cls')
            modulo_sup.espaco()
            print('            O valor total a ser pago é de R$ {:.2f}'.format(total))
            break
        
        else:
            system('cls')
            modulo_sup.espaco()
            print("\033[0;31m----------------- ERRO! DIGITE UMA OPÇÃO VÁLIDA -----------------\033[m")
            modulo_sup.espaco()      