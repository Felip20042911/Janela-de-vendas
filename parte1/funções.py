import PySimpleGUI as sg
import pandas as pd


class janelas_função:
    def jp():
        lay = [
            [sg.Text('Numero da mesa: '), sg.Input(key='Mesa', size=(5,0))],
            [sg.Button('Enter'), sg.Button('valor')]
        ]
        return sg.Window('Principal', layout=lay, finalize=True)


    
    def mesa1():
        lay = [
            [sg.Text('codigo:     '), sg.Input(key='codigo', size=(5,0))],
        [sg.Text('quantidade: '), sg.Input(key='qnt', size=(4,0))],
        [sg.Button('confirmar'), sg.Button('voltar')]
        ]
        return sg.Window('valores1', layout=lay, finalize=True)

    def mesa2():
        lay = [
            [sg.Text('codigo:     '), sg.Input(key='codigo', size=(5,0))],
        [sg.Text('quantidade: '), sg.Input(key='qnt', size=(4,0))],
        [sg.Button('confirmar'), sg.Button('voltar')]
        ]
        return sg.Window('valores2', layout=lay, finalize=True)

    def mesa3():
        lay = [
            [sg.Text('codigo:     '), sg.Input(key='codigo', size=(5,0))],
        [sg.Text('quantidade: '), sg.Input(key='qnt', size=(4,0))],
        [sg.Button('confirmar'), sg.Button('voltar')]
        ]
        return sg.Window('valores3', layout=lay, finalize=True)
    def mesa4():
        lay = [
            [sg.Text('codigo:     '), sg.Input(key='codigo', size=(5,0))],
        [sg.Text('quantidade: '), sg.Input(key='qnt', size=(4,0))],
        [sg.Button('confirmar'), sg.Button('voltar')]
        ]
        return sg.Window('valores4', layout=lay, finalize=True)
    def mesa5():
        lay = [
            [sg.Text('codigo:     '), sg.Input(key='codigo', size=(5,0))],
        [sg.Text('quantidade: '), sg.Input(key='qnt', size=(4,0))],
        [sg.Button('confirmar'), sg.Button('voltar')]
        ]
        return sg.Window('valores5', layout=lay, finalize=True)
    def mesa6():
        lay = [
            [sg.Text('codigo:     '), sg.Input(key='codigo', size=(5,0))],
        [sg.Text('quantidade: '), sg.Input(key='qnt', size=(4,0))],
        [sg.Button('confirmar'), sg.Button('voltar')]
        ]
        return sg.Window('valores6', layout=lay, finalize=True)
    def mesa7():
        lay = [
            [sg.Text('codigo:     '), sg.Input(key='codigo', size=(5,0))],
        [sg.Text('quantidade: '), sg.Input(key='qnt', size=(4,0))],
        [sg.Button('confirmar'), sg.Button('voltar')]
        ]
        return sg.Window('valores7', layout=lay, finalize=True)
    def mesa8():
        lay = [
            [sg.Text('codigo:     '), sg.Input(key='codigo', size=(5,0))],
        [sg.Text('quantidade: '), sg.Input(key='qnt', size=(4,0))],
        [sg.Button('confirmar'), sg.Button('voltar')]
        ]
        return sg.Window('valores8', layout=lay, finalize=True)
    def mesa9():
        lay = [
            [sg.Text('codigo:     '), sg.Input(key='codigo', size=(5,0))],
        [sg.Text('quantidade: '), sg.Input(key='qnt', size=(4,0))],
        [sg.Button('confirmar'), sg.Button('voltar')]
        ]
        return sg.Window('valores9', layout=lay, finalize=True)
    def mesa10():
        lay = [
            [sg.Text('codigo:     '), sg.Input(key='codigo', size=(5,0))],
            [sg.Text('quantidade: '), sg.Input(key='qnt', size=(4,0))],
            [sg.Button('confirmar'), sg.Button('voltar')]
        ]
        return sg.Window('valores10', layout=lay, finalize=True)

    
