from tkinter import *


janela = Tk()
janela.title('Operações Basicas')


checsoma = IntVar()
checsubtracao = IntVar()
checmultiplicacao = IntVar()
checdivisao = IntVar()

c1 = Checkbutton(janela, text='soma', variable= checsoma, onvalue=1, offvalue= 0, justify='left')
c1.grid(column=0, row=0, padx=10, pady=10)
c2 = Checkbutton(janela, text='subtração', variable= checsubtracao, onvalue=1, offvalue= 0, justify='left')
c2.grid(column=0, row=1, padx=10, pady=10)
c3 = Checkbutton(janela, text='multiplicação', variable= checmultiplicacao, onvalue=1, offvalue= 0, justify='left')
c3.grid(column=0, row=2, padx=10, pady=10)
c4 = Checkbutton(janela, text='divisão', variable= checdivisao, onvalue=1, offvalue= 0, justify='left')
c4.grid(column=0, row=3, padx=10, pady=10)

def soma(a,b):
    resultado = a+b
    return resultado
def subtracao(a,b):
    resultado = a-b
    return resultado
def multiplicacao(a,b):
    resultado = a*b
    return resultado
def divisao(a,b):
    resultado =a/b
    return resultado

pvalor = Entry(janela)
pvalor.grid(column=1, row=5)
svalor = Entry(janela)
svalor.grid(column=1,row=6)

lb = Label(janela, text='resultado')
lb.grid(column=1,row=7, padx=10, pady=10)

def btclcick():
    num_um = int(pvalor.get())
    num_dois = int(svalor.get())
    somavar = int(checsoma.get())
    subvar = int(checsubtracao.get())
    multvar = int(checmultiplicacao.get())
    divvar = int(checdivisao.get())
    if somavar == 1:
        lb['text'] = soma(num_um,num_dois)
    elif subvar == 1:
        lb['text'] = subtracao(num_um,num_dois)
    elif multvar == 1:
        lb['text'] = multiplicacao(num_um,num_dois)
    elif divvar == 1:
        lb['text'] = divisao(num_um,num_dois)
    else:
        lb['text'] = 'Não selecionou nenhuma opção'
    
def zerar():
    checsoma, checmultiplicacao, checdivisao, checsubtracao = 0 ,0 ,0,0 
    c1.deselect()
    c2.deselect()
    c3.deselect()
    c4.deselect()
    lb['text'] = 'resultado'
    pvalor.delete(0)
    svalor.delete(0)
    
    

    

bt = Button(janela, width=20, text='ação' ,command=btclcick)
bt.grid(column=0, row=8, padx=10, pady=10)

bt2 = Button(janela, width=20, text='limpar', command= zerar)
bt2.grid(column=1, row=8, padx=10, pady=10)


mainloop()

