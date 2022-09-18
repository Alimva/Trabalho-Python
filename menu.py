from sair import Sair
from compras import Compras
from devolucoes import Devolucoes



#class Menu(Sair):
def menuApp():
    count = 0
    cont = 0

    if(cont == 0):
        out = 0
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
            out = compras.compras()
            if(out == 3):
                break
        
            
        elif codigo == 2:
            devolucoes = Devolucoes()
            devolucoes.devolucoes()
        elif codigo == 3:
            break
        else:
            print('Código inválido')       