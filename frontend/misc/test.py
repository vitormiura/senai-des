import PySimpleGUI as sg
from style import *

"""
    Highly experimental demo of how the illusion of a window with a background image is possible with PySimpleGUI.

    Requires the latest PySimpleGUI from GitHub.  Your copy of PySimpleGUI should be local to your application so that 
    the global variable _move_all_windows can be changed.  
    
    Copyright 2020 PySimpleGUI.org
"""


sg.Window._move_all_windows = True


def title_bar(title, text_color, background_color):
    """
    Creates a "row" that can be added to a layout. This row looks like a titlebar
    :param title: The "title" to show in the titlebar
    :type title: str
    :param text_color: Text color for titlebar
    :type text_color: str
    :param background_color: Background color for titlebar
    :type background_color: str
    :return: A list of elements (i.e. a "row" for a layout)
    :rtype: List[sg.Element]
    """
    bc = background_color
    tc = text_color
    font = 'Helvetica 12'

    return [sg.Col([[sg.T(title, text_color=tc, background_color=bc, font=font, grab=True)]], pad=(0, 0), background_color=bc),
            sg.Col([[sg.T('_', text_color=tc, background_color=bc, enable_events=True, font=font, key='-MINIMIZE-'), sg.Text('❎', text_color=tc, background_color=bc, font=font, enable_events=True, key='Exit')]], element_justification='r', key='-C-', grab=True,
                   pad=(0, 0), background_color=bc)]



def main():

    background_layout = [ title_bar('This is the titlebar', sg.theme_text_color(), sg.theme_background_color()),
                        [sg.Image(data=background)]]
    window_background = sg.Window('Background', background_layout, no_titlebar=True, finalize=True, margins=(0, 0), element_padding=(0,0), right_click_menu=[[''], ['Exit',]])

    window_background['-C-'].expand(True, False, False)  # expand the titlebar's rightmost column so that it resizes correctly


    # ------ Column Definition ------ #
    column1 = [[sg.Text('Column 1', justification='center', size=(10, 1))],
               [sg.Spin(values=('Spin Box 1', 'Spin Box 2', 'Spin Box 3'),
                        initial_value='Spin Box 1')],
               [sg.Spin(values=['Spin Box 1', '2', '3'],
                        initial_value='Spin Box 2')],
               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]

    layout = [
        [sg.Text('Window + Background Image\nWith tkinter', size=(30, 2), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
        [sg.Text('Here is some text.... and a place to enter text')],
        [sg.InputText('This is my text')],
        [sg.Frame(layout=[
            [sg.CBox('Checkbox', size=(10, 1)),
             sg.CBox('My second checkbox!', default=True)],
            [sg.Radio('My first Radio!     ', "RADIO1", default=True, size=(10, 1)),
             sg.Radio('My second Radio!', "RADIO1")]], title='Options', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
        [sg.MLine(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),
         sg.MLine(default_text='A second multi-line', size=(35, 3))],
        [sg.Combo(('Combobox 1', 'Combobox 2'),default_value='Combobox 1', size=(20, 1)),
         sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],
        [sg.OptionMenu(('Menu Option 1', 'Menu Option 2', 'Menu Option 3'))],
        [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3)),
         sg.Frame('Labelled Group', [[
             sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25, tick_interval=25),
             sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),
             sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),
             sg.Col(column1)]])
        ],
        [sg.Text('_' * 80)],
        [sg.Text('Choose A Folder', size=(35, 1))],
        [sg.Text('Your Folder', size=(15, 1), justification='right'),
         sg.InputText('Default Folder'), sg.FolderBrowse()],
        [sg.Submit(tooltip='Click to submit this form'), sg.Cancel()],
    [sg.Text('Right Click To Exit', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_SUNKEN)], ]

    top_window = sg.Window('Everything bagel', layout, finalize=True, keep_on_top=True, grab_anywhere=False,  transparent_color=sg.theme_background_color(), no_titlebar=True)

    # window_background.send_to_back()
    # top_window.bring_to_front()

    while True:
        window, event, values = sg.read_all_windows()
        print(event, values)
        if event is None or event == 'Cancel' or event == 'Exit':
            print(f'closing window = {window.Title}')
            break

    top_window.close()
    window_background.close()



if __name__ == '__main__':
    background
    main()