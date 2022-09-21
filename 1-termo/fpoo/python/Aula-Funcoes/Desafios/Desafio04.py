def maior():
    num = input('Escreva os numeros da lista separados por espaço: ')
    list = num.split()

    for i in range(len(list)):
        list[i] = int(list[i])

    m = (max(int(num) for num in list))
    print(f'Maior valor = {m}') 
maior()