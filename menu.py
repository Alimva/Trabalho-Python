from sair import Sair
from compras import Compras

count = 0
cont = 0


class Menu(Sair):
    if(cont == 0):
        produtos = []
        tamanho = []
        cor = []
        quantidade = []
    while count == 0:
        
        print('=== Menu ===')           
        print('1 - Compras')
        print('2 - Devoluções')
        print('3 - Sair do site')
        codigo = int(input('Informe a opção desejada: '))

        if codigo == 1:
            cont = 1
            compras = Compras(produtos,tamanho,cor,quantidade)
            compras.compras()
            
        elif codigo == 2:
            devolucoes = Devolucoes()
            devolucoes.devolucoes()
        elif codigo == 3:
            break
        else:
            print('Código inválido')       