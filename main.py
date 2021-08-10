from os import system
import pagamento
import modulo_sup
import gera_csv
from pacote.sup_alimentos import lista_alimentos
from pacote.sup_bebidas import lista_bebidas
from pacote.sup_acougue import lista_carnes

while True:
    
    modulo_sup.cabecalho()
    
    opcao = input('Digite sua opção: ')
    system('cls')

    if opcao == '1':
        system('cls')
        modulo_sup.espaco()
        print(lista_alimentos)
        modulo_sup.espaco()
        modulo_sup.menu_alimentos()
 
    elif opcao == '2':
        system('cls')
        modulo_sup.espaco()
        print(lista_carnes)
        modulo_sup.espaco()
        modulo_sup.menu_acougue()
 
    elif opcao == '3':
        system('cls')
        modulo_sup.espaco()
        print(lista_bebidas)
        modulo_sup.espaco()
        modulo_sup.menu_bebidas()
    
    elif opcao == '4':
        pagamento.formas_pagamentos()
        gera_csv.gerarCsv()
        modulo_sup.fim_programa()
        
    else:
        system('cls')
        modulo_sup.espaco()
        print("\033[0;31m----------------- ERRO! DIGITE UMA OPÇÃO VÁLIDA -----------------\033[m")
    