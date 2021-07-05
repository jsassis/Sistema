#Sistema de cadastro de anúncio.
#Autor: Jéssica Silva de Assis

from tkinter import *
import os
import datetime
import math

c = os.path.dirname(__file__)
nome_arquivo = c+'\\relatorio_anuncio.txt'

'''Cálculo investimento total'''

def investimentoT():
    investimento1 = float(investimento_dia.get())
    data2 = str(data_final.get())
    data1 = str(data_inicial.get())
    dataI = datetime.datetime.strptime(data1, '%d/%m/%Y')
    dataF = datetime.datetime.strptime(data2, '%d/%m/%Y')
    diferenca = (dataF.date() - dataI.date())
    DIF = diferenca.days
    investimento_total = investimento1 * DIF
    bt_investimento = (Label(janela, text=f'R${investimento_total}').place(x=200, y=350))

'''Cálculo compartilhamentos'''

def compartilhamentoT():
    investimento3 = float(investimento_dia.get())
    data6 = str(data_final.get())
    data5 = str(data_inicial.get())
    data_I = datetime.datetime.strptime(data5, '%d/%m/%Y')
    data_F = datetime.datetime.strptime(data6, '%d/%m/%Y')
    diff = data_F.date() - data_I.date()
    DIF = diff.days
    compartilhamento_total = (investimento3 * DIF * 30 * 0.12 * 0.15) / 4
    bt_compartilhamento = Label(janela, text=f'{compartilhamento_total}').place(x=220, y=450)

'''Cálculo cliques'''

def cliquesT():
    investimento2 = float(investimento_dia.get())
    data4 = str(data_final.get())
    data3 = str(data_inicial.get())
    data_i = datetime.datetime.strptime(data3, '%d/%m/%Y')
    data_f = datetime.datetime.strptime(data4, '%d/%m/%Y')
    dif = data_f.date() - data_i.date()
    DIF = dif.days
    cliques_total = investimento2 * DIF * 30 * 0.12
    bt_cliques = Label(janela, text=f'{cliques_total}').place(x=220, y=400)

'''Cálculo visualizações'''

def visualizacoesT():
    investimento4 = float(investimento_dia.get())
    data8 = str(data_final.get())
    data7 = str(data_inicial.get())
    dataIn = datetime.datetime.strptime(data7, '%d/%m/%Y')
    dataFi = datetime.datetime.strptime(data8, '%d/%m/%Y')
    d = dataFi.date() - dataIn.date()
    DIF = d.days
    visualizacoes_total = ((investimento4 * DIF * 0.12 * 30 * 40)/4) + (investimento4 * DIF * 30)
    bt_visualizacoes = Label(janela, text=f'{visualizacoes_total}').place(x=220, y=500)

'''Criar relatórios'''

def salvar_dados():
    investimentodiario = float(investimento_dia.get())
    datafinal = str(data_final.get())
    datainicial = str(data_inicial.get())
    dataInicial = datetime.datetime.strptime(datainicial, '%d/%m/%Y')
    dataFinal = datetime.datetime.strptime(datafinal, '%d/%m/%Y')
    DIF = dataFinal.date() - dataInicial.date()
    DIF = DIF.days
    investimentototal = investimentodiario * DIF * 0.12
    cliquetotal = investimentototal * 30 * 0.15
    compartilhamentototal = (cliquetotal / 4) * 40
    visualizacoestotal = investimentototal + cliquetotal + compartilhamentototal
    arquivo = open(nome_arquivo, "a")
    arquivo.write('\n\n-=-')
    arquivo.write('\nDATA_CONSULTA......:%s' % datetime.date.today())
    arquivo.write('\nANUNCIO............:%s' % nome.get())
    arquivo.write('\nCLIENTE............:%s' % cliente.get())
    arquivo.write('\nDATA_INICIAL.......:%s' % data_inicial.get())
    arquivo.write('\nDATA_FINAL.........:%s' % data_final.get())
    arquivo.write('\nINVESTIMENTO_DIA...:%s' % investimento_dia.get())
    arquivo.write('\nINVESTIMENTO_TOTAL.:%s' % investimentototal)
    arquivo.write('\nQUANTIDADE_DIAS....:%s' % DIF)
    arquivo.write('\nCLIQUES............:%s' % cliquetotal)
    arquivo.write('\nCOMPARTILHAMENTO...:%s' % compartilhamentototal)
    arquivo.write('\nVISUALIZACOES......:%s' % visualizacoestotal)
    arquivo.write('\n-=-')
    arquivo.close()

