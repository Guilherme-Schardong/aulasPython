import os
from tkinter import *
from tkinter import filedialog,messagebox

# origem = filedialog.askdirectory()
# destino = filedialog.askdirectory()
# arquivo = filedialog.askopenfilename()


# with open(arquivo,'w') as arqu:
#     arqu.write('origem,destino\n')
#     arqu.write(f'{origem}, {destino}')

#####################################################################################

# continuar = messagebox.askyesno(title= 'Acresentar uma nova linha', message='Gostaria de adicionar uma nova linha de origem e destino')

# arquivo = filedialog.askopenfilename()

# with open(arquivo,'w') as arqu:
#     arqu.write('origem,destino\n')

#     while continuar:

#         origem = filedialog.askdirectory()
#         destino = filedialog.askdirectory()
#         arqu.write(f'{origem}, {destino}')
#         continuar = messagebox.askyesno(title= 'Acresentar uma nova linha', message='Gostaria de adicionar uma nova linha de origem e destino')


#############################################################################################

def continuar (): 
    return messagebox.askyesno(title= 'Acresentar uma nova linha', message='Gostaria de adicionar uma nova linha de origem e destino')

arquivo = filedialog.askopenfilename()

with open(f'{arquivo}' ,'w') as arqu:
    arqu.write('origem,destino\n')

    while continuar():

        origem = filedialog.askdirectory()
        destino = filedialog.askdirectory()
        arqu.write(f'{origem}, {destino}')
        