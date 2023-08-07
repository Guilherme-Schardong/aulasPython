from tkinter import *

principal = Tk()

#-----------------------------------icon do aplicativo---------------------------------------------------------------
principal.iconbitmap('imgCbx\imagens\Gartoon-Team-Gartoon-Mimetype-App-x-emerald-theme.ico')


#---------------------------------- importação de imagens para a aplicação -------------------------------------------
logo = PhotoImage(file= r'imgCbx\imagens\fundo.png')

lbi = Label(principal, image= logo)

lbi.place(relx=0.1, rely=0.1)



mainloop()