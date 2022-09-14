

class Devolucoes():
    @staticmethod
    def devolucoes(self):
        self.produtos= ("Tênis Run Max","tênis run max","Bota de Caminhada", "bota de caminhada","Sandália Confort","sandália confort","Sapatilha de Escalada","sapatilha de escalada")
        print("Olá!")
        self.aux = input("O que você deseja devolver? ")

        if(self.aux in self.produtos):
            

