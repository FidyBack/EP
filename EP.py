'''
Made by: Abel Cavalcante de Andrade
Some sources: https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter/7557028#7557028
'''

from firebase import firebase
import tkinter as tk
from tkinter import ttk


# Firebase initialization
fb = firebase.FirebaseApplication("https://nuvem-ep.firebaseio.com/", None)
stores = fb.get("/stores", None)


# Main class
class MainApp(tk.Tk):
	def __init__(self):
		super().__init__()

		self.geometry("800x600")
		self.shared_data = {
			"store_name": tk.StringVar()
		}

		# Initialize a model the with be used by the frames
		model = tk.Frame(self)
		model.pack(fill=tk.BOTH, expand=True)
		model.rowconfigure(0, weight=1)
		model.columnconfigure(0, weight=1)

		# Put the frames in a dictionary
		self.frames = {}
		for F in (InitialWindow, ConfirmationWindow, MenuWindow):
			frame = F(model, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")
			frame.rowconfigure(0, weight=1)
			frame.columnconfigure(0, weight=1)

		self.show_frame(InitialWindow)

	# Function to change Frame
	def show_frame(self, class_name):
		frame = self.frames[class_name]
		frame.tkraise()

	# Change frame and set the name of the store in the variable
	def store_consult(self, store_name):
		self.shared_data["store_name"].set(store_name)
		
		if store_name not in stores:
			self.show_frame(ConfirmationWindow)
		else:
			self.show_frame(MenuWindow)

	# Change frame and add store to firebase
	def add_store(self, store_name):
		stores[store_name] = 00
		fb.patch("/stores", stores)
		self.show_frame(MenuWindow)


# First window class
class InitialWindow(tk.Frame):
	def __init__(self, master, controller):
		tk.Frame.__init__(self, master)
		frm_store = tk.Frame(self)
		frm_store.grid(row=0, column=0)

		lbl_store = tk.Label(frm_store, text="Digite o nome da Loja")
		ent_store = tk.Entry(frm_store, width=30)
		btn_store = tk.Button(frm_store, text="Acessar Loja", command=lambda: controller.store_consult(ent_store.get()))

		lbl_store.pack(pady=(0,10))
		ent_store.pack()
		btn_store.pack(pady=(10,0))


# New time store window class
class ConfirmationWindow(tk.Frame):
	def __init__(self, master, controller):
		tk.Frame.__init__(self, master)
		frm_conf = tk.Frame(self)
		frm_conf.grid(row=0, column=0)
		
		lbl_conf = tk.Label(frm_conf, text="Essa loja não está registada, deseja adicioná-la?")
		lbl_conf.pack()
		
		frm_buttons = tk.Frame(frm_conf)
		btn_foward = tk.Button(frm_buttons, text="Sim", width=10, command=lambda: controller.add_store(controller.shared_data["store_name"].get()))
		btn_back = tk.Button(frm_buttons, text="Não", width=10, command=lambda: controller.show_frame(InitialWindow))

		frm_buttons.pack()
		btn_foward.grid(row=0, column=0, sticky="e")
		btn_back.grid(row=0, column=1, sticky="w")


# Menu window class
class MenuWindow(tk.Frame):
	def __init__(self, master, controller):
		tk.Frame.__init__(self, master)
		
		lbl_menu = tk.Label(self, textvariable=controller.shared_data["store_name"])
		lbl_menu.grid(sticky="n")

		frm_menu = tk.Frame(self)
		frm_menu.grid(row=0, column=0)

		lbl_estoque = tk.Label(frm_menu, text="Controle de Estoque")
		lbl_estoque.pack()

		frm_buttons = tk.Frame(frm_menu)

		btn_add = tk.Button(frm_buttons, text="Adicionar item", width=25, height=2 )
		btn_remove = tk.Button(frm_buttons, text="Remover item", width=25, height=2 )
		btn_change_quant = tk.Button(frm_buttons, text="Alterar quantidade do item", width=25, height=2 )
		btn_print_all = tk.Button(frm_buttons, text="Imprimir estoque", width=25, height=2 )
		btn_change_price = tk.Button(frm_buttons, text="Alterar preço unitário", width=25, height=2 )
		btn_print_negative = tk.Button(frm_buttons, text="Imprimir produtos com \nquantidades negativas", width=25, height=2 )
		btn_print_value = tk.Button(frm_buttons, text="Imprimir valor total do estoque", width=25, height=2 )
		btn_del = tk.Button(frm_buttons, text="Apagar estoque", width=25, height=2 )
		btn_back = tk.Button(frm_buttons, text="Voltar", width=25, height=2, command=lambda: controller.show_frame(InitialWindow) )
		
		
		frm_buttons.pack()
		btn_add.grid(row=0, column=0)
		btn_remove.grid(row=0, column=1)
		btn_change_quant.grid(row=1, column=0)
		btn_print_all.grid(row=1, column=1)
		btn_change_price.grid(row=2, column=0)
		btn_print_negative.grid(row=2, column=1)
		btn_print_value.grid(row=3, column=0)
		btn_del.grid(row=3, column=1)
		btn_back.grid(row=4, columnspan=2)


if __name__ == "__main__":
	# Create if dosen't exist
	if not stores:
		stores = {}
	
	app = MainApp()
	app.mainloop()



# # Menu Inicial
# 	iniciar = input("\nControle de estoque\n\
# 0 - Sair \n\
# 1 - Adicionar item \n\
# 2 - Remover item \n\
# 3 - Alterar quantidade do item \n\
# 4 - Imprimir estoque \n\
# 5 - Alterar preço unitário\n\
# 6 - Imprimir produtos com quantidades negativas\n\
# 7 - Imprimir valor total do estoque\n\
# 8 - Apagar estoque\n\
# Faça sua escolha: ")

# # Se o número 0 for selecionado
# 	if iniciar == "0":
# 		break

# # Se o número 1 for selecionado
# 	if iniciar == "1":
# 		produto_ad = input("\nNome do produto: ")
# 		if produto_ad in estoque[loja] and estoque[loja][produto_ad] != None:
# 			print("\nProduto já está no estoque")	
# 		else:
# 			quantia_ad = (input("Quantidade inicial: "))
# 			while quantia_ad.isnumeric() == False:
# 				print('ERRO')
# 				quantia_ad = (input("Quantidade inicial: "))
# 			preco_ad = float(input("Preço Unitário: "))
# 			estoque[loja][produto_ad] = {"quantidade":int(quantia_ad), "preco":preco_ad}
# 			print("\nProduto Adicionado!!!")

# # Se o número 2 for selecionado
# 	elif iniciar == "2":
# 		produto_rm =(input("\nProduto que quer remover: "))
# 		if produto_rm in estoque[loja]:
# 			del estoque[loja][produto_rm]
# 			print("\nProduto removido com sucesso!!!")
# 		else:
# 			print("\nEsse produto não se encontra em estoque")

# # Se o número 3 for selecionado
# 	elif iniciar == "3":
# 		produto_al = (input("\nProduto que quer alterar: "))
# 		if produto_al in estoque[loja]:
# 				quantia_al = int(input("Quantia para alteração: "))
# 				valor_atual = estoque[loja][produto_al]["quantidade"]
# 				estoque[loja][produto_al]["quantidade"] = valor_atual + quantia_al
# 				print("\nAlteração feita com sucesso!!!")
# 		else:
# 			print("\nProduto não encontrado")

# # Se o número 4 for selecionado
# 	elif iniciar == "4":
# 		print("\nEstoque: ",estoque[loja])

# #Se o número 5 for selecionado
# 	elif iniciar == "5":
# 		produto_df = input("\nNome do produto: ")
# 		if produto_df in estoque[loja]:
# 			preco_df = float(input("Novo preço do produto: "))
# 			if preco_df > 0:
# 				estoque[loja][produto_df]["preco"] = preco_df
# 				print("\nPerço alterado com sucesso!!")
# 			elif preco_df == 0:
# 				print("\nPreco não pode ser zero")
# 			else:
# 				print("\nPreco não pode ser negativo")
# 		else:
# 			print("\nProduto não está em estoque")

# #Se o número 6 for selecionado
# 	elif iniciar == "6":
# 		negativos = []
# 		for e in estoque[loja]:
# 			if estoque[loja][e]["quantidade"] < 0:
# 				negativos.append(e)
# 		print("\nProdutos em falta: ",negativos)

# #Se o número 7 for selecionado
# 	elif iniciar == "7":
# 		soma = 0
# 		for e in estoque[loja]:
# 			soma += (estoque[loja][e]["quantidade"]*estoque[loja][e]["preco"])
# 		print("\nValor total em estoque: {0} R$".format(soma))

# #Se o número 8 for selecionado
# 	elif iniciar == "8":
# 		resp = input("\nTem certeza que deseja apagar?\n1-Sim\n2-Não\n")
# 		if resp == "1":
# 			estoque = {}
# 			print("\nEstoque apagado com sucesso!!!")
# 		elif resp != "2":
# 			print("\nOpção inválida")
# #Erro
# 	else:
# 		print("\nOpção Inválida")

# #Transformando em firebase
# 	loja_fb = fb.patch("/estoque/lojas", estoque)

# #Selecionando 0
# print("\nVolte Sempre!!!")
