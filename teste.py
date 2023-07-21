from tkinter import *

def soma(a,b):
    resultado = a+b
    return resultado


janela = Tk()
janela.title('Soma')
janela.geometry('300x300')

texto_orientacao = Label(janela, text='insira dois valores para soma-los' )
texto_orientacao.grid(column='0',row='0', padx=10, pady=10 )

vA_text = Label(janela, text='Insira o primeiro Valor: ')
vA_text.grid(column='0', row='1')

vA_valor = Entry(janela, width=10)
vA_valor.grid(column='1', row='1')

vB_text = Label(janela, text='Insira o segundo Valor: ')
vB_text.grid(column='0', row='2')

vB_valor = Entry(janela, width=10)
vB_valor.grid(column='1', row='2')

def somarButton():
    prvalor= int(vA_valor.get())
    sgvalor= int(vB_valor.get())
    soma_resultado = soma(prvalor,sgvalor)
    resultado = Label(janela, text=soma_resultado)
    resultado.grid(column='0', row='5', padx= 50)

btSoma = Button(janela, text='Somar', command=somarButton)
btSoma.grid(column='0', row='4')

mainloop()