from sair import Sair

count = 0


class Menu:
    while count == 0:
        print('=== Menu ===')
        print('1 - Compras')
        print('2 - Devoluções')
        print('3 - Sair do site')
        codigo = int(input('Informe a opção desejada: '))

        if codigo == 1:
            compras = Compras()
            compras.compras()
        elif codigo == 2:
            devolucoes = Devolucoes()
            devolucoes.devolucoes()
        elif codigo == 3:
            sair = Sair()
            sair.sair()
            break
        else:
            print('Código inválido')