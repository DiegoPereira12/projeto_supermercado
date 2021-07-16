import csv
from modulo_sup import carrinho

def gerarCsv():
    
    with open('produtos.csv', 'w') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["Produto;"+"Valor"])
        for produto,valor in carrinho.items():
            writer.writerow([produto, valor])