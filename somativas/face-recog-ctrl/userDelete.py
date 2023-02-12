import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import os
import shutil

def delShot():
    name = simpledialog.askstring(title="Delete", prompt="Digite o nome do usuário que deseja deletar:")

    folder = 'database'

    for name in os.listdir(folder):
        file_path = os.path.join(folder, name)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
            messagebox.showinfo("Sucesso!", "Usuário removido com sucesso")
        except IOError:
                print('Failed to delete %s. Reason: %s' % (file_path, e))