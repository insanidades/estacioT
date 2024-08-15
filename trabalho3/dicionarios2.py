dic = {
    1: {'nome': 'Maria', 'idade': 26, 'nacionalidade': 'brasileira'}
}

dic.update({
    2: {'nome': 'Daniel', 'idade': 20, 'nacionalidade': 'portuguesa'},
    3: {'nome': 'Castiel', 'idade': 19, 'nacionalidade': 'italiana'}
})

print(f'Após o dicionário ser atualizado: \n{dic}')

dic_copia = dic.copy() #Dicionário Cópia

elem_pop = dic.pop(3)
print(f'Após um item ser removido: \n{elem_pop} \nDicionário após o item removido: {dic}')

print(f'Após utilizar o "popitem" {dic.popitem()}')

#limpando
dic.clear()
dic_copia.clear()

new_chaves = ['1', '2', '3']
new_dicionario = dict.fromkeys(new_chaves, 'valor')

print('\nConteúdo do novo dicionário:')
print(new_dicionario.items())

print('\nChaves do novo dicionário:')
print(new_dicionario.keys())

print('\nValores do novo dicionário:')
print(new_dicionario.values())