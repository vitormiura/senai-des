from PySimpleGUI import PySimpleGUI as g
from ExactData import ExactData as e

class ShowData:

    def showDataWindow(self):
        g.theme('Default')

        show_Data = [
            [g.Text('CLICA', key='-DATA-', enable_events=True)]
        ]

        layout = [
            [g.Button('Voltar', key='-BACK-')],
            [g.Frame("Dados dos Alunos", layout=show_Data, key='-CONTAINER-', size=(450, 450))]
        ]

        window = g.Window('Mostragem dos Dados',layout=layout, size=(500,500), element_justification='c', finalize=True)

        while True:
            event, value = window.read()

            if event == g.WINDOW_CLOSED or event == '-BACK-':
                break

            elif event == '-DATA-':
                for i in range(10):
                    window.extend_layout(window['-CONTAINER-'], [[g.Text('salve', key=str(i), enable_events=True)]])

            elif event == '1':
                e.exactDataWindow(0)