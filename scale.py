from tkinter import *

app = Tk()
app.geometry('500x300')

def mostrar(v):
    print(v)

slide= Scale(app, from_=0, to= 100, orient=HORIZONTAL, resolution=0.5, command=mostrar)
slide.place(relx=0.1, rely=0.2)

def noclick():
    print(slide.get())


bt= Button(app, text= 'Mostrar click', command=noclick)
bt.place(relx=0.25, rely=0.4)
mainloop()