from PySimpleGUI import PySimpleGUI as g

class ExactData:

    def exactDataWindow(self):
        g.theme('Default')

        show_Data = [
            [g.Text("alo teste", key='-DATA-')]
        ]

        layout = [
            [g.Frame('Dados do Aluno', layout=show_Data, key='-CONTAINER-', size=(250,250))]
        ]

        window = g.Window('Mostragem dos Dados de um Aluno', layout=layout, size=(300,300), element_justification='c', finalize=True)

        while True:
            event, value = window.read()

            if event == g.WINDOW_CLOSED:
                break