#from asyncio.windows_events import NULL
#from mailbox import NotEmptyError
#from multiprocessing.reduction import send_handle
#from operator import truediv
from os import access
from pickle import TRUE
from sre_constants import SUCCESS
from unicodedata import name
import json

class Login:
    def __init__(self):
        pass
        #self.nome = nome
        #self.senha = senha

    #função para fazer login    
    def login(self):
        self.nome = input("Digite seu nome: ")
        self.senha = input("Digite sua senha: ")

        ok = False
        file = open("DadosUsuarios.json","r")
        for i in file:

            a,b = i.split(",")
            b = b.strip()
            if(a == self.nome and b == self.senha):
                ok = True
                break
        file.close()
        return ok
         

    #função para fazer cadastro de usuário        
    def cadastro(self):
        print("Por favor, digite seu nome e senha para fazer cadastro")
        self.nome = input("Digite seu nome: ")
        self.senha = input("Digite sua senha: ")

        file = open("DadosUsuarios.json","a")
        file.write(self.nome+","+self.senha+"\n")
        file.close()
