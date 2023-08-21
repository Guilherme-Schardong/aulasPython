from tkinter import *



app = Tk()
app.geometry('300x250')

cor_vermelho = '0'
cor_verde = '0'
cor_azul= '0'
cor_app =f'#{cor_vermelho}{cor_verde}{cor_azul}'

lb_vermelho = Label(app, text='Vermelho')
lb_verde = Label(app, text='Verde')
lb_azul = Label(app, text='Azul')

lb_vermelho.place(relx=0.1,rely=0.15)
lb_verde.place(relx=0.35,rely=0.15)
lb_azul.place(relx=0.55,rely=0.15)

def setar_vermelho(value):
    global cor_vermelho    
    cor_vermelho = list(hex(int(value)))
    if(len(cor_vermelho) == 3):
        cor_vermelho = f'0{cor_vermelho[2]}'
    else:
        cor_vermelho = f'{cor_vermelho[2]}{cor_vermelho[3]}'
        
    print(cor_vermelho)
    # if(int(value)<=15):
    #     cor_vermelho = f'0{int(value):x}'
    # else:
    #     cor_vermelho = f'{int(value):x}'
   
    # setar_cor_fundo()
    
    

def setar_verde(value):
    global cor_verde
    cor_verde = list(hex(int(value)))
    if(len(cor_verde) == 3):
        cor_verde = f'0{cor_verde[2]}'
    else:
        cor_vermelho = f'{cor_verde[2]}{cor_verde[3]}'

def setar_azul(value):
    global cor_azul
    if(int(value)<=15):
        cor_azul = f'0{int(value):x}'
    else:
        cor_azul = f'0{int(cor_azul):x}'
    setar_cor_fundo()

def setar_cor_fundo():
    global cor_app
    global cor_vermelho
    global cor_verde
    global cor_azul
    if(int(cor_vermelho)<=15):
        cor_vermelho = f'0{int(cor_vermelho):x}'
    else:
        cor_vermelho = f'{int(cor_vermelho):x}'
    if(int(cor_verde)<=15):
        cor_verde = f'0{int(cor_verde):x}'
    else:
        cor_verde = f'{int(cor_verde):x}'
    if(int(cor_azul)<=15):
        cor_azul = f'0{int(cor_azul):x}'
    else:    
        cor_azul = f'{int(cor_azul):x}'
    cor_app = ''
    cor_app =f'#{cor_vermelho}{cor_verde}{cor_azul}'
    app.configure(bg= cor_app)

escala_vermelho = Scale(app, from_=0,to=255, command=setar_vermelho)
escala_vermelho.place(relx=0.1, rely=0.3)

escala_verde = Scale(app, from_=0, to=255, command=setar_verde)
escala_verde.place(relx=0.3, rely=0.3)

escala_azul = Scale(app, from_=0, to=255, command=setar_azul)
escala_azul.place(relx=0.5, rely=0.3)



app.mainloop()