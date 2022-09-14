import os

produtos = (
    {'id': 1, 'nome': 'produto1', 'preço': 100 },
    {'id': 2, 'nome': 'produto2', 'preço': 200 },
    {'id': 3, 'nome': 'produto3', 'preço': 50 },
    {'id': 4, 'nome': 'produto4', 'preço': 150 }
)

carrinho = []

def exibir_opcoes():
    print('\n\n')
    
    print('1 - Adicionar item ao carrinho')
    print('2 - Remover item do carrinho')
    print('3 - Exibir itens e o valor total a pagar')
    print('4 - Limpar carrinho')
    print('5 -Sair')

def exibir_produtos():
    for p in produtos:
        print('Id: {0} - Nome: {1} - Preço: {2}\n'.format(p['id'],p['nome'], p['preço']))

opcao = '1'

os.system('clear')
print('Carrinho de compras \n')

def obter_nome_produto(id):
    for p in produtos:
        if p['id'] == id:
            return p['nome']

while opcao != "5":
    exibir_opcoes()
    opcao = input('Digite uma opção: ')     

    if opcao == '1':
        exibir_produtos()
        
        id = int(input('Digite o número do produto:'))
        quantidade = int(input('Digite a quantidade desejada do produto: '))
        carrinho.append({'id': id, 'quantidade': quantidade})

    if opcao == '2':
        id = int(input('digite o número do produto:'))
        temp = []
        for item in carrinho:
            if item['id'] != id:
                temp.append(item)
    
    if opcao == '3':
        print('\n\n')
        somatorio = 0 
        for item in carrinho:
            for produto in produtos:
                if produto['id'] == item['id']:
                    somatorio = somatorio + \
                        (produto['preço'] * item['quantidade'])
                    break
            
            print(
                'Nome: {0} - Quantidade: {1}'.format(obter_nome_produto(item['id']), item['quantidade']))
        print('Preço total: {0}'.format(somatorio))
    
    if opcao == '4':
        carrinho = []                