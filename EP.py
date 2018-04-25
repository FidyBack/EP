"""
Created on Mon Apr 23 18:44:09 2018

@author: Rodrigo e Abel zicas da balada

PAGUEM-NOS
"""
# Arquivos
import json as js 
with open('loja.txt','r') as arquivo:
	conteudo = arquivo.read()
	lojas = js.loads(conteudo)

loja=0
while loja not in lojas:
	loja=input('Qual o nome da loja?')
estoque=lojas[loja]
#Repetição
iniciar = '-1'
while iniciar != '0':

# Menu Inicial
	iniciar = input('Controle de estoque\n\
0 - Sair \n\
1 - Adicionar item \n\
2 - Remover item \n\
3 - Alterar quantidade do item \n\
4 - Imprimir estoque \n\
5 - Alterar preço unitário\n\
6 - Imprimir produtos com quantidades negativas\n\
7 - Imprimir valor total do estoque\n\
8 - Apagar estoque\n\
Faça sua escolha: ')
# Se o número 0 for selecionado
	if iniciar == '0':
		break

# Se o número 1 for selecionado
	if iniciar == '1':
		produto_ad = input('Nome do produto: ')
		if produto_ad in estoque and estoque[produto_ad] != None:
			print('Produto já está no estoque')	
		else:
			quantia_ad = int(input('Quantidade inicial: '))
			preco_ad = float(input('Preço Unitário: '))
			estoque[produto_ad] = {'quantidade':quantia_ad, 'preco':preco_ad}
			print('Produto Adicionado!!!')

# Se o número 2 for selecionado
	elif iniciar == '2':
		produto_rm =(input('Produto que quer remover: '))
		if produto_rm in estoque:
			del estoque[produto_rm]
		else:
			print('Esse produto não se encontra em estoque')

# Se o número 3 for selecionado
	elif iniciar == '3':
		produto_al = (input('Produto que quer alterar: '))
		if produto_al in estoque:
				quantia_al = int(input('Quantia para alteração:'))
				valor_atual = estoque[produto_al]['quantidade']
				estoque[produto_al]['quantidade'] = valor_atual + quantia_al
		else:
			print('Produto não encontrado')

# Se o número 4 for selecionado
	elif iniciar == '4':
		print(estoque)

#Se o número 5 for selecionado
	elif iniciar == '5':
		produto_df = input('Nome do produto: ')
		if produto_df in estoque:
			preco_df = float(input('Qual o novo preço unitário do produto? '))
			if preco_df >= 0:
				estoque[produto_df]['preco'] = preco_df
			else:
				print('Preco não pode ser negativo e nem zero')
		else:
			print('Produto não está em estoque')

#Se o número 6 for selecionado
	elif iniciar == '6':
		negativos = []
		for e in estoque:
			if estoque[e]['quantidade'] < 0:
				negativos.append(e)
		print(negativos)

#Se o número 7 for selecionado
	elif iniciar == '7':
		soma = 0
		for e in estoque:
			soma += (estoque[e]['quantidade']*estoque[e]['preco'])
		print(soma)

#Se o número 8 for selecionado
	elif iniciar == '8':
		resp = input('Tem certeza que deseja apagar?\n1-Sim\n2-Não\n')
		if resp == '1':
			estoque = {}
		elif resp != '2':
			print('Opção inválida')
#Erro
	else:
		print('ERRO')

#Transformando em json
	lojas[loja]=estoque
	with open('loja.txt','w') as arquivo:
		loja_js = js.dumps(lojas, sort_keys = True, indent = 4)
		conteudo = arquivo.write(loja_js)

#Selecionando 0
print('Volte Sempre!!!')
