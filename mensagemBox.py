from tkinter import *
from tkinter import messagebox


app = Tk()
app.geometry('500x300')

def mostrarMsg(tipo_msg, msg):
    if(tipo_msg =='1'):
        messagebox.showinfo(title='Aula de mensagenBox', message=msg)
    elif(tipo_msg=='2'):
        messagebox.showwarning(title='Aula de mensagenBox', message=msg)
    elif(tipo_msg=='3'):
        messagebox.showerror(title='Aula de mensagenBox', message=msg)

def reset_entrada():
    res = messagebox.askyesno('reset', 'Deseja resetar o valor da entrda')
    if(res==True):
        entrada.delete(0,END)
    


msg = 'AUla de msageBox'

lb = Label(app, text='Selecione 1, 2 ou 3 para selecionar o tipo de menssagem')
lb.place(relx=0.05, rely=0.05)
entrada = Entry(app)
entrada.place(relx=0.15, rely=0.2)


bt = Button(app, text='mostrar mensagem', command=lambda:mostrarMsg(entrada.get(), msg))
bt.place(relx=0.15, rely=0.35)

btr = Button(app, text='Resetar entrada', command=reset_entrada)
btr.place(relx=0.15, rely=0.70)
mainloop()