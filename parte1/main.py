import pandas as pd
import PySimpleGUI as sg
from funções import janelas_função, se


#importando as mesas
arq_mesa = pd.read_excel(r"C:\Users\FELIPE\Desktop\documentos\Pai\mesas\mesas\mesa.xlsx")


#abrindo a janela principal
jprincipal, jmesa1, jmesa2, jmesa3, jmesa4, jmesa5, jmesa6, jmesa7, jmesa8, jmesa9, jmesa10 = janelas_função.jp(

), None, None, None, None, None, None, None, None, None, None


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
    if windows == jmesa4 and evento == sg.WIN_CLOSED:
        break
    if windows == jmesa5 and evento == sg.WIN_CLOSED:
        break
    if windows == jmesa6 and evento == sg.WIN_CLOSED:
        break
    if windows == jmesa7 and evento == sg.WIN_CLOSED:
        break
    if windows == jmesa8 and evento == sg.WIN_CLOSED:
        break
    if windows == jmesa9 and evento == sg.WIN_CLOSED:
        break
    if windows == jmesa10 and evento == sg.WIN_CLOSED:
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
    if windows == jprincipal and evento == 'Enter' and valor['Mesa'] == '3':
        jmesa4 = janelas_função.mesa4()
        jprincipal.hide()
    if windows == jprincipal and evento == 'Enter' and valor['Mesa'] == '3':
        jmesa5 = janelas_função.mesa5()
        jprincipal.hide()
    if windows == jprincipal and evento == 'Enter' and valor['Mesa'] == '3':
        jmesa6 = janelas_função.mesa6()
        jprincipal.hide()
    if windows == jprincipal and evento == 'Enter' and valor['Mesa'] == '3':
        jmesa7 = janelas_função.mesa7()
        jprincipal.hide()
    if windows == jprincipal and evento == 'Enter' and valor['Mesa'] == '3':
        jmesa8 = janelas_função.mesa8()
        jprincipal.hide()
    if windows == jprincipal and evento == 'Enter' and valor['Mesa'] == '3':
        jmesa9 = janelas_função.mesa9()
        jprincipal.hide()
    if windows == jprincipal and evento == 'Enter' and valor['Mesa'] == '3':
        jmesa10 = janelas_função.mesa10()
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
    if windows == jmesa4 and evento == 'voltar':
        jmesa4.hide()
        jprincipal.un_hide()
    if windows == jmesa5 and evento == 'voltar':
        jmesa5.hide()
        jprincipal.un_hide()
    if windows == jmesa6 and evento == 'voltar':
        jmesa6.hide()
        jprincipal.un_hide()
    if windows == jmesa7 and evento == 'voltar':
        jmesa7.hide()
        jprincipal.un_hide()
    if windows == jmesa8 and evento == 'voltar':
        jmesa8.hide()
        jprincipal.un_hide()
    if windows == jmesa9 and evento == 'voltar':
        jmesa9.hide()
        jprincipal.un_hide()
    if windows == jmesa10 and evento == 'voltar':
        jmesa10.hide()
        jprincipal.un_hide()




#mexendo nos arquivos da mesa 1
    se.mexendoo(windows, evento, valor, arq_mesa, jmesa1, 'mesa1')

#mexendo nos arquivos da mesa 2
    se.mexendoo(windows, evento, valor, arq_mesa, jmesa2, 'mesa2')

#mexendo nos arquivos da mesa 3
    se.mexendoo(windows, evento, valor, arq_mesa, jmesa3, 'mesa3')

#mexendo nos arquivos da mesa 4
    se.mexendoo(windows, evento, valor, arq_mesa, jmesa4, 'mesa4')

#mexendo nos arquivos da mesa 5
    se.mexendoo(windows, evento, valor, arq_mesa, jmesa5, 'mesa5')

#mexendo nos arquivos da mesa 6
    se.mexendoo(windows, evento, valor, arq_mesa, jmesa6, 'mesa6')

#mexendo nos arquivos da mesa 7
    se.mexendoo(windows, evento, valor, arq_mesa, jmesa7, 'mesa7')

#mexendo nos arquivos da mesa 8
    se.mexendoo(windows, evento, valor, arq_mesa, jmesa8, 'mesa8')

#mexendo nos arquivos da mesa 9
    se.mexendoo(windows, evento, valor, arq_mesa, jmesa9, 'mesa9')

#mexendo nos arquivos da mesa 10
    se.mexendoo(windows, evento, valor, arq_mesa, jmesa10, 'mesa10')

