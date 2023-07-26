from tkinter import *



janela = Tk()
janela.title('Teste de cores')
janela['bg']= '#13678A'

janela.geometry('300x300+100+150')

lb = Label(janela,text='Esse texto no meio')
lb['fg']='#012030'

lb.place(y=5, x=5)
#lb.grid(column=0, row=0)

mainloop()