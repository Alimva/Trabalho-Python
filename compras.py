
from sair import Sair

class Compras:
    def __init__(self,produtos,tamanho,cor,quantidade):
        self.produtos = produtos
        self.tamanho = tamanho
        self.cor = cor
        self.quantidade = quantidade


    def compras(self):
        
        count = 0
        cores = ['preto','branco','azul','amarelo','vermelho','roxo','lilas','verde','laranja','rosa','cinza']

        while count == 0:
            print("\n")
            print("1 - Menu")
            print("2 - Carrinho")
            print("3 - Sair do site")
            print("\n")
            
            
            print(" Tênis Run Max            Bota de Caminhada          Sandália Confort           Sapatilha de Escalada\n")
            print("    R$200,00                 R$350,00                   R$250,00                       R$500,00")
            print("O tênis ideal pa-        O companheiro perfei-      Elegante e estilosa,    A melhor amiga dos amantes")
            print("ra quem gosta de        to para suas aventuras.    esse design clássico é            de escalada.")
            print("de correr. Com um       Oferecendo o suporte e     o que você precisa para     Seja em uma academia de ")
            print("interior macio fei-     a estabilidade que você       o seu dia-a-dia.          escalada indoor ou no")
            print("to com nossa tecno-    precisa nas suas trilhas.   As faixas delicadas são     meio da natureza, essa ")
            print("logia ultra-confort    Todas as nossas botas     feitas de algodão orgânico sapatilha tem tudo o que você")
            print("para melhorar a sua     são feitas com impacto     oferecendo suporte firme   precisa,com o seu solado ")
            print("performance sem sa-    ambiental completamente     sem correr o risco de     anti-derrapamente de alta")
            print("crificar seu conforto.          zerado.             machucar os seus pés     qualidade o céu é o limite.\n")

            check = input("O que você quer comprar? ")
            print("\n")

            if(check == "1"):
                break
            elif(check == "2"):
                carrinho = Carrinho()
                carrinho.Carrinho()
            elif(check == '3'):
                return 3
            elif(check == "Tênis Run Max" or check == "tênis run max"):
                self.produtos.append('Tênis Run Max')
                aux = int(input('Tamanho (temos tamanhos 35 a 47): '))
                
                while(not 35 <= aux <= 47):
                    print('Ops! Não temos esse tamanho!')
                    aux = int(input('Tamanho: '))
                
                self.tamanho.append(aux)
                aux = input('Cor (temos preto,branco,azul,vermelho,amarelo,roxo,verde,laranja,rosa,lilas e cinza): ')

                while(aux not in cores):
                    print("Ops! Não temos essa cor")
                    aux = input('Cor (temos preto,branco,azul,vermelho,amarelo,roxo,verde,laranja,rosa,lilas e cinza): ')
                
                self.cor.append(aux)
                aux = int(input('Quantidade: '))
                self.quantidade.append(aux)
            elif(check == "Bota de Caminhada" or check == "bota de caminhada"):
                self.produtos.append('Bota de Caminhada')
                aux = int(input('Tamanho (temos tamanhos 35 a 47): '))
                
                while(not 35 <= aux <= 47):
                    print('Ops! Não temos esse tamanho!')
                    aux = int(input('Tamanho: '))
                
                self.tamanho.append(aux)
                aux = input('Cor (temos preto,branco,azul,vermelho,amarelo,roxo,verde,laranja,rosa,lilas e cinza): ')

                while(aux not in cores):
                    print("Ops! Não temos essa cor")
                    aux = input('Cor (temos preto,branco,azul,vermelho,amarelo,roxo,verde,laranja,rosa,lilas e cinza): ')
                
                self.cor.append(aux)
                aux = int(input('Quantidade: '))
                self.quantidade.append(aux)
            elif(check == "Sandália Confort" or check == "sandália confort"):
                self.produtos.append('Sandália Confort')
                aux = int(input('Tamanho (temos tamanhos 35 a 47): '))
                
                while(not 35 <= aux <= 47):
                    print('Ops! Não temos esse tamanho!')
                    aux = int(input('Tamanho: '))
                
                self.tamanho.append(aux)
                aux = input('Cor (temos preto,branco,azul,vermelho,amarelo,roxo,verde,laranja,rosa,lilas e cinza): ')

                while(aux not in cores):
                    print("Ops! Não temos essa cor")
                    aux = input('Cor (temos preto,branco,azul,vermelho,amarelo,roxo,verde,laranja,rosa,lilas e cinza): ')
                
                self.cor.append(aux)
                aux = int(input('Quantidade: '))
                self.quantidade.append(aux)
            elif(check == "Sapatilha de Escalada" or check == "sapatilha de escalada"):
                self.produtos.append('Sapatilha de Escalada')
                aux = int(input('Tamanho (temos tamanhos 35 a 47): '))
                
                while(not 35 <= aux <= 47):
                    print('Ops! Não temos esse tamanho!')
                    aux = int(input('Tamanho: '))
                
                self.tamanho.append(aux)
                aux = input('Cor (temos preto,branco,azul,vermelho,amarelo,roxo,verde,laranja,rosa,lilas e cinza): ')

                while(aux not in cores):
                    print("Ops! Não temos essa cor")
                    aux = input('Cor (temos preto,branco,azul,vermelho,amarelo,roxo,verde,laranja,rosa,lilas e cinza): ')
                
                self.cor.append(aux)
                aux = int(input('Quantidade: '))
                self.quantidade.append(aux)
            else:
                print('Ops! Essa não é uma resposta válida')
            

            






    
    
