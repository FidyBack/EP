"""
Created on Mon Apr 23 18:44:09 2018

@author: Rodrigo e Abel zicas da balada

PAGUEM-NOS
"""

#Firebase
from firebase import firebase
fb = firebase.FirebaseApplication("https://nuvem-ep.firebaseio.com/", None)
estoque = fb.get("/estoque/lojas", None)

#Criando o estoque caso não haja nada no código
if estoque == None:
	estoque = {}

#Escolhendo adicionar a Loja
loja = "-1"
while loja not in estoque:
	loja = input("\nDigite o nome da loja: ")
	if loja not in estoque:
		ask = input("\nLoja não encontrada, deseja adiciona-la?\n1 - Sim\n2 - Não\n")
		if ask == "1":
			estoque[loja] = {}
			print("\nLoja adicionada, entrando no estoque")
		else:
			print("\nvoltando para a escolha da loja")

#Repetição
iniciar = "-1"
while iniciar != "0":

# Menu Inicial
	iniciar = input("\nControle de estoque\n\
0 - Sair \n\
1 - Adicionar item \n\
2 - Remover item \n\
3 - Alterar quantidade do item \n\
4 - Imprimir estoque \n\
5 - Alterar preço unitário\n\
6 - Imprimir produtos com quantidades negativas\n\
7 - Imprimir valor total do estoque\n\
8 - Apagar estoque\n\
Faça sua escolha: ")

# Se o número 0 for selecionado
	if iniciar == "0":
		break

# Se o número 1 for selecionado
	if iniciar == "1":
		produto_ad = input("\nNome do produto: ")
		if produto_ad in estoque[loja] and estoque[loja][produto_ad] != None:
			print("\nProduto já está no estoque")	
		else:
			quantia_ad = (input("Quantidade inicial: "))
			while quantia_ad.isnumeric() == False:
				print('ERRO')
				quantia_ad = (input("Quantidade inicial: "))
			preco_ad = float(input("Preço Unitário: "))
			estoque[loja][produto_ad] = {"quantidade":int(quantia_ad), "preco":preco_ad}
			print("\nProduto Adicionado!!!")

# Se o número 2 for selecionado
	elif iniciar == "2":
		produto_rm =(input("\nProduto que quer remover: "))
		if produto_rm in estoque[loja]:
			del estoque[loja][produto_rm]
			print("\nProduto removido com sucesso!!!")
		else:
			print("\nEsse produto não se encontra em estoque")

# Se o número 3 for selecionado
	elif iniciar == "3":
		produto_al = (input("\nProduto que quer alterar: "))
		if produto_al in estoque[loja]:
				quantia_al = int(input("Quantia para alteração: "))
				valor_atual = estoque[loja][produto_al]["quantidade"]
				estoque[loja][produto_al]["quantidade"] = valor_atual + quantia_al
				print("\nAlteração feita com sucesso!!!")
		else:
			print("\nProduto não encontrado")

# Se o número 4 for selecionado
	elif iniciar == "4":
		print("\nEstoque: ",estoque[loja])

#Se o número 5 for selecionado
	elif iniciar == "5":
		produto_df = input("\nNome do produto: ")
		if produto_df in estoque[loja]:
			preco_df = float(input("Novo preço do produto: "))
			if preco_df > 0:
				estoque[loja][produto_df]["preco"] = preco_df
				print("\nPerço alterado com sucesso!!")
			elif preco_df == 0:
				print("\nPreco não pode ser zero")
			else:
				print("\nPreco não pode ser negativo")
		else:
			print("\nProduto não está em estoque")

#Se o número 6 for selecionado
	elif iniciar == "6":
		negativos = []
		for e in estoque[loja]:
			if estoque[loja][e]["quantidade"] < 0:
				negativos.append(e)
		print("\nProdutos em falta: ",negativos)

#Se o número 7 for selecionado
	elif iniciar == "7":
		soma = 0
		for e in estoque[loja]:
			soma += (estoque[loja][e]["quantidade"]*estoque[loja][e]["preco"])
		print("\nValor total em estoque: {0} R$".format(soma))

#Se o número 8 for selecionado
	elif iniciar == "8":
		resp = input("\nTem certeza que deseja apagar?\n1-Sim\n2-Não\n")
		if resp == "1":
			estoque = {}
			print("\nEstoque apagado com sucesso!!!")
		elif resp != "2":
			print("\nOpção inválida")
#Erro
	else:
		print("\nOpção Inválida")

#Transformando em json
	loja_fb = fb.patch("/estoque/lojas", estoque)

#Selecionando 0
print("\nVolte Sempre!!!")
