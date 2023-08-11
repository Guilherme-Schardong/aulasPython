from tkinter import *

app = Tk()
app.geometry('500x300')

vl_a = IntVar()
vl_b = IntVar()
def noclick():
    print(f'a = {vl_a.get()} b = {vl_b.get()}')

ra_1 = Radiobutton(app, text='opção a 1', variable= vl_a, value=1, command=noclick, indicatoron=1)
ra_2 = Radiobutton(app, text='opção a 2', variable= vl_a, value=2,indicatoron=1)
ra_3 = Radiobutton(app, text='opção a 3', variable= vl_a, value=3,indicatoron=1)

rb_1 = Radiobutton(app, text='opção b 1', variable= vl_b, value=1)
rb_2 = Radiobutton(app, text='opção b 2', variable= vl_b, value=2)
rb_3 = Radiobutton(app, text='opção b 3', variable= vl_b, value=3)

ra_1.place(relx=0.1, rely=0.15 )
ra_2.place(relx=0.1, rely=0.35)
ra_3.place(relx=0.1, rely=0.55)

rb_1.place(relx=0.55, rely=0.15 )
rb_2.place(relx=0.55, rely=0.35)
rb_3.place(relx=0.55, rely=0.55)



bt= Button(app, text= 'Mostrar click', command=noclick)
bt.place(relx=0.25, rely=0.4)

mainloop()