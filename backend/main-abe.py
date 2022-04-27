import pandas as pd
import tkinter as tk
from tkinter import filedialog
from datetime import datetime
import json


def main():
    root = tk.Tk()
    root.withdraw()
    csv = get_file()
    selected = get_grade()
    # Cria tabela (dataframe) com os dados requisitados
    data_format = {
        "Nome": [],
        "Faltas": [],
        f"Faltas {selected[0]} - Seg": [],
        f"Faltas {selected[1]} - Ter": [],
        f"Faltas {selected[2]} - Qua": [],
        f"Faltas {selected[3]} - Qui": [],
        f"Faltas {selected[4]} - Sex": [],
    }
    df = pd.DataFrame(data_format)

    # Obtem a lista de alunos na Tabela
    alunos = list(csv.drop_duplicates(subset=["NomeAluno"])["NomeAluno"])

    for aluno in alunos:
        # Obtem todos os registros do aluno
        linha_aluno = csv.loc[csv["NomeAluno"] == aluno]
        arr = list()
        dia = {"faltas": 0, "aulas": 0}
        for i in range(5):
            arr.append(dia.copy())
        for (
            index,
            row,
        ) in linha_aluno.iterrows():
            # print(row['DataAula'])
            date_obj = datetime.strptime(row["DataAula"], "%d/%m/%Y")
            date_week = date_obj.weekday()
            arr[date_week]["faltas"] += int(row["NumeroFaltas"])
            arr[date_week]["aulas"] += int(row["TotalAulas"])
            # print(date_obj.weekday())
            # print(row['DataAula'], row['TotalAulas'], row['NumeroFaltas'])

        total_faltas_aluno = linha_aluno.sum(axis=0, skipna=True)["NumeroFaltas"]
        total_aulas_aluno = linha_aluno.sum(axis=0, skipna=True)["TotalAulas"]

        appenddata = {
            "Nome": aluno,
            "Faltas": total_faltas_aluno,
            f"Faltas {selected[0]} - Seg": arr[0]["faltas"],
            f"Faltas {selected[1]} - Ter": arr[1]["faltas"],
            f"Faltas {selected[2]} - Qua": arr[2]["faltas"],
            f"Faltas {selected[3]} - Qui": arr[3]["faltas"],
            f"Faltas {selected[4]} - Sex": arr[4]["faltas"],
        }
        # df = df.append(appenddata, ignore_index=True)
        df = pd.concat([df, pd.DataFrame.from_records([appenddata])])
        pd.set_option("display.width", None)
        pd.set_option("display.max_colwidth", None)

    print(df)


def add_grade(grades_json):
    semdays = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
    aulas_dia = []
    nome = input("Digite o nome da grade a ser adicionada: ")
    if nome in grades_json.keys():
        add_grade(grades_json)
    for i in range(5):
        aulas_dia.append(input(f'materia dia {semdays[i]} -> '))
    grades_json[nome] = aulas_dia
    with open('../grades.json', 'w') as f:
        json.dump(grades_json, f)


def delete_grade(grades_json):
    nome = input("Digite o nome da grade a ser deletada: ")
    if nome not in grades_json.keys():
        delete_grade(grades_json)
    del grades_json[nome]
    with open('../grades.json', 'w') as f:
        json.dump(grades_json, f)


def edit_grade(grades_json):
    semdays = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
    aulas_dia = []

    nome = input("Digite o nome da grade a ser editada: ")
    if nome not in grades_json.keys():
        edit_grade(grades_json)
    for i in range(5):
        aulas_dia.append(input(f'materia dia {semdays[i]} -> '))
    grades_json[nome] = aulas_dia
    with open('../grades.json', 'w') as f:
        json.dump(grades_json, f)


def get_grade():
    while True:
        with open('../grades.json', 'r') as read_json:
            grades_json = json.load(read_json)
        grades_disponiveis = []
        for grade in grades_json.keys():
            grades_disponiveis.append(grade)
        print("Grades disponiveis (-1 adiciona -2 deleta -3 edita) :")
        for i in range(len(grades_disponiveis)):
            print(f'{i} - {grades_disponiveis[i]}')
        escolhido = int(input("Escolha uma: "))
        if escolhido == -1:
            add_grade(grades_json)
            continue
        elif escolhido == -2:
            delete_grade(grades_json)
            continue
        elif escolhido == -3:
            edit_grade(grades_json)
            continue
        else:
            selected = grades_json[grades_disponiveis[escolhido]]
            return selected


def get_file():
    # Obtem o caminho do arquivo excel e lê os dados
    file_path = filedialog.askopenfilename()
    # file_path = "/home/abe/ws/leitor-xls-senai-old/abe/alunos.xls"
    pd.read_excel(file_path).to_csv(r"output.csv", index=None, header=True)
    csv = pd.read_csv(
        r"output.csv",
        encoding="UTF-8",
        usecols=[
            "NomeAluno",
            "DataAula",
            "TotalAulas",
            "NumeroFaltas",
            "NumeroAtrasos",
        ],
    )
    return csv


if __name__ == "__main__":
    main()