class se:
    def mexendoo(windows, evento, valor, arq_mesa, jmesa1, a):
        if windows == jmesa1 and evento == 'confirmar' and valor['codigo'] == '1':
            arq_mesa.loc[arq_mesa['mesas'] == a, 'coca600'] = (valor['qnt'])
        arq_mesa.to_excel(r'C:\Users\FELIPE\Desktop\documentos\Pai\mesas\mesas\nova\mesaf.xlsx', index=False)

        if windows == jmesa1 and evento == 'confirmar' and valor['codigo'] == '2':
            arq_mesa.loc[arq_mesa['mesas'] == a, 'guarana600'] = valor['qnt']
            arq_mesa.to_excel(r'C:\Users\FELIPE\Desktop\documentos\Pai\mesas\mesas\nova\mesaf.xlsx', index=False)

        if windows == jmesa1 and evento == 'confirmar' and valor['codigo'] == '3':
            arq_mesa.loc[arq_mesa['mesas'] == a, 'fanta600'] = valor['qnt']
            arq_mesa.to_excel(r'C:\Users\FELIPE\Desktop\documentos\Pai\mesas\mesas\nova\mesaf.xlsx', index=False)

        if windows == jmesa1 and evento == 'confirmar' and valor['codigo'] == '4':
            arq_mesa.loc[arq_mesa['mesas'] == a, 'itaipavaLata'] = valor['qnt']
            arq_mesa.to_excel(r'C:\Users\FELIPE\Desktop\documentos\Pai\mesas\mesas\nova\mesaf.xlsx', index=False)

        if windows == jmesa1 and evento == 'confirmar' and valor['codigo'] == '5':
            arq_mesa.loc[arq_mesa['mesas'] == a, 'skolsLata'] = valor['qnt']
            arq_mesa.to_excel(r'C:\Users\FELIPE\Desktop\documentos\Pai\mesas\mesas\nova\mesaf.xlsx', index=False)

        if windows == jmesa1 and evento == 'confirmar' and valor['codigo'] == '6':
            arq_mesa.loc[arq_mesa['mesas'] == a, 'itaipavalatinha'] = valor['qnt']
            arq_mesa.to_excel(r'C:\Users\FELIPE\Desktop\documentos\Pai\mesas\mesas\nova\mesaf.xlsx', index=False)

        if windows == jmesa1 and evento == 'confirmar' and valor['codigo'] == '7':
            arq_mesa.loc[arq_mesa['mesas'] == a, 'skolslatinha'] = valor['qnt']
            arq_mesa.to_excel(r'C:\Users\FELIPE\Desktop\documentos\Pai\mesas\mesas\nova\mesaf.xlsx', index=False)

        if windows == jmesa1 and evento == 'confirmar' and valor['codigo'] == '8':
            arq_mesa.loc[arq_mesa['mesas'] == a, 'coca2L'] = valor['qnt']
            arq_mesa.to_excel(r'C:\Users\FELIPE\Desktop\documentos\Pai\mesas\mesas\nova\mesaf.xlsx', index=False)

        if windows == jmesa1 and evento == 'confirmar' and valor['codigo'] == '9':
            arq_mesa.loc[arq_mesa['mesas'] == a, 'guarana2L'] = valor['qnt']
            arq_mesa.to_excel(r'C:\Users\FELIPE\Desktop\documentos\Pai\mesas\mesas\nova\mesaf.xlsx', index=False)

        if windows == jmesa1 and evento == 'confirmar' and valor['codigo'] == '10':
            arq_mesa.loc[arq_mesa['mesas'] == a, 'fanta2L'] = valor['qnt']
            arq_mesa.to_excel(r'C:\Users\FELIPE\Desktop\documentos\Pai\mesas\mesas\nova\mesaf.xlsx', index=False)

