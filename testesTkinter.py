from tkinter import *

janela = Tk()

#--------------Dimensinamento de tela ----------------------------------------

#janela.resizable(TRUE,FALSE )
# janela.maxsize(width= 800 , height= 600)
# janela.minsize(width= 400 , height= 300)
# btteste = Button(janela, text='Exemplo')
# btteste.place(relx=0.5, rely=0.5, relwidth=0.25, relheight=0.18)

#------------------Frames ou separadores-------------------------------

# fr= Frame(janela, bg='Blue')
# fr.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

# fr2= Frame(janela, bg='Red')
# fr2.place(relx=0.02, rely=0.50, relwidth=0.96, relheight=0.46)


#------------Bordas---------------------------

# lb1 = Label(janela, text='Solid', bd=10 , relief= SOLID)
# lb1.place(relx=0.5, rely= 0.02)
# lb2 = Label(janela, text='Flat', bd=10 , relief= FLAT)
# lb2.place(relx=0.5, rely=0.15)
# lb3 = Label(janela, text='Raised', bd=10 , relief= RAISED)
# lb3.place(relx=0.5, rely=0.3)
# lb4 = Label(janela, text='Sunken', bd=10 , relief= SUNKEN)
# lb4.place(relx=0.5, rely=0.45)
# lb5 = Label(janela, text='Ridge', bd=10 , relief= RIDGE)
# lb5.place(relx=0.5, rely=0.6)
# lb6 = Label(janela, text='Groove', bd=10 , relief= GROOVE)
# lb6.place(relx=0.5, rely=0.75)

#-------------efeitos de passar o mouse -------------------------------------------------

# bt = Button(janela, text='Efeitos', bd=5, relief=SOLID, overrelief=GROOVE )
# bt.place(relx=0.5, rely=0.5, relheight=0.18, relwidth=0.25)


#--------------------Checkbutton ------------------------------------------------------------

# def atribuir_valor():
#     lb_teste['text']= var1.get()

# var1 = StringVar()

# ch1 = Checkbutton(janela, text='teste de check', variable=var1, onvalue='checado', offvalue= 'nao checado' )

# ch1.place(relx=0.1, rely=0.1)

# bt = Button(janela, text='Verificar', command=atribuir_valor)

# bt.place(relx=0.25, rely=0.25)

# lb_teste = Label(janela, text='')
# lb_teste.place(rely=0.35, relx=0.50)


#--------------  multiplas janelas ---------------------------------s


# def abrir_nova_janela():
#     janela2 = Toplevel()
#     janela2.title('Nova janela')
#     janela2.transient(janela)
#     janela2.focus_force()
#     janela2.grab_set()
#     bt2 = Button(janela2 , text='fechar janela', command=janela2.destroy )
#     bt2.place(relx=0.5, rely= 0.5)




# bt = Button(janela, text='nova janela', command=abrir_nova_janela)
# bt.place(relx=0.5, rely= 0.5)

mainloop()
