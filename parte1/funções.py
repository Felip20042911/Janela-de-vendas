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

    


