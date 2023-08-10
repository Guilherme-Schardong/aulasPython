from tkinter import *

def add_value():
    lsib.insert(END,entrada.get())

def remove_item():
    lsib.delete(lsib.curselection())
    # a função curselection() retorna uma tulpa com a posição dos itens selecionados se nada foi selecionado retorna uma tupla vazia
    # para fins de comparação uma tumpla vazia é igual a () ou voce tambem pode utilizar o metodo ''.join() e dentro dele utilizar o 
    # curselection() para trransformar em uma string que para fins de comparação em caso de vazio é igual a ''.

def imp_selection():
    print(lsib.get(ACTIVE))

app = Tk()
app.geometry('500x300')

lista_atividades = ['futebol', 'volei', 'basquete']

lsib = Listbox(app)
lsib.place(relx=0.1, rely=0.1)

for atividade in lista_atividades:
    lsib.insert(END, atividade)
btad = Button(app, text='Adicionar Valor', command=add_value)
btad.place(relx=0.5, rely=0.1)

btremove = Button(app, text='Remover item selecionado', command=remove_item)
btremove.place(relx=0.5, rely=0.25)

btcapt = Button(app, text='printar item selecionado', command=imp_selection)
btcapt.place(relx=0.5, rely=0.6)

entrada = Entry(app)
entrada.place(relx=0.5, rely=0.45)
mainloop()
