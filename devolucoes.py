

class Devolucoes():
    @staticmethod
    def devolucoes():
        produtos= ("Tenis Run Max","tenis run max","Bota de Caminhada", "bota de caminhada","Sandalia Confort","sandalia confort","Sapatilha de Escalada","sapatilha de escalada")
        print("Olá!")
        aux = input("O que você deseja devolver? ")

        while(aux not in produtos):
            print("Ops! Esse produto não existe! Deseja tentar novamente?")
            ans = input("Y/n")
            if(ans == 'n'):
                break
        
        while(aux in produtos):
            review = input("Qual foi o problema que você teve com o produto? ")
            print("Seu dinheiro será devolvido.\nPor favor, realize o envio do produto em até duas semanas.")

