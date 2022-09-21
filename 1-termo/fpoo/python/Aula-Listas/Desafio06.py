exp = str(input('Dgite a expressão: '))
if exp.count('(') == exp.count(')'):
    print("Sua expressão está válida!")
else:
    print("Sua expressão está errada!")