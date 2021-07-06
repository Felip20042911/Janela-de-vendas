import pandas as pd
import PySimpleGUI as sg
from funções import janelas_função


#importando as mesas
arq_mesa = pd.read_excel(r"C:\Users\FELIPE\Desktop\documentos\Pai\mesas\table_1.xlsx")


#abrindo a janela principal
jprincipal, jmesa1, jmesa2, jmesa3 = janelas_função.jp(), None, None, None


#looping para permanecer tudo aberto
while True:
    windows, evento, valor = sg.read_all_windows()

    if windows == jprincipal and evento == sg.WIN_CLOSED:
        break
    if windows == jmesa1 and evento == sg.WIN_CLOSED:
        break
    if windows == jmesa2 and evento == sg.WIN_CLOSED:
        break
    if windows == jmesa3 and evento == sg.WIN_CLOSED:
        break


#navegação pelas janelas

    #enter
    if windows == jprincipal and evento == 'Enter' and valor['Mesa'] == '1':
        jmesa1 = janelas_função.mesa1()
        jprincipal.hide()
    if windows == jprincipal and evento == 'Enter' and valor['Mesa'] == '2':
        jmesa2 = janelas_função.mesa2()
        jprincipal.hide()
    if windows == jprincipal and evento == 'Enter' and valor['Mesa'] == '3':
        jmesa3 = janelas_função.mesa3()
        jprincipal.hide()


    #voltar
    if windows == jmesa1 and evento == 'voltar':
        jmesa1.hide()
        jprincipal.un_hide()
    if windows == jmesa2 and evento == 'voltar':
        jmesa2.hide()
        jprincipal.un_hide()
    if windows == jmesa3 and evento == 'voltar':
        jmesa3.hide()
        jprincipal.un_hide()



    #mexendo nos arquivos da mesa 1
    if windows == jmesa1 and evento == 'confirmar' and valor['codigo'] == '1':
        arq_mesa['refri'] = valor['qnt']
        arq_mesa.to_excel(r'C:\Users\FELIPE\Desktop\documentos\Pai\mesas\nova\mesa 1.xlsx', index=False)
    if windows == jmesa1 and evento == 'confirmar' and valor['codigo'] == '2':
        arq_mesa['cerveja'] = valor['qnt']
        arq_mesa.to_excel(r'C:\Users\FELIPE\Desktop\documentos\Pai\mesas\nova\mesa 1.xlsx', index=False)
    if windows == jmesa1 and evento == 'confirmar' and valor['codigo'] == '3':
        arq_mesa['comida'] = valor['qnt']
        arq_mesa.to_excel(r'C:\Users\FELIPE\Desktop\documentos\Pai\mesas\nova\mesa 1.xlsx', index=False)



    #mexendo nos arquivos da mesa 2
    if windows == jmesa2 and evento == 'confirmar' and valor['codigo'] == '1':
        arq_mesa['refri'] = valor['qnt']
        arq_mesa.to_excel(r'C:\Users\FELIPE\Desktop\documentos\Pai\mesas\nova\mesa 2.xlsx', index=False)
    if windows == jmesa2 and evento == 'confirmar' and valor['codigo'] == '2':
        arq_mesa['cerveja'] = valor['qnt']
        arq_mesa.to_excel(r'C:\Users\FELIPE\Desktop\documentos\Pai\mesas\nova\mesa 2.xlsx', index=False)
    if windows == jmesa2 and evento == 'confirmar' and valor['codigo'] == '3':
        arq_mesa['comida'] = valor['qnt']
        arq_mesa.to_excel(r'C:\Users\FELIPE\Desktop\documentos\Pai\mesas\nova\mesa 2.xlsx', index=False)


    
    #mexendo nos arquivos da mesa 3
    if windows == jmesa3 and evento == 'confirmar' and valor['codigo'] == '1':
        arq_mesa['refri'] = valor['qnt']
        arq_mesa.to_excel(r'C:\Users\FELIPE\Desktop\documentos\Pai\mesas\nova\mesa 3.xlsx', index=False)
    if windows == jmesa3 and evento == 'confirmar' and valor['codigo'] == '2':
        arq_mesa['cerveja'] = valor['qnt']
        arq_mesa.to_excel(r'C:\Users\FELIPE\Desktop\documentos\Pai\mesas\nova\mesa 3.xlsx', index=False)
    if windows == jmesa3 and evento == 'confirmar' and valor['codigo'] == '3':
        arq_mesa['comida'] = valor['qnt']
        arq_mesa.to_excel(r'C:\Users\FELIPE\Desktop\documentos\Pai\mesas\nova\mesa 3.xlsx', index=False)
