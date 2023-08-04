from tkinter import * 


jP = Tk()

jP.geometry('350x200')
jP.title('Teste de Lambda')

def soma(a,b):
    res = a+b
    txtLb.set(res)

enp = Entry(jP, width=15)
enp.place(relx=0.1, rely=0.25)

ens = Entry(jP, width=15)
ens.place(relx=0.1, rely=0.40)





btCal = Button(jP, width=8, height=4, text='Calcular', command= lambda: soma( int(enp.get()),int(ens.get())))
btCal.place(relx=0.50, rely=0.25)

txtLb = StringVar()

lbRe = Label(jP, textvariable=txtLb , font=(' Cursive 24 bold'))
lbRe.place(relx=0.5, rely=0.7)


mainloop()