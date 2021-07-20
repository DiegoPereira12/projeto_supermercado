import csv
import modulo_sup

def gerarCsv():
    
    with open('produtos4.csv', 'w') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["Produtos","Valor"])
        for item in modulo_sup.carrinho:
            for key, value in item.items():
                writer.writerow([key, value])