def contador(* num):
    for valor in num:
        print(f'{valor}', end='|')
    print('')

contador(1, 5, 7, 9, 2, 5, 6, 7)
contador(4, 6, 8)
