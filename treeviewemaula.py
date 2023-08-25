from tkinter import *

from tkinter import ttk,messagebox


def inserir():

    if vNome.get()=='' or vIdade.get()=='' or vSexo.get()=='':

        messagebox.showerror(title='Erro', message='Insira valores para acrensetar na lista')
        return

    tv.insert('','end', values=(vNome.get(),vIdade.get(),vSexo.get()))

    vNome.delete(0,END)

    vIdade.delete(0,END)

    vSexo.delete(0,END)

    vNome.focus()



def deletar():
    try:
        itemSelecionado = tv.selection()[0]
        tv.delete(itemSelecionado)
    except:
        messagebox.showerror(title='Erro', message='Selecione um item para poder deletar')

def obter():
    try:
        itemSelecionado = tv.selection()[0]
        valores = tv.item(itemSelecionado, 'values')
        print(valores)
    except:
        messagebox.showerror(title='Erro', message='Selecione um item para ser exibido')
    





app = Tk()

app.geometry('550x350')

app.title('TreeView')


lbNome = Label(app, text='Nome')

lbIdade = Label(app, text='Idade')

lbSexo = Label(app, text='Sexo')



vNome = Entry(app)

vIdade = Entry(app)

vSexo = Entry(app)




tv = ttk.Treeview(app, columns=('nome','idade','sexo'), show='headings')

tv.column('nome', minwidth=0, width=200)

tv.column('idade', minwidth=0, width=50)

tv.column('sexo', minwidth=0, width=150)

tv.heading('nome', text='Nome')

tv.heading('idade', text='Idade')

tv.heading('sexo', text='Sexo')


btn_inserir = Button(app, text='Inserir', command=inserir)

btn_deletar = Button(app, text='Deletar', command=deletar)

btn_obter = Button(app, text='Obter', command=obter)



tv.grid(column=0, row=3, columnspan=3, pady=5)


lbNome.grid(column=0,row=0)

vNome.grid(column=0,row=1)


lbIdade.grid(column=1,row=0)

vIdade.grid(column=1,row=1)


lbSexo.grid(column=2,row=0)

vSexo.grid(column=2,row=1)


btn_inserir.grid(column=0, row=4)

btn_deletar.grid(column=1, row=4)

btn_obter.grid(column=2, row=4)



#listaNomes = [['Guilherme','32','Masculino'],['Laura','25','Feminino'],['Jocasta','24','Feminino']]


#tv.insert('','end',values=('Pedro','45','Masculino'))


# for nome,idade,sexo in listaNomes:

#     tv.insert('','end', values=(nome,idade,sexo))





mainloop()