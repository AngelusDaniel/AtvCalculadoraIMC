from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title('Cálculo de IMC - índice de Massa Corporal')
janela.geometry('550x250')
janela.configure(bg = 'white')

frame= Frame(janela, width = 235, height=50, bg='white', pady=0, padx=0, relief = 'flat')
frame.grid(row=0, column=0, stick=NSEW)



l_nome = Label(frame, text='Nome do paciente', width=10, height=1, padx=0, relief='flat', anchor='w', font=('Ivy 11'))
l_nome.grid(row=0, column=0, stick=NSEW, pady=10, padx=3)
e_nome = Entry(frame, width= 20 , relief='solid', font=('Ivy 11'), justify='center')
e_nome.grid(row=0, column=1,columnspan=3, stick=NSEW, pady=10, padx=3)


l_endereco = Label(frame, text='Endereço completo', width=20, height=1, padx=0, relief='flat', anchor='w', font=('Ivy 11'))
l_endereco.grid(row=1, column=0, stick=NSEW, pady=10, padx=3)
e_endereco = Entry(frame, width= 10 , relief='solid', font=('Ivy 11'), justify='center')
e_endereco.grid(row=1, column=1, columnspan=3, stick=NSEW, pady=10, padx=3)

l_altura = Label(frame, text='Altura (cm)', width=20, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 11'))
l_altura.grid(row=2, column=0, stick=NSEW, pady=10, padx=3)
e_altura = Entry(frame, width= 10 , relief='solid', font=('Ivy 11'), justify='center')
e_altura.grid(row=2, column=1, stick=NSEW, pady=10, padx=3)

l_peso = Label(frame, text='Peso (ckg)', width=20, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 11'))
l_peso.grid(row=3, column=0, stick=NSEW, pady=10, padx=3)
e_peso = Entry(frame, width= 10 , relief='solid', font=('Ivy 11'), justify='center')
e_peso.grid(row=3, column=1, stick=NSEW, pady=10, padx=3)

l_vazio = Label(frame, text='', width=20, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 11'))
l_vazio.grid(row=4, column=0, stick=NSEW, pady=10, padx=3)


l_resultado = Label(frame, text='resultado', width=20, height=1, padx=0, pady=6 ,  relief='flat', anchor='center', font=('Ivy 11'))
l_resultado.grid(row=2, rowspan=3, column=3, stick=NSEW, pady=10, padx=3)



janela.mainloop()