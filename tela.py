# -*- encoding: utf-8 -*
from tkinter import *
from tkinter import messagebox
from random import randint


def num_entrada():
    global vlr_entrada
    vlr_entrada = int(float(tb_entrada.get()))
    print(f'Número digitado: {vlr_entrada}')
    tb_entrada.delete(0, END)


def gera_aleatorio():
    global vlr_random
    vlr_random = randint(1, 5)
    print(f'Número gerado: {vlr_random}')



def compara():
    if (vlr_entrada < vlr_random):
        messagebox.showinfo('Resultado','Você digitou um número abaixo do valor aleatório. Digite outro número')
    elif(vlr_entrada > vlr_random):
        messagebox.showinfo('Resultado','Você digitou um número acima do valor aleatório. Digite outro número')
    else:
        messagebox.showinfo('Resultado', 'O número aleatório era {}. Você acertou!!'.format(vlr_random))

tela = Tk()
tela.title('Random')
tela.geometry('225x195')
tela.resizable(False, False)
tela.eval('tk::PlaceWindow . center')
tela.configure(bg='darkgrey')

Label(tela, text='Escolha um número :',bg='darkgrey', fg='#000000').place(x=20, y=70,)
tb_entrada = Entry(tela)
tb_entrada.place(x=145, y=70, width=60, height=20)

btn_aleatorio = Button(tela, text='Gerar número aleatório', bg='#000000', fg='#ffffff', command=gera_aleatorio)
btn_aleatorio.place(x=20, y=10, width=185, height=50)
#
btn_entrada = Button(text='Grava número digitado', bg='#000000', fg='#ffffff', command=num_entrada)
btn_entrada.place(x=20, y=100, width=185, height=20)
#
btn_compara = Button(tela, text='Comparar', bg='#000000', fg='#ffffff', command=compara)
btn_compara.place(x=20, y=130, width=185, height=20)

btn_sair = Button(tela, text='Sair', command=tela.destroy, bg='#000000', fg='#ffffff')
btn_sair.place(x=20, y=160, width=185, height=20)

tela.mainloop()
