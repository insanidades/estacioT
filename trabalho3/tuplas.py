primeira_tupla = (1, 2, 3, 4, "Olá, tupla")
print(f'O conteúdo da tupla: {primeira_tupla}')

el1 = primeira_tupla.index(4)
print(f'Existe o elemento 4 na tupla?')
print(bool(el1))

el2 = primeira_tupla.index(3)
print(f'Existe o elemento 3 na tupla?')
print(bool(el2))

try:
    el3 = primeira_tupla.index(33)
    print(f'Existe o elemento 33 na tupla?')
    print(True)
except ValueError:
    print(f'Existe o elemento 33 na tupla?')
    print(False)