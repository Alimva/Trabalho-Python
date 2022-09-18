from menu import menuApp
from login import Login
#from sair import Sair

def menuLogin():
    print('##########  Login  ##########')
    login = Login()
    op = 0
    while(op!=3):
        op = input("Deseja fazer Login ou Cadastro? \n Por favor, digite uma opção ((1)-login , (2)-cadastro : ")
        if(op == "1"):
            ok = login.login()
            if(ok == True):
                print('Login realizado com sucesso!!!')
                menuApp()
            else:
                print("Nome de usuário ou senha estão errados! Tente novamente.")

        if(op == "2"):
            ok = login.cadastro()
            print("Cadastro realizado com sucesso!")
                        




    

 
1
if __name__ == '__main__':
    menuLogin()
    