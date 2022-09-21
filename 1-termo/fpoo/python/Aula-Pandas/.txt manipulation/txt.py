f = open('texto.txt', 'w', encoding='utf8')
f.write('kkkkk\n')
f.write('haha\n')
f.write('café\n')
f.close()

try:
    f = open('texto.txt', 'r', encoding='utf8')
    f.seek(0)
    print(f.read())
finally:
    f.close()

