
#-----------------------------importações de bibliotecas para usar combobox a ordem importa
from tkinter.ttk import *
from tkinter import *


jlp = Tk()
jlp.geometry('450x300')

lb1 = Label(jlp, text='Selecione um local')
lb1.place(relx=0.15, rely= 0.2)

#---------------------- declaração de combo box--------------------------------------
combo = Combobox(jlp)

#-----------------------declaração dos valores da combo box ---------------------
combo['values'] = ['Brasil', 'Portugal', 'Escocia', 'Indonésia']

combo.place(relx=0.55, rely= 0.2)

# combo.current(0)

def mostrar_selecao():
    #------------------------------capturando o valor selecionado no combobox
    resultado = combo.get()
    print(resultado)

bt1 = Button(jlp, text= 'capturar', command=mostrar_selecao )
bt1.place(relx=0.1, rely=0.35)



mainloop()