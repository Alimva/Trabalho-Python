from asyncio.proactor_events import _ProactorDuplexPipeTransport
import os
from tabnanny import check


class Carrinho:

    def __init__(self,produtos,tamanho,cor,quantidade):
        self.produtos = produtos
        self.tamanho = tamanho
        self.cor = cor
        self.quantidade = quantidade
        

    preco = {'Tênis Run Max':200,'Bota de Caminhada':350, 'Sandália Confort':250, 'Sapatilha de Escalada':500}

    def carrinho(self):
        count = 0
        while count == 0:
            
            print('\n\n')
            print('1 - Remover item do carrinho')
            print('2 - Exibir itens e o valor total a pagar')
            print('3 - Limpar carrinho')
            print('4 -Sair')
            
            check = input('Escolha uma opção: ')
            print('\n')

            if(check == '1'):
                #removendo itens do carrinho
                for i in self.produtos:
                    print("########### Produtos no carrinho: ########## \n" , self.produtos )
                    remover = input("Que item deseja remover?")

                    if remover in self.produtos:
                        self.produtos = self.produtos.remove(remover)
                        break

          

            elif(check == '2'):
                #exibir itens e mostrar o valor total a pagar
                valor = 0
                for i in range(len(self.produtos)):
                    print('Produtos no carrinho')
                    print(self.produtos[i] + self.tamanho[i] + self.cor[i]+ self.quantidade[i])

                #imprimindo o valor total    
                preco = {'Tênis Run Max': 200,'Bota de Caminhada': 350, 'Sandália Confort': 250, 'Sapatilha de Escalada': 500}
                for i in range(len(self.produtos)):
                    
                    valor += preco[self.produtos[i][0]] * self.quantidade[i][0]
                print('O valor total a ser pago será de: ',valor, "reais.")
                    
                return valor
                

                    
            elif(check == '3'):
                self.produtos = []
                self.tamanho = []
                self.cor = []
                self.quantidade = []
                print('O carrinho está limpo.')

            elif(check == '4'):
                return

            else:
                print('Intente novamente. Digite uma opção válida.')    