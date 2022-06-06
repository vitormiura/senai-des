import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import os

def delShot():
    name = USER_INP = simpledialog.askstring(title="Delete",
                                    prompt="Digite o nome do usuário que deseja deletar:")

    parent_dir = 'database'

    try:
        path = os.path.join(parent_dir, name)
        os.remove(path)
        messagebox.showinfo("Sucesso!", "Usuário removido com sucesso")
    except IOError:
        messagebox.showerror("Erro!", "Usuário não encontrado")