janela = Tk()
janela.geometry('390x610')
janela.title('FICHA DE CADASTRO')
janela.resizable(False, False)
janela.configure(background='#1c3743')

titulo = Label(janela, text='CADASTRE SEU ANÚNCIO', background='#1c3743', foreground='#fff',
               font=('verdana', 15, 'bold'))
titulo.place(x=10, y=10, width=370, height=80) #TÍTULO

'''Nome do anúncio'''
NOME = Label(janela, text='Nome do anúncio:', background='#1c3743', foreground='#fff', anchor=W)
NOME.place(x=30, y=100, width=150, height=20)
nome = Entry(janela) # NOME DO ANÚNCIO
nome.place(x=150, y=100, width=200, height=25)

'''Nome do cliente'''
CLIENTE = Label(janela, text='Nome do cliente:', background='#1c3743', foreground='#fff', anchor=W)
CLIENTE.place(x=30, y=150, width=150, height=20)
cliente = Entry(janela) # NOME DO CLIENTE
cliente.place(x=150, y=150, width=200, height=25)

'''Data inicial'''
DATA_INICIAL = Label(janela, text='Data inicial:', background='#1c3743', foreground='#fff', anchor=W)
DATA_INICIAL.place(x=30, y=200, width=150, height=20)
DATA_FORMATO = Label(janela, text='(dd/mm/aaaa)', background='#1c3743', foreground='#fff', anchor=W,
                     font=('verdana', 7))
DATA_FORMATO.place(x=30, y=215, width=150, height=20)
data_inicial = Entry(janela) # DATA INICIAL
data_inicial.place(x=150, y=200, width=200, height=25)

'''Data final'''
DATA_FINAL = Label(janela, text='Data final:', background='#1c3743', foreground='#fff', anchor=W)
DATA_FINAL.place(x=30, y=250, width=150, height=20)
data_formato = Label(janela, text='(dd/mm/aaaa)', background='#1c3743', foreground='#fff', anchor=W,
                     font=('verdana', 7))
data_formato.place(x=30, y=265, width=150, height=20)
data_final = Entry(janela) # DATA FINAL
data_final.place(x=150, y=250, width=200, height=25)

'''Investimento diário'''
INVESTIMENTO_DIA = Label(janela, text='Investimento diário:', background='#1c3743', foreground='#fff', anchor=W)
INVESTIMENTO_DIA.place(x=30, y=300, width=150, height=20)
investimento_dia = Entry(janela) # INVESTIMENTO DIÁRIO
investimento_dia.place(x=150, y=300, width=200, height=25)

'''Resultados'''

'''Investimento total'''
INVESTIMENTO_TOTAL = Label(janela, text='Valor total investido:', background='#1c3743', foreground='#fff', anchor=W)
INVESTIMENTO_TOTAL.place(x=30, y=350, width=300, height=20)

'''Máximo de cliques'''
CLIQUES = Label(janela, text='Máximo de cliques:', background='#1c3743', foreground='#fff', anchor=W)
CLIQUES.place(x=30, y=450, width=300, height=20)

'''Máximo de compartilhamento'''
COMPARTILHAMENTO = Label(janela, text='Máximo de compartilhamentos:', background='#1c3743', foreground='#fff',
                         anchor=W)
COMPARTILHAMENTO.place(x=30, y=400, width=300, height=20)

'''Máximo de visualizações'''
VISUALIZACOES = Label(janela, text='Máximo de visualizações:', background='#1c3743', foreground='#fff', anchor=W)
VISUALIZACOES.place(x=30, y=500, width=300, height=20)

#BOTÕES
'''Investimento total'''
Button(janela, text='CALCULAR', command=investimentoT).place(x=270, y=350, width=80, height=30)
'''Máximo de cliques'''
Button(janela, text='CALCULAR', command=cliquesT).place(x=270, y=400, width=80, height=30)
'''Máximo de compartilhamentos'''
Button(janela, text='CALCULAR', command=compartilhamentoT).place(x=270, y=450, width=80, height=30)
'''Máximo de visualizações'''
Button(janela, text='CALCULAR', command=visualizacoesT).place(x=270, y=500, width=80, height=30)
'''Salvador informações e gerar arquivo'''
Button(janela, text='SALVAR', font=('verdana', 8, 'bold'), command=salvar_dados).\
    place(x=155, y=555, width=80, height=30)

janela.mainloop()
