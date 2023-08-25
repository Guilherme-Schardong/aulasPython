from tkinter import *
from tkinter import ttk, messagebox


# app = Tk()
# app.geometry('600x300')

# listaNomes = [['0','Guilherme','9857'],['1','Bruna','8943'],['2','Jonas','8427']]

# tv = ttk.Treeview(app, columns=('id','nome','fone'), show='headings')
# tv.column('id', minwidth=0,width=50)
# tv.column('nome', minwidth=0,width=250)
# tv.column('fone', minwidth=0,width=150)
# tv.heading('id', text='ID')
# tv.heading('nome', text='NOME')
# tv.heading('fone', text='TELEFONE')
# tv.pack()

# #tv.insert('','end',values=('10','erich','9834'))

# for(id,nome,fone) in listaNomes:
#     tv.insert('','end',values=(id,nome,fone))


# mainloop()

###########################################################################

def inserir():
    if vid.get() ==''or vnome.get()==''or vfone.get()=='':
        messagebox.showerror(title='ERRO', message='Digite todos os dados')
        return
    tv.insert('','end',values=(vid.get(),vnome.get(),vfone.get()))
    vid.delete(0,END)
    vnome.delete(0,END)
    vfone.delete(0,END)
    vid.focus()

def deletar():
    try:
        itemSelecionado = tv.selection()[0]
        tv.delete(itemSelecionado)
    except:
        messagebox.showerror(title='ERRO', message='Selecione um elemento para ser deletado')

def obter():
    try:
        itemSelecionado = tv.selection()[0]
        valores=tv.item(itemSelecionado, 'values')
        print(valores)       
    except:
        messagebox.showerror(title='ERRO', message='Selecione um elemento para ser exibido')

app = Tk()
app.geometry('600x350')

ldid = Label(app,text='ID')
vid=Entry(app)

ldnome = Label(app,text='Nome')
vnome=Entry(app)

ldfone = Label(app,text='Fone')
vfone=Entry(app)


tv = ttk.Treeview(app, columns=('id','nome','fone'), show='headings')
tv.column('id', minwidth=0,width=50)
tv.column('nome', minwidth=0,width=250)
tv.column('fone', minwidth=0,width=150)
tv.heading('id', text='ID')
tv.heading('nome', text='NOME')
tv.heading('fone', text='TELEFONE')


btn_inserir = Button(app, text='Inserir', command=inserir)
btn_deletar = Button(app, text='Deletar', command=deletar)
btn_obter = Button(app, text='Obter', command=obter)

ldid.grid(column=0, row=0)
vid.grid(column=0, row=1)

ldnome.grid(column=1, row=0)
vnome.grid(column=1, row=1)

ldfone.grid(column=2, row=0)
vfone.grid(column=2, row=1)

tv.grid(column=0, row=3, columnspan=3, pady=5)

btn_inserir.grid(column=0, row=4)
btn_deletar.grid(column=1, row=4)
btn_obter.grid(column=2, row=4)

#tv.insert('','end',values=(id,nome,fone))


mainloop()