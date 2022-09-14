from mailbox import NotEmptyError
from operator import truediv
from os import access
from pickle import TRUE
from sre_constants import SUCCESS
from unicodedata import name
import json

granted = False
def grant():
    global granted
    granted = True

#Fazendo login
def login(nome,senha):
    SUCCESS = False
    file = open("DadosUsuarios.json","r")
    for i in file:
        
        a,b = i.split(",")
        b = b.strip()
        if(a == nome and b == senha):
            SUCCESS = True
            break
    file.close()
    
    if(SUCCESS):
        print("Login realizado com sucesso!!!")
        grant()
    else:
        print("Nome de usuário ou senha são incorretos! Tenta novamente.")    

#Função para realizar cadastro
def cadastro(nome,senha):
    file = open("DadosUsuarios.json","a")
    file.write(nome + "," + senha + "\n")
    file.close()
    grant()


def access(opcion):
    global nome
    if(option == "login"):
        nome = input("Digite seu nome: ")
        senha = input("Digite sua senha: ")
        login(nome,senha)
    else:
        print("Por favor, digite seu nome e senha para fazer cadastro")
        nome = input("Digite seu nome: ")
        senha = input("Digite sua senha: ")
        cadastro(nome,senha)

def begin():
    global option
    print('##########  Login  ##########')
    option = input('Deseja fazer Login ou Cadastro? \n Por favor, digite uma opção (login, cadastro) :')
    if (option != "login" and option != "cadastro"):
        begin()
begin()        
access(option)
if(granted):
    print("Seja Bem-Vindo!")
    print("### Detalhes de Usuário ###")
    print("Nome de usuário: ",nome)
