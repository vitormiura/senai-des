from PySimpleGUI import PySimpleGUI as g
from ShowData import ShowData as s
from misc.style import *
import json

g.Window._move_all_windows = True
g.Window._minimize_all_windows = True

class ChooseFile:

    def chooseFileWindow(self):
        dict_json = self.gradesList()

        background_layout = [ 
            title_bar('Leitor XLS dos cria', g.theme_text_color(), g.theme_background_color()),
            [g.Image(data=background)],     
        ]

        window_background = g.Window('Background', background_layout, no_titlebar=True, finalize=True, margins=(0, 0), element_padding=(0,0), right_click_menu=[['Minimize'], ['Exit',]])

        window_background['-C-'].expand(True, False, False)

        layout = [
            [g.Text('Escolha o arquivo Excel', text_color="#000000")],
            [g.FileBrowse("Procurar Arquivo", target="-FILE-", size=(25, 2))],
            [g.Text("NOME DO ARQUIVO", key="-FILE-", text_color="#000000")],
            [g.Combo(dict_json, size=(25,0), default_value="Escolha a Grade", readonly=True)],
            [g.Button("Gerenciar Grade", key="-MANAGE-", size=(8,2)), g.Button("Confirmar", key="-CONFIRM-", size=(8,2))]
        ]


        # Panel para o menu de gerenciamento das grades. Deve ser oculto e so aparecer quando chamado
        # manageGrade = []

        window = g.Window('Chooser', layout, finalize=True, keep_on_top=True, grab_anywhere=False, no_titlebar=True)

        window_background.send_to_back()
        window.bring_to_front()

        while True:
            window, event, value = g.read_all_windows()
            print(event, value)

            if event is None or event == g.WINDOW_CLOSED or event == 'Exit':
                print(f'closing window = {window.Title}')
                break

            elif event == "-CONFIRM-":
                s.showDataWindow(0)

        window.close()
        window_background.close()

    # Retornar as chaves do JSON para uma lista, indo para as opcoes do select
    def gradesList(self):
        with open('./grades.json', 'r') as read_json:
            dict_json = json.load(read_json)

        keys_list = []
        for k,v in dict_json.items():
            keys_list.append(k)

        return keys_list

if __name__ == '__main__':
    background
    c = ChooseFile()
    c.chooseFileWindow()