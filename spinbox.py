from tkinter import *

app = Tk()
app.geometry('500x300')

s1 = Spinbox(app, from_=0, to=10) 
s1.place(relx=0.25, rely=0.5)

s2 = Spinbox(app, values=('abacate', 'banana', 'abacaxi'), wrap=True) 
s2.place(relx=0.25, rely=0.75)

def executar():
    print(s2.get())


b1 = Button(app, text='executar', command=executar)
b1.place(relx=0.1, rely=0.35)

mainloop()