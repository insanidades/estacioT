lista_mesclada = [1, 2, 3, 'Olá, Python', True, 12.6]
print(lista_mesclada)

lista_mesclada.append(["Lista aninhada"])
print(f'Após o append {lista_mesclada}')

lista_mesclada.insert(4, '5')
print(f'Após o insert {lista_mesclada}')

print(f'O tamanho atual da lista é {len(lista_mesclada)}')

del lista_mesclada[1]
print(f'Após deletar o item da posição 1 {lista_mesclada}')

nova_lista_mesclada = lista_mesclada[:5]
print(nova_lista_mesclada)